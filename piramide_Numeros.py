filas = int(input("¿Cuántas filas quieres? "))

for i in range(1, filas + 1):
    # Empezamos con la fila vacía (como una hoja en blanco)
    fila_actual = ""

    # Este ciclo mete los números uno por uno en la "hoja"
    for j in range(1, i + 1):
        # Convertimos el número a texto y le sumamos un espacio
        fila_actual = fila_actual + str(j) + " "

    # Cuando la fila ya tiene todos los números, la imprimimos
    print(fila_actual)