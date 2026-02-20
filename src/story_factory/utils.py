import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_model(model_name: str = "gpt-4o-mini", temperature: float = 0.7):
    """Retorna el modelo solicitado con la temperatura deseada."""
    api_key = os.getenv("OPENAI_API_KEY")
    return ChatOpenAI(
        model=model_name,
        temperature=temperature,
        openai_api_key=api_key
    )


# src/story_factory/utils.py

def get_past_stories_titles():
    """Simula una consulta a una BBDD real de cuentos guardados."""
    # En un caso real, aquí harías un SELECT título FROM cuentos
    return ["El gato Chispa y el microondas", "Las crónicas de la tostadora"]