n = int(input("¿Cuántos términos deseas ver? "))

primero = 0
segundo = 1

for i in range(n):
    print(primero)
    suma = primero + segundo
    primero = segundo
    segundo = suma