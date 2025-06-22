#!/usr/bin/env python
"""
RAG Agent Crew - Sistema Multi-Agente RAG 100% Local

⚠️  AVISO IMPORTANTE: PROYECTO EDUCATIVO Y DE LABORATORIO
📚 Este sistema está diseñado exclusivamente para fines educativos y de experimentación
🎓 Ideal para estudiantes, desarrolladores e investigadores
⚠️  El uso de este sistema es bajo la completa responsabilidad del usuario
🚫 NO está diseñado para uso en producción sin validaciones adicionales

📋 RESPONSABILIDADES DEL USUARIO:
- Verificar la precisión de toda información generada
- No usar para decisiones críticas sin validación humana
- Cumplir con regulaciones locales sobre uso de IA
- Usar únicamente con fines educativos y de experimentación responsable

💡 Objetivo: Aprender y experimentar con tecnologías de IA de manera responsable
"""

import sys
import warnings
from datetime import datetime
from pathlib import Path

from rag_agent.crew import RagAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the RAG-enhanced crew.
    
    ¿Por qué mantener la misma interfaz?
    - Compatibilidad con comandos existentes
    - Los agentes ahora usan RAG automáticamente
    - No requiere cambios en el flujo de usuario
    """
    inputs = {
        'topic': 'bases de datos vectoriales',
        'current_year': str(datetime.now().year)
    }
    
    try:
        print("🤖 Iniciando RAG Agent con capacidades de búsqueda vectorial...")
        print(f"📊 Tema: {inputs['topic']}")
        print(f"📅 Año: {inputs['current_year']}")
        print("=" * 60)
        
        RagAgent().crew().kickoff(inputs=inputs)
        
        print("\n" + "=" * 60)
        print("✅ RAG Agent completado exitosamente!")
        print("📄 Revisa el archivo 'report.md' para ver los resultados")
        
    except Exception as e:
        raise Exception(f"An error occurred while running the RAG crew: {e}")

def setup_knowledge_base():
    """
    Initialize the knowledge base with initial documents.
    
    ¿Por qué una función separada?
    - Permite configurar el sistema RAG antes del primer uso
    - Carga datos iniciales necesarios
    - Puede ejecutarse independientemente
    """
    try:
        print("🔧 Configurando base de conocimiento RAG...")
        
        # Importar y ejecutar el script de setup
        from rag_agent.setup_knowledge_base import main as setup_main
        setup_main()
        
    except Exception as e:
        raise Exception(f"Error setting up knowledge base: {e}")

def train():
    """
    Train the RAG-enhanced crew for a given number of iterations.
    
    ¿Por qué mantener entrenamiento?
    - Los agentes RAG también pueden mejorar con entrenamiento
    - Permite optimizar el uso de herramientas RAG
    - Mantiene compatibilidad con CrewAI
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        print("🏋️ Entrenando RAG Agent...")
        RagAgent().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the RAG crew: {e}")

def replay():
    """
    Replay the RAG crew execution from a specific task.
    """
    try:
        print("🔄 Reproduciendo ejecución de RAG Agent...")
        RagAgent().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the RAG crew: {e}")

def test():
    """
    Test the RAG crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        print("🧪 Probando RAG Agent...")
        RagAgent().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the RAG crew: {e}")

def search_knowledge():
    """
    Interactive search in the knowledge base.
    
    ¿Por qué esta funcionalidad?
    - Permite explorar la base de conocimiento directamente
    - Útil para debugging y verificación
    - Proporciona interfaz simple para consultas
    """
    try:
        from rag_agent.rag_client import RAGClient
        
        rag_client = RAGClient()
        
        print("🔍 Búsqueda interactiva en la base de conocimiento")
        print("Escribe 'quit' para salir")
        print("=" * 50)
        
        while True:
            query = input("\n💬 Tu consulta: ").strip()
            
            if query.lower() in ['quit', 'exit', 'salir']:
                print("👋 ¡Hasta luego!")
                break
            
            if not query:
                continue
                
            print(f"\n🔍 Buscando: {query}")
            results = rag_client.search_similar(query, limit=3)
            
            if results:
                print(f"📚 Encontrados {len(results)} resultados:")
                for i, result in enumerate(results, 1):
                    print(f"\n--- Resultado {i} (Score: {result['score']:.3f}) ---")
                    print(f"📄 Texto: {result['text'][:200]}...")
                    if result['metadata']:
                        print(f"🏷️ Categoría: {result['metadata'].get('category', 'N/A')}")
            else:
                print("❌ No se encontraron resultados relevantes")
                
    except Exception as e:
        print(f"❌ Error en búsqueda: {e}")

def show_help():
    """
    Show available commands for the RAG system.
    """
    help_text = """
🤖 RAG Agent - Sistema de Agentes con Recuperación Aumentada

⚠️  PROYECTO EDUCATIVO Y DE LABORATORIO
📚 Solo para fines educativos y experimentación
⚠️  Uso bajo responsabilidad del usuario

Comandos disponibles:

📊 EJECUCIÓN:
  run                    - Ejecutar el sistema RAG completo
  train <iterations> <file>   - Entrenar los agentes
  test <iterations> <model>   - Probar el sistema
  replay <task_id>       - Reproducir ejecución específica

🔧 CONFIGURACIÓN:
  setup                  - Configurar base de conocimiento inicial
  search                 - Búsqueda interactiva en la base de conocimiento

❓ AYUDA:
  help                   - Mostrar esta ayuda

📋 REQUISITOS PREVIOS:
  - Ollama ejecutándose en localhost:11434
  - Modelo llama3.2:latest descargado
  - Modelo nomic-embed-text:latest descargado
  - Qdrant ejecutándose en localhost:6333
  - Archivo .env configurado

🚀 INICIO RÁPIDO:
  1. crewai run setup    (configurar base de conocimiento)
  2. crewai run          (ejecutar sistema RAG)
    """
    print(help_text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == "setup":
            setup_knowledge_base()
        elif command == "search":
            search_knowledge()
        elif command == "help":
            show_help()
        else:
            print(f"❌ Comando desconocido: {command}")
            show_help()
    else:
        run()
