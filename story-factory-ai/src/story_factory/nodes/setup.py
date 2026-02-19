from story_factory.state import StoryState

def setup_node(state: StoryState):
    """Inicializa contadores y limpia entradas si es necesario."""
    print("--- [FASE 0 & 1]: CONFIGURANDO ENTORNO ---")
    
    # Aseguramos valores por defecto si no vienen en el input inicial
    return {
        "revision_count": 0,
        "past_story_references": state.get("past_story_references", []),
        "story_draft": None,
        "idea": None
    }