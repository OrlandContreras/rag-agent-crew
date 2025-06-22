#!/usr/bin/env python3
"""
Script para inicializar y poblar la base de conocimiento RAG

¿Por qué necesitamos este script?
- Inicializa la base de datos vectorial con datos útiles
- Carga documentos existentes de la carpeta knowledge/
- Proporciona datos de ejemplo para demostración
- Facilita el setup inicial del sistema RAG
"""

import os
import sys
from pathlib import Path
from .rag_client import RAGClient

def load_initial_documents():
    """
    Carga documentos iniciales en la base de conocimiento
    
    ¿Por qué estos documentos específicos?
    - Información base sobre IA y LLMs (tema por defecto)
    - Datos sobre el usuario (de user_preference.txt)
    - Conceptos fundamentales de RAG
    """
    
    rag_client = RAGClient()
    
    # Documentos base sobre IA y LLMs
    ai_documents = [
        {
            "text": """Los Large Language Models (LLMs) son modelos de inteligencia artificial entrenados en grandes cantidades de texto para entender y generar lenguaje natural. Ejemplos populares incluyen GPT-4, Claude, Llama, y Gemini. Estos modelos han revolucionado el procesamiento de lenguaje natural y tienen aplicaciones en chatbots, asistentes virtuales, generación de código, y análisis de texto.""",
            "metadata": {"category": "ai_fundamentals", "source": "setup", "topic": "llms_overview"}
        },
        {
            "text": """RAG (Retrieval-Augmented Generation) es una técnica que combina la recuperación de información con la generación de texto. Permite a los LLMs acceder a bases de conocimiento específicas para proporcionar respuestas más precisas y actualizadas. RAG consta de dos componentes principales: un sistema de recuperación (usando embeddings y bases de datos vectoriales) y un generador (LLM) que usa la información recuperada.""",
            "metadata": {"category": "ai_fundamentals", "source": "setup", "topic": "rag_concept"}
        },
        {
            "text": """Los embeddings son representaciones vectoriales de texto que capturan el significado semántico. Se usan en RAG para convertir documentos y consultas en vectores numéricos que permiten búsquedas por similitud. Modelos populares de embeddings incluyen sentence-transformers, OpenAI embeddings, y nomic-embed-text.""",
            "metadata": {"category": "ai_fundamentals", "source": "setup", "topic": "embeddings"}
        },
        {
            "text": """Qdrant es una base de datos vectorial de código abierto optimizada para búsquedas de similitud. Permite almacenar vectores de alta dimensión y realizar búsquedas rápidas usando diferentes métricas de distancia como coseno, euclidiana, y producto punto. Es especialmente útil para aplicaciones de RAG y búsqueda semántica.""",
            "metadata": {"category": "tools", "source": "setup", "topic": "qdrant"}
        },
        {
            "text": """Ollama es una herramienta que permite ejecutar modelos de lenguaje localmente. Soporta diversos modelos como Llama, Mistral, Code Llama, y modelos de embeddings. Proporciona una API compatible con OpenAI, lo que facilita la integración con aplicaciones existentes.""",
            "metadata": {"category": "tools", "source": "setup", "topic": "ollama"}
        }
    ]
    
    print("🚀 Iniciando carga de documentos base sobre IA...")
    for doc in ai_documents:
        success = rag_client.add_document(doc["text"], doc["metadata"])
        if success:
            print(f"✅ Documento sobre {doc['metadata']['topic']} añadido")
        else:
            print(f"❌ Error añadiendo documento sobre {doc['metadata']['topic']}")
    
    return len(ai_documents)

def load_knowledge_folder():
    """
    Carga documentos de la carpeta knowledge/
    
    ¿Por qué cargar esta carpeta?
    - Contiene información específica del usuario
    - Permite personalización del sistema
    - Aprovecha datos existentes del proyecto
    """
    
    rag_client = RAGClient()
    knowledge_path = Path("knowledge")
    
    if not knowledge_path.exists():
        print("⚠️ Carpeta 'knowledge' no encontrada")
        return 0
    
    docs_loaded = 0
    
    for file_path in knowledge_path.glob("*.txt"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                
                if content:
                    metadata = {
                        "category": "user_data",
                        "source": str(file_path),
                        "filename": file_path.name
                    }
                    
                    success = rag_client.add_document(content, metadata)
                    if success:
                        print(f"✅ Archivo {file_path.name} cargado")
                        docs_loaded += 1
                    else:
                        print(f"❌ Error cargando {file_path.name}")
                        
        except Exception as e:
            print(f"❌ Error procesando {file_path}: {e}")
    
    return docs_loaded

def test_rag_functionality():
    """
    Prueba básica de funcionalidad RAG
    
    ¿Por qué hacer pruebas aquí?
    - Valida que todo funciona correctamente
    - Proporciona ejemplos de uso
    - Detecta problemas de configuración temprano
    """
    
    print("\n🧪 Probando funcionalidad RAG...")
    
    rag_client = RAGClient()
    
    # Prueba de búsqueda
    test_queries = [
        "¿Qué es RAG?",
        "¿Cómo funcionan los embeddings?",
        "¿Qué información hay sobre el usuario?"
    ]
    
    for query in test_queries:
        print(f"\n🔍 Consulta: {query}")
        results = rag_client.search_similar(query, limit=2)
        
        if results:
            for i, result in enumerate(results, 1):
                print(f"   Resultado {i}: Score {result['score']:.3f}")
                print(f"   Texto: {result['text'][:100]}...")
        else:
            print("   ❌ No se encontraron resultados")

def main():
    """
    Función principal del script de setup
    """
    print("🎯 Iniciando configuración de la base de conocimiento RAG")
    print("=" * 60)
    
    try:
        # 1. Cargar documentos base
        base_docs = load_initial_documents()
        print(f"\n📚 Documentos base cargados: {base_docs}")
        
        # 2. Cargar carpeta knowledge
        knowledge_docs = load_knowledge_folder()
        print(f"📁 Documentos de knowledge/ cargados: {knowledge_docs}")
        
        # 3. Pruebas de funcionalidad
        test_rag_functionality()
        
        print("\n" + "=" * 60)
        print("✅ ¡Base de conocimiento configurada exitosamente!")
        print(f"📊 Total de documentos: {base_docs + knowledge_docs}")
        print("\n💡 El sistema RAG está listo para usar")
        
    except Exception as e:
        print(f"\n❌ Error durante la configuración: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 