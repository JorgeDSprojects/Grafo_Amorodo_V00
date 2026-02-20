from langgraph.checkpoint.sqlite import SqliteSaver # <-- Nuevo import
from langgraph.graph import StateGraph, END
from story_factory.state import StoryState
from story_factory.nodes.setup import setup_node
from story_factory.nodes.ideator import idea_generator_node
from story_factory.nodes.writer import writer_node
from story_factory.nodes.evaluator import evaluator_node
from story_factory.nodes.finalizer import finalizer_node  # Importamos el Hito 5

def decide_to_finish(state: StoryState):
    """Lógica de control para el bucle de calidad"""
    if state["evaluation_score"] >= 8 or state["revision_count"] >= 3:
        return "finalize"
    return "rewrite"

def create_story_graph():
    # Creamos la base de datos de checkpoints
    # En producción usarías una conexión persistente, aquí usamos una en memoria o archivo
    memory = SqliteSaver.from_conn_string(":memory:") # O "checkpoints.sqlite"
    # 1. Constructor
    workflow = StateGraph(StoryState)

    # 2. Registro de Nodos
    workflow.add_node("setup", setup_node)
    workflow.add_node("ideator", idea_generator_node)
    workflow.add_node("writer", writer_node)
    workflow.add_node("evaluator", evaluator_node)
    workflow.add_node("finalizer", finalizer_node)

    # 3. Aristas (Edges)
    workflow.set_entry_point("setup")
    workflow.add_edge("setup", "ideator")
    workflow.add_edge("ideator", "writer")
    workflow.add_edge("writer", "evaluator")
    
    # 4. El Bucle Condicional (Hito 4 + 5)
    workflow.add_conditional_edges(
        "evaluator",
        decide_to_finish,
        {
            "rewrite": "writer",
            "finalize": "finalizer"
        }
    )
    
    workflow.add_edge("finalizer", END)

    # 5. Compilación
    # 🔥 IMPORTANTE: Al compilar, añadimos el checkpointer
    return workflow.compile(checkpointer=memory)

# 🔥 ESTA ES LA LÍNEA QUE TE FALTA (fuera de la función) 🔥
app = create_story_graph()