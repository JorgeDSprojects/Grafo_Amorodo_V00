from langchain_core.prompts import ChatPromptTemplate
from story_factory.state import StoryState
from story_factory.utils import get_model

# Prompt profesional para el borrador del cuento
STORY_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """Eres un novelista premiado. Tu tarea es escribir un cuento completo basado en una idea previa.
    
    INSTRUCCIONES:
    1. Mantén la coherencia con la idea original: {idea}
    2. Escribe para el público objetivo: {audience}
    3. Respeta el formato solicitado: {format}
    4. Cumple con la longitud aproximada: {length}
    5. No uses NUNCA estas palabras prohibidas: {forbidden}
    
    Estilo: Narrativa fluida, rica en detalles y emocionalmente conectada con el lector."""),
    ("human", "Escribe el cuento completo basándote en la idea aprobada.")
])

def writer_node(state: StoryState):
    print("--- [FASE 3]: REDACTANDO BORRADOR COMPLETO ---")
    
    model = get_model(temperature=0.7)
    
    # Preparamos las variables del estado
    reqs = state["requirements"]
    
    chain = STORY_PROMPT | model
    
    response = chain.invoke({
        "idea": state["idea"],
        "audience": state["target_audience"],
        "format": reqs["format"],
        "length": reqs["length"],
        "forbidden": ", ".join(reqs["forbidden_words"])
    })
    
    return {"story_draft": response.content}