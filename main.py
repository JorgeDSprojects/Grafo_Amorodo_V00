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
    # CONFIGURACIÓN DE PERSISTENCIA
    # El thread_id permite recuperar el maletín si el proceso se detiene
    config = {
        "configurable": {
            "thread_id": "sesion_pro_001",
            "model_name": "gpt-4o",  # <--- ¡Cambiamos el cerebro aquí!
            "temperature": 0.8
        }
    }

    # Ejecutamos el grafo pasando la configuración
    final_state = app.invoke(inputs, config=config)

    # 3. Inspeccionamos los resultados
    print("\n--- [RESULTADO DEL TEST] ---")
    print(f"💡 Idea Generada: \n{final_state.get('idea')}")
    print(f"📖 Borrador del Cuento: \n{final_state.get('story_draft')}")
    print(f"\n📈 Contador de Revisiones: {final_state.get('revision_count')}")
    print(f"🏷️ Título Final: \n{final_state.get('final_title')}")
    print(f"📝 Descripción Final: \n{final_state.get('final_description')}")
    
    if final_state.get('idea'):
        print("\n✅ TEST EXITOSO: El maletín ha pasado por los nodos correctamente.")
    else:
        print("\n❌ TEST FALLIDO: La idea no se generó.")

if __name__ == "__main__":
    # --- GENERACIÓN DEL DIAGRAMA ---
    # Lo colocamos aquí para que se genere siempre antes de correr el test
    try:
        with open("graph_diagram.png", "wb") as f:
            f.write(app.get_graph().draw_mermaid_png())
        print("🖼️ Diagrama del grafo guardado como 'graph_diagram.png'")
    except Exception as e:
        # En entornos de producción, es posible que falten dependencias de dibujo (como pygraphviz)
        print(f"⚠️ Nota: No se pudo generar el diagrama visual ({e}).")
        print("   Asegúrate de tener instaladas las dependencias necesarias si deseas la imagen.")

    # Ejecutar la prueba de los nodos
    run_test()