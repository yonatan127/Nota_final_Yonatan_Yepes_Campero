filas = int(input("¿Cuántas filas quieres? : "))

for i in range(1, filas + 1):
    for j in range(1, i + 1):
     #el end hace que los números se queden en la misma fila
        print(j, end=" ")
        #por si algo esto es un salto de linea
    print()