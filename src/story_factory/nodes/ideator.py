from langchain_core.prompts import ChatPromptTemplate
from story_factory.state import StoryState
from story_factory.utils import get_model

# Definimos el Prompt siguiendo el estándar de producción
IDEA_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """Eres un director creativo experto en narrativa. 
    Tu objetivo es proponer una idea única para un cuento basada en el contexto del usuario.
    
    REGLAS:
    1. No repitas ideas parecidas a estas referencias previas: {past_references}
    2. Ajusta el tono para el público: {audience}
    3. Respeta estas restricciones: {requirements}"""),
    ("human", "Genera una idea para un cuento basado en este contexto: {context}")
])

def idea_generator_node(state: StoryState):
    print("--- [FASE 2]: GENERANDO IDEA CREATIVA ---")
    
    # Extraemos la configuración. Si no viene nada, usamos valores por defecto.
    configurable = config.get("configurable", {})
    model_name = configurable.get("model_name", "gpt-4o-mini")
    temp = configurable.get("temperature", 0.9) # Más creativo para ideas
    
    model = get_model(model_name=model_name, temperature=temp)
    # Creamos la cadena LCEL
    chain = IDEA_PROMPT | model
    
    # Ejecutamos pasando los datos del estado
    response = chain.invoke({
        "context": state["context"],
        "audience": state["target_audience"],
        "requirements": state["requirements"],
        "past_references": ", ".join(state["past_story_references"])
    })
    
    return {"idea": response.content}