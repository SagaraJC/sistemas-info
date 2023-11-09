# Definición de funciones para las conversiones de moneda, temperatura y longitud
def conversion_moneda(valor, opcion):
    tasas_de_cambio = {
        1: 0.85,  # Dólar a Euro
        2: 1.18,  # Euro a Dólar
        3: 0.74,  # Dólar a Libra Esterlina
        4: 1.36,  # Libra Esterlina a Dólar
        5: 108.62,  # Yen a Dólar
        6: 0.0092  # Dólar a Yen
    }
    return valor * tasas_de_cambio[opcion]

def conversion_temperatura(valor, opcion):
    if opcion == 1:
        return (valor - 32) * 5/9  # Fahrenheit a Celsius
    elif opcion == 2:
        return valor * 9/5 + 32  # Celsius a Fahrenheit
    elif opcion == 3:
        return valor + 273.15  # Celsius a Kelvin
    elif opcion == 4:
        return (valor - 273.15) * 9/5 + 32  # Kelvin a Fahrenheit
    elif opcion == 5:
        return valor - 273.15  # Kelvin a Celsius

def conversion_longitud(valor, opcion):
    factores_de_conversion = {
        1: 0.3048,  # Pies a Metros
        2: 3.2808,  # Metros a Pies
        3: 0.0003048,  # Pies a Kilómetros
        4: 3280.84,  # Metros a Pulgadas
        5: 39.3701,  # Pulgadas a Metros
        6: 1.0936  # Yardas a Metros
    }
    return valor * factores_de_conversion[opcion]

# Bucle principal del programa
while True:
    print("Elija el tipo de unidad para convertir:")
    print("1. Monedas")
    print("2. Temperaturas")
    print("3. Longitudes")
    print("4. Salir del programa")
    
    # Leer la opción del usuario para el tipo de unidad
    tipo_unidad = int(input("Ingrese su opción: "))
    
    # Salir del programa si la opción es 4
    if tipo_unidad == 4:
        print("¡Hasta luego!")
        break
    
    # Verificar si la opción del usuario es válida
    if tipo_unidad not in [1, 2, 3]:
        print("Opción no válida. Por favor, ingrese una opción válida.")
        continue
    
    print("Elija el tipo de conversión:")
    
    # Mostrar opciones de conversión según el tipo de unidad seleccionado
    if tipo_unidad == 1:
        print("1. Dólar a Euro")
        print("2. Euro a Dólar")
        print("3. Dólar a Libra Esterlina")
        print("4. Libra Esterlina a Dólar")
        print("5. Yen a Dólar")
        print("6. Dólar a Yen")
    elif tipo_unidad == 2:
        print("1. Fahrenheit a Celsius")
        print("2. Celsius a Fahrenheit")
        print("3. Celsius a Kelvin")
        print("4. Kelvin a Fahrenheit")
        print("5. Kelvin a Celsius")
    elif tipo_unidad == 3:
        print("1. Pies a Metros")
        print("2. Metros a Pies")
        print("3. Pies a Kilómetros")
        print("4. Metros a Pulgadas")
        print("5. Pulgadas a Metros")
        print("6. Yardas a Metros")
    
    # Leer la opción de conversión del usuario
    opcion = int(input("Ingrese su opción de conversión: "))
    
    # Leer el valor a convertir del usuario
    valor = float(input("Ingrese el valor de la unidad: "))
    
    # Realizar la conversión según el tipo de unidad seleccionado y la opción de conversión
    if tipo_unidad == 1:
        resultado = conversion_moneda(valor, opcion)
    elif tipo_unidad == 2:
        resultado = conversion_temperatura(valor, opcion)
    elif tipo_unidad == 3:
        resultado = conversion_longitud(valor, opcion)
    
    # Mostrar el resultado de la conversión
    print("Resultado:", resultado)
    
    # Preguntar al usuario si desea cambiar de tipo de unidad o salir del programa
    continuar = input("¿Desea convertir otra unidad (s) o salir del programa (n)? ").lower()
    if continuar != 's':
        print("¡Hasta luego!")
        break