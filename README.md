# 🤖 RAG Agent Crew - Sistema Multi-Agente RAG 100% Local

¡Bienvenido al proyecto **RAG Agent Crew**! Un **sistema multi-agente RAG completamente local** que combina [CrewAI](https://crewai.com), **Ollama** y **Qdrant** para crear agentes inteligentes colaborativos con acceso a conocimiento vectorial.

## ⚠️ **AVISO IMPORTANTE - Propósito Educativo y de Laboratorio**

🎓 **ESTE PROYECTO ES EXCLUSIVAMENTE PARA FINES EDUCATIVOS Y DE EXPERIMENTACIÓN**

- **📚 Propósito**: Este sistema está diseñado para **aprendizaje, investigación y experimentación** con tecnologías de IA, RAG y sistemas multi-agente
- **🧪 Ambiente de laboratorio**: Ideal para estudiantes, desarrolladores e investigadores que quieren **explorar y comprender** estas tecnologías
- **⚠️ Responsabilidad del usuario**: El **uso de este sistema es bajo la completa responsabilidad de cada individuo**
- **🚫 No para producción**: Este proyecto **NO está diseñado para uso en entornos de producción** sin las debidas modificaciones y validaciones

### 📋 **Responsabilidades del Usuario**
- ✅ Verificar la precisión de la información generada
- ✅ Validar resultados antes de tomar decisiones importantes  
- ✅ Cumplir con las regulaciones locales sobre uso de IA
- ✅ Usar con fines educativos y de experimentación responsable
- ❌ No usar para decisiones críticas sin validación humana
- ❌ No distribuir información generada sin verificación

**💡 El objetivo es aprender y experimentar con estas tecnologías de manera responsable.**

## 🌟 **Características Principales**

✅ **100% Local**: Sin APIs externas, sin límites de uso, privacidad total  
✅ **Multi-Agente**: Agentes especializados trabajando en equipo  
✅ **RAG Avanzado**: Búsqueda semántica en base de conocimiento vectorial  
✅ **Open Source**: Tecnologías abiertas y modificables  
✅ **Escalable**: Fácil agregar nuevos agentes y conocimiento

## 🚀 ¿Qué es este Sistema Multi-Agente RAG Local?

Un **ecosistema completo de IA** que ejecuta **100% en tu máquina local**, donde múltiples agentes especializados colaboran usando RAG (Retrieval-Augmented Generation) para resolver problemas complejos:

### **🤖 Agentes Colaborativos:**
- **Researcher Agent**: Investiga y almacena información en la base vectorial
- **Reporting Agent**: Analiza y genera reportes basados en conocimiento recuperado
- **Arquitectura extensible**: Fácil agregar nuevos agentes especializados

### **🧠 Capacidades RAG Avanzadas:**
- 🔍 **Búsqueda semántica inteligente** en base de conocimiento vectorial
- 💾 **Almacenamiento automático** de nuevos hallazgos
- 🔗 **Contexto enriquecido** para respuestas más precisas
- 📚 **Memoria persistente** entre sesiones

### **🏠 Ventajas de Ejecución Local:**
- 🔒 **Privacidad total**: Tus datos nunca salen de tu máquina
- 💰 **Costo cero**: Sin tarifas por token o uso
- ⚡ **Disponibilidad**: Funciona offline sin conexión
- 🎛️ **Control completo**: Personaliza modelos y configuraciones

### 🏗️ Arquitectura Multi-Agente RAG Local

```
    🏠 EJECUCIÓN 100% LOCAL 🏠
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  ┌─────────────────┐    ┌──────────────────┐    ┌─────┐ │
│  │   🤖 CrewAI     │    │  🧠 Ollama       │    │🔍 Q │ │
│  │   Multi-Agente  │◄──►│  LLM + Embeddings│◄──►│drant│ │
│  │                 │    │  (Local Models)  │    │ DB  │ │
│  └─────────────────┘    └──────────────────┘    └─────┘ │
│         │                        │                 │    │
│         ▼                        ▼                 ▼    │
│    📊 Orquestación        ⚡ Procesamiento    🔍 Búsqueda │
│    de Agentes             de IA Local        Vectorial  │
│                                                         │
│         🔄 Flujo RAG Colaborativo:                      │
│    Researcher 🔍 → Vectoriza → Almacena → Analista 📊   │
└─────────────────────────────────────────────────────────┘
```

## 📋 Requisitos Previos

### 1. **🧠 Ollama** (Motor de IA Local)
```bash
# Instalar Ollama (motor de LLMs locales)
curl -fsSL https://ollama.ai/install.sh | sh

# Descargar modelos para ejecución local
ollama pull mistral:7b               # LLM principal (eficiente)
ollama pull nomic-embed-text:latest  # Modelo de embeddings para RAG

# Verificar instalación
ollama list
```

### 2. **🔍 Qdrant** (Base de Datos Vectorial Local)
```bash
# Usando Podman (ejecución local containerizada)
podman run -d -p 6333:6333 --name qdrant qdrant/qdrant

# O usando Docker
docker run -d -p 6333:6333 --name qdrant qdrant/qdrant

# Verificar que esté ejecutándose
curl http://localhost:6333/health
```

### 3. **Python & Dependencias**
```bash
# Instalar UV (recomendado)
pip install uv

# O usar pip tradicional
pip install -r requirements.txt
```

## ⚡ Instalación Rápida

1. **Clonar y configurar el proyecto:**
```bash
git clone <tu-repo>
cd rag_agent
uv install  # o: pip install -e .
```

2. **Crear archivo de configuración:**
```bash
# Crear .env (basado en .env.example)
cp .env.example .env
# Editar .env según tu configuración
```

3. **Inicializar la base de conocimiento:**
```bash
crewai run setup
```

4. **Ejecutar el sistema RAG:**
```bash
crewai run
```

## 🔧 Configuración

### Archivo `.env`
```bash
# Configuración de Ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:latest
EMBEDDING_MODEL=nomic-embed-text:latest

# Configuración de Qdrant
QDRANT_URL=http://localhost:6333
QDRANT_COLLECTION_NAME=knowledge_base

# Configuración para CrewAI
MODEL=ollama/llama3.2:latest
API_BASE=http://localhost:11434/v1
```

## 🎯 Uso del Sistema

### Comandos Principales

| Comando | Descripción |
|---------|-------------|
| `crewai run` | Ejecuta el sistema RAG completo |
| `crewai run setup` | Configura la base de conocimiento inicial |
| `crewai run search` | Búsqueda interactiva en la base de conocimiento |
| `crewai run help` | Muestra ayuda completa |

### 🔄 Flujo Multi-Agente RAG Local

1. **🔍 Researcher Agent**: 
   - Busca información en la base de conocimiento local
   - Analiza y procesa datos usando Ollama (local)
   - Almacena nuevos hallazgos en Qdrant (local)

2. **📊 Reporting Agent**:
   - Recupera contexto relevante de la base vectorial
   - Genera reportes coherentes usando RAG
   - Todo procesado localmente sin APIs externas

3. **🔄 Colaboración**:
   - Los agentes comparten información a través de la base vectorial
   - Cada agente especializado en su dominio
   - Resultados mejorados por la colaboración multi-agente

## 🤖 Agentes del Sistema

### 🔬 **Researcher Agent** (Investigador RAG)
- **Rol**: Investigador senior con acceso a base de conocimiento vectorial
- **Herramientas**:
  - `RAGSearchTool`: Búsqueda semántica
  - `RAGAddDocumentTool`: Almacenamiento de documentos
  - `RAGContextTool`: Obtención de contexto específico

### 📊 **Reporting Analyst** (Analista RAG)
- **Rol**: Analista que verifica información contra la base de conocimiento
- **Herramientas**:
  - `RAGSearchTool`: Verificación de datos
  - `RAGContextTool`: Contexto para reportes

## 📁 Estructura del Proyecto

```
rag_agent/
├── src/rag_agent/
│   ├── rag_client.py              # Cliente RAG principal
│   ├── crew.py                    # Configuración de agentes
│   ├── main.py                    # Punto de entrada
│   ├── setup_knowledge_base.py    # Inicialización de datos
│   ├── config/
│   │   ├── agents.yaml           # Configuración de agentes
│   │   └── tasks.yaml            # Configuración de tareas
│   └── tools/
│       ├── rag_tools.py          # Herramientas RAG
│       └── custom_tool.py        # Herramientas personalizadas
├── knowledge/                     # Base de conocimiento inicial
│   └── user_preference.txt
├── .env                          # Variables de entorno
└── pyproject.toml               # Dependencias del proyecto
```

## 🔍 Stack Tecnológico 100% Local

### **🧠 Procesamiento de IA Local**
- **LLM**: Mistral 7B ejecutándose en Ollama
- **Embeddings**: nomic-embed-text (768 dimensiones)
- **Optimizado**: Para RAG y búsqueda semántica multilingüe
- **Sin dependencias externas**: Todo funciona offline

### **🔍 Base Vectorial Local**
- **Motor**: Qdrant (containerizado localmente)
- **Distancia**: Coseno (óptima para similitud semántica)
- **Persistencia**: Datos almacenados en tu máquina
- **Escalabilidad**: Millones de vectores sin límites de API

### **🤖 Orquestación Multi-Agente**
- **Framework**: CrewAI para coordinación de agentes
- **Arquitectura**: Agentes especializados colaborativos
- **Comunicación**: A través de base de conocimiento compartida
- **Extensibilidad**: Fácil agregar nuevos agentes especializados

## 🏆 Ventajas del Sistema Multi-Agente RAG Local

| Aspecto | Sistema Tradicional | Nuestro Sistema Multi-Agente RAG Local |
|---------|--------------------|-----------------------------------------|
| **Privacidad** | Datos en servidores externos | 🔒 100% local, datos nunca salen |
| **Costos** | Tarifas por token/mes | 💰 Cero costos de operación |
| **Disponibilidad** | Depende de internet/APIs | ⚡ Funciona offline completo |
| **Especialización** | Un solo agente genérico | 🤖 Múltiples agentes especializados |
| **Memoria** | Sin contexto persistente | 🧠 Base de conocimiento acumulativa |
| **Control** | Limitado por proveedor | 🎛️ Control total de configuración |

## 📊 Ejemplo de Uso

```python
# Búsqueda directa en la base de conocimiento
from rag_agent.rag_client import RAGClient

rag = RAGClient()

# Buscar información
results = rag.search_similar("¿Qué es RAG?", limit=3)

# Añadir nuevo documento
rag.add_document(
    text="RAG combina recuperación con generación...",
    metadata={"category": "ai_concepts", "source": "research"}
)
```

## 🚨 Solución de Problemas

### Problemas Comunes

| Problema | Solución |
|----------|----------|
| "Ollama connection error" | Verificar que Ollama esté ejecutándose: `ollama list` |
| "Qdrant connection failed" | Verificar contenedor: `podman ps` o `docker ps` |
| "No embedding model found" | Descargar modelo: `ollama pull nomic-embed-text:latest` |
| "Empty knowledge base" | Ejecutar: `crewai run setup` |

### Verificación del Sistema
```bash
# Verificar Ollama
curl http://localhost:11434/api/version

# Verificar Qdrant
curl http://localhost:6333/health

# Verificar modelos
ollama list
```

## 🔧 Personalización

### Añadir Nuevos Documentos
1. Colocar archivos `.txt` en la carpeta `knowledge/`
2. Ejecutar: `crewai run setup`

### Modificar Agentes
- Editar `src/rag_agent/config/agents.yaml`
- Ajustar roles, objetivos y estrategias

### Crear Herramientas Personalizadas
- Extender `src/rag_agent/tools/rag_tools.py`
- Seguir el patrón de `BaseTool` de CrewAI


---

## 🎯 **¿Por qué elegir un Sistema Multi-Agente RAG Local?**

### **🔒 Máxima Privacidad y Seguridad**
- Todos tus datos permanecen en tu máquina local
- Sin riesgo de filtraciones o acceso no autorizado
- Cumplimiento automático de regulaciones de privacidad
- Control total sobre información sensible

### **💰 Economía y Sostenibilidad**
- Sin costos recurrentes de APIs o servicios cloud
- Una sola inversión en hardware vs. pagos mensuales
- Escalabilidad sin incremento de costos
- ROI inmediato para uso intensivo

### **🤖 Inteligencia Colaborativa Superior**
- Múltiples agentes especializados > un agente genérico
- Cada agente perfeccionado para su dominio específico
- Colaboración inteligente entre agentes
- Resultados de mayor calidad y precisión

### **🧠 Memoria y Aprendizaje Continuo**
- Base de conocimiento que crece con el uso
- Contexto persistente entre sesiones
- Aprendizaje acumulativo sin límites
- Conocimiento organizacional preservado

### **⚡ Performance y Disponibilidad**
- Latencia ultra-baja (sin round-trips a APIs)
- Disponibilidad 24/7 sin dependencias externas
- Escalabilidad horizontal en tu infraestructura
- Control de recursos y optimizaciones

---

**🚀 ¡Experimenta el futuro de la IA: Multi-Agente, RAG y 100% Local!**

*Donde la privacidad, el control y la inteligencia colaborativa se encuentran.*

## 📄 Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE) - consulta el archivo LICENSE para más detalles.

### ¿Qué significa la Licencia MIT?

✅ **Uso Libre**: Puedes usar este software para cualquier propósito  
✅ **Modificación**: Puedes modificar el código como necesites  
✅ **Distribución**: Puedes distribuir copias del software  
✅ **Uso Comercial**: Puedes usar este software en proyectos comerciales  
✅ **Uso Privado**: Puedes usar el software de forma privada  

📋 **Únicos Requisitos**:
- Incluir la licencia y copyright en distribuciones
- No usar el nombre de los autores para promoción sin permiso

🛡️ **Sin Garantías**: El software se proporciona "tal como está" sin garantías

---

## ⚠️ **DESCARGO DE RESPONSABILIDAD Y USO EDUCATIVO**

### 🎓 **Finalidad Educativa y de Investigación**

Este proyecto **RAG Agent Crew** está diseñado exclusivamente para:
- **📚 Aprendizaje y educación** sobre tecnologías de IA, RAG y sistemas multi-agente
- **🔬 Investigación y experimentación** en entornos controlados de laboratorio
- **💡 Comprensión práctica** de la integración de LLMs, bases vectoriales y agentes

### ⚖️ **Responsabilidad del Usuario**

**EL USO DE ESTE SISTEMA ES BAJO LA COMPLETA RESPONSABILIDAD DEL USUARIO:**

- **🔍 Verificación obligatoria**: Toda información generada debe ser verificada antes de su uso
- **🚫 No para decisiones críticas**: No usar para decisiones médicas, legales, financieras o de seguridad
- **📝 Validación humana**: Siempre requiere supervisión y validación humana experta
- **⚖️ Cumplimiento legal**: El usuario debe cumplir con todas las regulaciones locales e internacionales

### 🚨 **Limitaciones Importantes**

- **❌ No es un sistema de producción**: Requiere modificaciones adicionales para uso productivo
- **❌ No garantiza precisión**: Los resultados pueden contener errores o información incorrecta
- **❌ No substituye expertise humano**: Complementa pero no reemplaza el juicio profesional
- **❌ No para uso crítico**: No usar en sistemas donde errores puedan causar daños

### 📋 **Recomendaciones de Uso Responsable**

1. **🧪 Experimentación controlada**: Usar solo en entornos de prueba y aprendizaje
2. **📚 Propósitos educativos**: Ideal para aprender sobre IA y sistemas RAG
3. **🔬 Investigación académica**: Perfecto para estudios y proyectos de investigación
4. **💡 Desarrollo de prototipos**: Base para desarrollar sistemas más robustos

### 💬 **Mensaje Final**

**Este proyecto busca democratizar el acceso a tecnologías avanzadas de IA para fines educativos.** Su valor está en el aprendizaje, la experimentación y la comprensión de estas tecnologías emergentes.

**Úsalo con responsabilidad, aprende de él, y contribuye a un futuro más informado sobre IA.**

---

*© 2025 RAG Agent Crew - Proyecto educativo bajo Licencia MIT*
