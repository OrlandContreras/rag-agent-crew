from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os
from dotenv import load_dotenv

# Importar herramientas RAG
from .tools.rag_tools import RAGSearchTool, RAGAddDocumentTool, RAGContextTool

load_dotenv()

# Configuración de LLM para Ollama
# ¿Por qué esta configuración específica?
# - model: Especifica el modelo de Ollama a usar
# - base_url: URL de la API de Ollama (compatible con OpenAI)
# - temperature: 0.1 para respuestas más precisas en RAG (menos creativas, más factuales)
# - max_tokens: Suficiente para respuestas completas pero controladas
llm = LLM(
    model=os.getenv("MODEL", "ollama/mistral:7b"),
    base_url=os.getenv("API_BASE", "http://localhost:11434"),
    temperature=0.1,  # Reducido para mayor precisión en RAG
    max_tokens=1500,  # Reducido para respuestas más concisas
    timeout=60,  # Timeout de 60 segundos
)

@CrewBase
class RagAgent():
    """
    RagAgent crew con capacidades RAG integradas
    
    ¿Por qué esta transformación?
    - Los agentes ahora pueden buscar información específica
    - Combina capacidades de LLM con datos vectoriales
    - Mantiene la arquitectura multi-agente de CrewAI
    """

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        """
        Agente investigador con capacidades RAG
        
        ¿Por qué estas herramientas específicas?
        - RAGSearchTool: Para buscar información existente
        - RAGAddDocumentTool: Para almacenar hallazgos importantes
        - RAGContextTool: Para obtener contexto específico
        """
        return Agent(
            config=self.agents_config['researcher'], 
            verbose=True,
            llm=llm,
            tools=[
                RAGSearchTool(),
                RAGAddDocumentTool(),
                RAGContextTool()
            ]
        )

    @agent
    def reporting_analyst(self) -> Agent:
        """
        Agente analista con acceso a la base de conocimiento
        
        ¿Por qué el analista también necesita RAG?
        - Puede verificar información contra la base de conocimiento
        - Puede buscar datos específicos para enriquecer reportes
        - Mantiene consistencia con información almacenada
        """
        return Agent(
            config=self.agents_config['reporting_analyst'], 
            verbose=True,
            llm=llm,
            tools=[
                RAGSearchTool(),
                RAGContextTool()
            ]
        )

    @task
    def research_task(self) -> Task:
        """
        Tarea de investigación RAG-enhanced
        
        ¿Por qué mantener la misma configuración?
        - Las herramientas RAG se integran automáticamente
        - El agente decidirá cuándo usar RAG vs búsqueda web
        - Mantiene compatibilidad con configuración existente
        """
        return Task(
            config=self.tasks_config['research_task'], 
        )

    @task
    def reporting_task(self) -> Task:
        """
        Tarea de reporte con acceso a base de conocimiento
        """
        return Task(
            config=self.tasks_config['reporting_task'], 
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """
        Crea el crew RAG-enhanced
        
        ¿Por qué mantener Process.sequential?
        - El investigador primero busca/almacena información
        - El analista luego usa esa información para el reporte
        - Flujo lógico para maximizar uso de RAG
        """
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,            
        )
