from langgraph.graph import StateGraph, END
from story_factory.nodes.finalizer import finalizer_node # <-- Importar

def create_story_graph():
    workflow = StateGraph(StoryState)

    # 1. Nodos
    workflow.add_node("setup", setup_node)
    workflow.add_node("ideator", idea_generator_node)
    workflow.add_node("writer", writer_node)
    workflow.add_node("evaluator", evaluator_node)
    workflow.add_node("finalizer", finalizer_node) # <-- Añadir

    # 2. Aristas Fijas
    workflow.set_entry_point("setup")
    workflow.add_edge("setup", "ideator")
    workflow.add_edge("ideator", "writer")
    workflow.add_edge("writer", "evaluator")
    workflow.add_edge("finalizer", END) # El finalizador cierra el proceso

    # 3. Arista Condicional (Actualizada)
    workflow.add_conditional_edges(
        "evaluator",
        decide_to_finish,
        {
            "rewrite": "writer",
            "finalize": "finalizer" # <-- Ahora va al finalizador antes de terminar
        }
    )

    return workflow.compile()