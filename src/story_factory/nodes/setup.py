from story_factory.state import StoryState
from story_factory.utils import get_past_stories_titles

def setup_node(state: StoryState):
    print("--- [FASE 0]: CONSULTANDO MEMORIA DE LARGO PLAZO ---")
    
    # Cargamos títulos previos para que el Ideator los conozca
    past_titles = get_past_stories_titles()
    
    return {
        "revision_count": 0,
        "past_story_references": past_titles
    }