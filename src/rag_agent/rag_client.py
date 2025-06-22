import os
import requests
import json
import numpy as np
from typing import List, Dict, Any, Optional
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Filter
from dotenv import load_dotenv

load_dotenv()

class RAGClient:
    """
    Cliente RAG que integra Ollama (LLM + Embeddings) con Qdrant (Vector DB)
    
    ¿Por qué esta arquitectura?
    - Ollama maneja tanto el LLM como los embeddings localmente
    - Qdrant proporciona búsqueda vectorial eficiente
    - Separamos las responsabilidades: embeddings, almacenamiento, recuperación
    """
    
    def __init__(self):
        # Configuración de Ollama
        self.ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.embedding_model = os.getenv("EMBEDDING_MODEL", "nomic-embed-text:latest")
        
        # Configuración de Qdrant
        self.qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
        self.collection_name = os.getenv("QDRANT_COLLECTION_NAME", "knowledge_base")
        
        # Inicializar clientes
        self.qdrant_client = QdrantClient(url=self.qdrant_url)
        
        # Crear colección si no existe
        self._ensure_collection_exists()
    
    def _ensure_collection_exists(self):
        """
        Crea la colección en Qdrant si no existe
        
        ¿Por qué 768 dimensiones?
        - nomic-embed-text genera vectores de 768 dimensiones
        - Distance.COSINE: mejor para similitud semántica en embeddings de texto
        """
        try:
            collections = self.qdrant_client.get_collections()
            collection_names = [col.name for col in collections.collections]
            
            if self.collection_name not in collection_names:
                self.qdrant_client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(
                        size=768,  # Dimensión de nomic-embed-text
                        distance=Distance.COSINE
                    )
                )
                print(f"✅ Colección '{self.collection_name}' creada en Qdrant")
            else:
                print(f"✅ Colección '{self.collection_name}' ya existe")
                
        except Exception as e:
            print(f"❌ Error al crear/verificar colección: {e}")
    
    def get_embedding(self, text: str) -> List[float]:
        """
        Genera embedding usando Ollama
        
        ¿Por qué Ollama para embeddings?
        - Control local completo
        - nomic-embed-text está optimizado para RAG
        - Consistencia con el stack local
        """
        try:
            response = requests.post(
                f"{self.ollama_base_url}/api/embeddings",
                json={
                    "model": self.embedding_model,
                    "prompt": text
                }
            )
            
            if response.status_code == 200:
                embedding = response.json()["embedding"]
                return embedding
            else:
                raise Exception(f"Error en Ollama: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error generando embedding: {e}")
            return []
    
    def add_document(self, text: str, metadata: Dict[str, Any] = None) -> bool:
        """
        Añade un documento a la base de conocimiento
        
        ¿Por qué incluir metadata?
        - Permite filtros más específicos en búsquedas
        - Útil para tracking de fuentes, fechas, categorías
        """
        try:
            # Generar embedding
            embedding = self.get_embedding(text)
            if not embedding:
                return False
            
            # Preparar payload
            payload = {
                "text": text,
                "metadata": metadata or {}
            }
            
            # Generar ID único basado en hash del texto
            import hashlib
            doc_id = hashlib.md5(text.encode()).hexdigest()
            
            # Insertar en Qdrant
            point = PointStruct(
                id=doc_id,
                vector=embedding,
                payload=payload
            )
            
            self.qdrant_client.upsert(
                collection_name=self.collection_name,
                points=[point]
            )
            
            print(f"✅ Documento añadido con ID: {doc_id}")
            return True
            
        except Exception as e:
            print(f"❌ Error añadiendo documento: {e}")
            return False
    
    def search_similar(self, query: str, limit: int = 5, score_threshold: float = 0.4) -> List[Dict]:
        """
        Busca documentos similares usando búsqueda vectorial
        
        ¿Por qué estos parámetros?
        - limit=5: Balance entre contexto y velocidad
        - score_threshold=0.7: Filtro de calidad para evitar resultados irrelevantes
        """
        try:
            # Generar embedding de la consulta
            query_embedding = self.get_embedding(query)
            if not query_embedding:
                return []
            
            # Búsqueda en Qdrant
            search_result = self.qdrant_client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=limit,
                score_threshold=score_threshold
            )
            
            # Formatear resultados
            results = []
            for hit in search_result:
                results.append({
                    "text": hit.payload.get("text", ""),
                    "metadata": hit.payload.get("metadata", {}),
                    "score": hit.score,
                    "id": hit.id
                })
            
            print(f"✅ Encontrados {len(results)} documentos similares")
            return results
            
        except Exception as e:
            print(f"❌ Error en búsqueda: {e}")
            return []
    
    def get_context_for_query(self, query: str, max_context_length: int = 2000) -> str:
        """
        Obtiene contexto relevante para una consulta (función principal de RAG)
        
        ¿Por qué limitar la longitud del contexto?
        - Los LLMs tienen límites de tokens
        - Demasiado contexto puede confundir al modelo
        - Balance entre información relevante y eficiencia
        """
        similar_docs = self.search_similar(query)
        
        if not similar_docs:
            return "No se encontró información relevante en la base de conocimiento."
        
        # Concatenar documentos hasta el límite
        context_parts = []
        current_length = 0
        
        for doc in similar_docs:
            text = doc["text"]
            if current_length + len(text) <= max_context_length:
                context_parts.append(f"[Fuente ID: {doc['id']}, Score: {doc['score']:.3f}]\n{text}")
                current_length += len(text)
            else:
                break
        
        context = "\n\n---\n\n".join(context_parts)
        
        return context if context else "No se encontró información relevante." 