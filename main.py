from story_factory.graph import app
from story_factory.state import StoryRequirements

def run_test():
    print("🚀 Iniciando Test de Producción - Story Factory AI\n")

    # 1. Definimos el input inicial (Lo que el usuario enviaría)
    inputs = {
        "context": "Un gato que descubre que puede hablar con los electrodomésticos",
        "target_audience": "Niños de 8 a 10 años",
        "requirements": {
            "length": "corto",
            "format": "cuento infantil",
            "forbidden_words": ["muerte", "violencia"]
        },
        "past_story_references": ["El perro que bailaba", "La tostadora valiente"]
    }

    # 2. Ejecutamos el grafo
    # Al usar thread_id (opcional aquí) simulamos una sesión real
    final_state = app.invoke(inputs)

    # 3. Inspeccionamos los resultados
    print("\n--- [RESULTADO DEL TEST] ---")
    print(f"💡 Idea Generada: \n{final_state.get('idea')}")
    print(f"📖 Borrador del Cuento: \n{final_state.get('story_draft')}")
    print(f"\n📈 Contador de Revisiones: {final_state.get('revision_count')}")
    
    if final_state.get('idea'):
        print("\n✅ TEST EXITOSO: El maletín ha pasado por los nodos correctamente.")
    else:
        print("\n❌ TEST FALLIDO: La idea no se generó.")

if __name__ == "__main__":
    run_test()