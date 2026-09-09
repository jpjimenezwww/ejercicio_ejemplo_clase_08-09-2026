
def pedir_positivo():
    numero = int(input("Ingrese un número: "))
    while numero <= 0:
        numero = int(input("Inválido. Ingrese uno mayor que 0: "))
    return numero

n = pedir_positivo()
print("Número válido:", n)