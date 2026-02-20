from langgraph.checkpoint.memory import MemorySaver # <-- Cambiamos el import
from langgraph.graph import StateGraph, END
from story_factory.state import StoryState
from story_factory.nodes.setup import setup_node
from story_factory.nodes.ideator import idea_generator_node
from story_factory.nodes.writer import writer_node
from story_factory.nodes.evaluator import evaluator_node
from story_factory.nodes.finalizer import finalizer_node

def decide_to_finish(state: StoryState):
    """Lógica de control para el bucle de calidad"""
    if state["evaluation_score"] >= 8 or state["revision_count"] >= 3:
        return "finalize"
    return "rewrite"

def create_story_graph():
    # 1. Usamos MemorySaver (no necesita context manager)
    # Esto permite la persistencia por thread_id durante la ejecución
    memory = MemorySaver() 

    # 2. Constructor
    workflow = StateGraph(StoryState)

    # 3. Registro de Nodos
    workflow.add_node("setup", setup_node)
    workflow.add_node("ideator", idea_generator_node)
    workflow.add_node("writer", writer_node)
    workflow.add_node("evaluator", evaluator_node)
    workflow.add_node("finalizer", finalizer_node)

    # 4. Aristas (Edges)
    workflow.set_entry_point("setup")
    workflow.add_edge("setup", "ideator")
    workflow.add_edge("ideator", "writer")
    workflow.add_edge("writer", "evaluator")
    
    # 5. Bucle Condicional
    workflow.add_conditional_edges(
        "evaluator",
        decide_to_finish,
        {
            "rewrite": "writer",
            "finalize": "finalizer"
        }
    )
    
    workflow.add_edge("finalizer", END)

    # 6. Compilación con el checkpointer
    return workflow.compile(checkpointer=memory)

# Exportamos la aplicación
app = create_story_graph()