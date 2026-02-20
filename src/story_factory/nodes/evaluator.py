from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from story_factory.state import StoryState
from story_factory.utils import get_model
from pydantic import BaseModel, Field

# Definimos un esquema para la respuesta estructurada del evaluador
class Evaluation(BaseModel):
    score: int = Field(description="Puntuación del 1 al 10")
    feedback: str = Field(description="Explicación detallada de la nota y puntos a mejorar")

EVALUATOR_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """Eres un editor literario exigente. Tu misión es evaluar si el cuento cumple con los requisitos.
    
    CRITERIOS DE EVALUACIÓN:
    1. ¿Respeta el público objetivo ({audience})?
    2. ¿Evita las palabras prohibidas?
    3. ¿Es coherente con la idea original?
    4. ¿Tiene una calidad literaria alta?
    
    Responde SIEMPRE en formato JSON con las llaves 'score' y 'feedback'."""),
    ("human", "Evalúa este borrador: {draft}")
])

def evaluator_node(state: StoryState):
    print(f"--- [FASE 4]: EVALUANDO CALIDAD (Intento {state['revision_count'] + 1}) ---")
    
    model = get_model(temperature=0) # Temperatura 0 para una evaluación consistente
    parser = JsonOutputParser(pydantic_object=Evaluation)
    
    chain = EVALUATOR_PROMPT | model | parser
    
    res = chain.invoke({
        "audience": state["target_audience"],
        "draft": state["story_draft"]
    })
    
    # Actualizamos el estado con la nota, el feedback e incrementamos el contador
    return {
        "evaluation_score": res["score"],
        "evaluation_feedback": res["feedback"],
        "revision_count": state["revision_count"] + 1
    }