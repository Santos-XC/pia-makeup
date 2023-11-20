# URL de la API makeup-api
api_url = "http://makeup-api.herokuapp.com/api/v1/products.json"

#inicializacion de datos
data = None

while True:
    opcion = input("¿Qué deseas hacer?\n1. Consultar API\n2. Cargar datos\n3. Analizar datos\n4. Generar gráficas\n5. Salir\nOpción: ")

    if opcion == "1":
        data = consultar_api(api_url)
        if data:
            guardar_opcion = input("¿Deseas guardar los datos consultados? (S/N): ").strip().lower()
            if guardar_opcion == "s":
                guardar_datos(data, "makeup_data.json")
    elif opcion == "2":
        data = cargar_datos("makeup_data.json")
    elif opcion == "3":
        resultado_analisis = analizar_datos(data)

        if resultado_analisis:
            promedio, producto_mas_comprado, maquillaje_mas_utilizado = resultado_analisis
            print(f"Promedio de precios: ${promedio:.2f}")
        else:
            print("No hay datos para analizar. Consulta la API o carga datos.")
            
    elif opcion == "4":
        generar_graficas(data)
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Introduce una opción válida.")