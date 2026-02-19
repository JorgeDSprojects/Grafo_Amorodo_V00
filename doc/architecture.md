story-factory-ai/
├── src/
│   ├── story_factory/
│   │   ├── __init__.py
│   │   ├── state.py       <-- Definición del "Maletín" (Hito 1)
│   │   ├── nodes/         <-- Aquí irán los "trabajadores"
│   │   │   ├── __init__.py
│   │   │   ├── setup.py
│   │   │   └── writer.py
│   │   └── graph.py       <-- La orquestación de LangGraph
├── .env                   <-- Tus API Keys (no se sube a GitHub)
├── pyproject.toml
└── main.py                <-- Punto de entrada de la app
