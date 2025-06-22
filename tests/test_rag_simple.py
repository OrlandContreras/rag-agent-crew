#!/usr/bin/env python3
"""
Script de prueba simple para el sistema RAG
"""

from datetime import datetime
from src.rag_agent.crew import RagAgent

def test_simple():
    """
    Prueba simple del sistema con límites estrictos
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    
    print("🔥 Iniciando prueba simple del sistema RAG...")
    print("=" * 50)
    
    try:
        # Crear el crew
        crew = RagAgent().crew()
        
        # Ejecutar solo con timeout
        result = crew.kickoff(inputs=inputs)
        
        print("\n" + "=" * 50)
        print("✅ ¡Prueba completada!")
        print(f"📄 Resultado: {result}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_simple() 