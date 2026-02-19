from langgraph.graph import StateGraph, END
from story_factory.state import StoryState
from story_factory.nodes.setup import setup_node
from story_factory.nodes.ideator import idea_generator_node

def create_story_graph():
    # 1. Crear el constructor del grafo con nuestro State
    workflow = StateGraph(StoryState)

    # 2. Añadir los nodos definidos
    workflow.add_node("setup", setup_node)
    workflow.add_node("ideator", idea_generator_node)

    # 3. Establecer las conexiones (Edges)
    workflow.set_entry_point("setup")
    workflow.add_edge("setup", "ideator")
    workflow.add_edge("ideator", END) # De momento termina aquí

    return workflow.compile()

# Instancia para exportar
app = create_story_graph()