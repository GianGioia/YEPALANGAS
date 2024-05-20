def calculadora_cientifica():
    print("Calculadora Científica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Salir")
    eleccion = int(input("Elige una operación: "))

    if eleccion == 7:
        return
    else:
        num1 = float(input("Ingresa el primer número: "))
        if eleccion != 6:
            num2 = float(input("Ingresa el segundo número: "))

        if eleccion == 1:
            print("Resultado: ", num1 + num2)
        elif eleccion == 2:
            print("Resultado: ", num1 - num2)
        elif eleccion == 3:
            print("Resultado: ", num1 * num2)
        elif eleccion == 4:
            print("Resultado: ", num1 / num2)
        elif eleccion == 5:
            print("Resultado: ", num1 ** num2)
        elif eleccion == 6:
            print("Resultado: ")

        calculadora_cientifica()

calculadora_cientifica()
