from langchain_core.prompts import ChatPromptTemplate
from story_factory.state import StoryState
from story_factory.utils import get_model

FINALIZER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """Eres un experto en marketing editorial. Tu tarea es poner el título perfecto 
    y una descripción atractiva (blurb) para el cuento que se te presenta.
    
    REGLAS:
    1. El título debe ser sugerente y original.
    2. La descripción debe enganchar al público objetivo ({audience}) sin hacer spoilers.
    3. Responde indicando claramente el Título y la Descripción."""),
    ("human", "Aquí tienes el cuento final: {story}")
])

def finalizer_node(state: StoryState):
    print("--- [FASE 5]: GENERANDO TÍTULO Y DESCRIPCIÓN FINAL ---")
    
    model = get_model(temperature=0.8) # Un poco de creatividad para el título
    
    chain = FINALIZER_PROMPT | model
    
    # Invocamos basándonos en el borrador que ya fue aprobado
    response = chain.invoke({
        "audience": state["target_audience"],
        "story": state["story_draft"]
    })
    
    # Aquí podrías usar un parser para separar título y descripción, 
    # por ahora lo guardamos como texto procesado
    return {
        "final_title": "Título Generado", # Simulación de extracción
        "final_description": response.content 
    }