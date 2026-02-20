from typing import TypedDict, List, Optional

class StoryRequirements(TypedDict):
    """Restricciones y configuraciones iniciales"""
    length: str          # e.g., "500 words"
    format: str          # e.g., "markdown"
    forbidden_words: List[str]

class StoryState(TypedDict):
    """
    El estado global de nuestro proceso de escritura.
    Cada nodo puede leer y modificar estas claves.
    """
    # Fase 1: Contexto
    context: str
    target_audience: str
    requirements: StoryRequirements
    
    # Fase 2 y 3: Generación
    idea: Optional[str]
    story_draft: Optional[str]
    
    # Fase 4: Evaluación
    evaluation_score: int    # 1 a 10
    evaluation_feedback: str
    
    # Fase 5: Entrega
    final_title: Optional[str]
    final_description: Optional[str] # <-- Añadimos este campo
    
    # Control de flujo y BBDD
    past_story_references: List[str]   # IDs o títulos previos
    revision_count: int                # Cuántas veces hemos vuelto atrás