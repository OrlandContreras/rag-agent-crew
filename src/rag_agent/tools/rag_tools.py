from crewai.tools import BaseTool
from typing import Type, List, Dict, Any
from pydantic import BaseModel, Field
from ..rag_client import RAGClient

class RAGSearchInput(BaseModel):
    """Input schema para búsqueda RAG."""
    query: str = Field(..., description="Consulta o pregunta para buscar en la base de conocimiento")
    max_results: int = Field(default=5, description="Número máximo de resultados a retornar")

class RAGAddDocumentInput(BaseModel):
    """Input schema para añadir documentos."""
    text: str = Field(..., description="Texto del documento a añadir a la base de conocimiento")
    category: str = Field(default="general", description="Categoría del documento")
    source: str = Field(default="unknown", description="Fuente del documento")

class RAGSearchTool(BaseTool):
    """
    Herramienta para buscar información en la base de conocimiento vectorial
    
    ¿Por qué esta herramienta es esencial?
    - Permite a los agentes acceder a información específica
    - Convierte consultas en contexto relevante
    - Mejora la precisión de las respuestas
    """
    name: str = "rag_search"
    description: str = (
        "Busca información relevante en la base de conocimiento usando búsqueda semántica. "
        "Úsala cuando necesites información específica sobre un tema para responder preguntas "
        "o completar tareas con datos precisos."
    )
    args_schema: Type[BaseModel] = RAGSearchInput
    
    def _run(self, query: str, max_results: int = 5) -> str:
        """
        Ejecuta la búsqueda RAG
        
        ¿Por qué retornar string y no objeto?
        - CrewAI espera strings como output de herramientas
        - Formato legible para que el LLM pueda procesarlo
        """
        try:
            # Crear cliente RAG
            rag_client = RAGClient()
            # Obtener contexto relevante
            context = rag_client.get_context_for_query(query, max_context_length=3000)
            
            if "No se encontró información" in context:
                return f"❌ No se encontró información relevante para la consulta: '{query}'"
            
            # Formatear respuesta para el agente
            formatted_response = f"""
🔍 RESULTADOS DE BÚSQUEDA RAG:
Consulta: {query}

📋 INFORMACIÓN ENCONTRADA:
{context}

💡 Esta información proviene de la base de conocimiento vectorial y es relevante para tu consulta.
"""
            return formatted_response
            
        except Exception as e:
            return f"❌ Error en búsqueda RAG: {str(e)}"

class RAGAddDocumentTool(BaseTool):
    """
    Herramienta para añadir documentos a la base de conocimiento
    
    ¿Por qué necesitamos esta herramienta?
    - Permite que los agentes enriquezcan la base de conocimiento
    - Útil para almacenar resultados de investigaciones
    - Mejora el sistema de forma incremental
    """
    name: str = "rag_add_document"
    description: str = (
        "Añade un documento a la base de conocimiento vectorial para futuras consultas. "
        "Úsala cuando encuentres información valiosa que debería ser recordada y consultada más tarde."
    )
    args_schema: Type[BaseModel] = RAGAddDocumentInput
    
    def _run(self, text: str, category: str = "general", source: str = "unknown") -> str:
        """
        Añade documento a la base de conocimiento
        """
        try:
            # Crear cliente RAG
            rag_client = RAGClient()
            metadata = {
                "category": category,
                "source": source,
                "added_by": "agent"
            }
            
            success = rag_client.add_document(text, metadata)
            
            if success:
                return f"✅ Documento añadido exitosamente a la categoría '{category}' desde fuente '{source}'"
            else:
                return f"❌ Error al añadir documento a la base de conocimiento"
                
        except Exception as e:
            return f"❌ Error añadiendo documento: {str(e)}"

class RAGContextTool(BaseTool):
    """
    Herramienta especializada para obtener contexto específico para preguntas
    
    ¿Por qué una herramienta separada para contexto?
    - Optimizada específicamente para proveer contexto a LLMs
    - Formato más limpio y estructurado
    - Control fino sobre la cantidad de contexto
    """
    name: str = "get_rag_context"
    description: str = (
        "Obtiene contexto específico y relevante de la base de conocimiento para responder "
        "una pregunta específica. El contexto está optimizado para ser usado por LLMs."
    )
    args_schema: Type[BaseModel] = RAGSearchInput
    
    def _run(self, query: str, max_results: int = 3) -> str:
        """
        Obtiene contexto limpio para el LLM
        """
        try:
            # Crear cliente RAG
            rag_client = RAGClient()
            context = rag_client.get_context_for_query(query, max_context_length=2000)
            
            if "No se encontró información" in context:
                return "CONTEXTO: No hay información específica disponible en la base de conocimiento para esta consulta."
            
            return f"CONTEXTO RELEVANTE:\n{context}"
            
        except Exception as e:
            return f"ERROR AL OBTENER CONTEXTO: {str(e)}" 