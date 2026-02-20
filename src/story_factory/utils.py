import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_model(temperature=0.7):
    # Usamos gpt-4o-mini por su excelente relación calidad/precio
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=temperature,
        api_key=os.getenv("OPENAI_API_KEY")
    )


# src/story_factory/utils.py

def get_past_stories_titles():
    """Simula una consulta a una BBDD real de cuentos guardados."""
    # En un caso real, aquí harías un SELECT título FROM cuentos
    return ["El gato Chispa y el microondas", "Las crónicas de la tostadora"]