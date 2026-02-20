from langgraph.graph import StateGraph, END
from story_factory.state import StoryState
from story_factory.nodes.setup import setup_node
from story_factory.nodes.ideator import idea_generator_node
from story_factory.nodes.writer import writer_node # <-- Importar nuevo nodo

def create_story_graph():
    workflow = StateGraph(StoryState)

    # 1. Añadir los nodos
    workflow.add_node("setup", setup_node)
    workflow.add_node("ideator", idea_generator_node)
    workflow.add_node("writer", writer_node) # <-- Añadir al flujo

    # 2. Definir las aristas (edges)
    workflow.set_entry_point("setup")
    workflow.add_edge("setup", "ideator")
    workflow.add_edge("ideator", "writer") # De ideator pasamos a writer
    workflow.add_edge("writer", END)        # De momento terminamos aquí

    return workflow.compile()

app = create_story_graph()