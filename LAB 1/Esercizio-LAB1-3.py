def quadrato(numero, n=2):
    return numero ** n

def cubo(numero, n=3):
    return numero ** n

numero=float(input("Inserisci un numero: "))

print(quadrato(numero,n=2))
print(cubo(numero, n=3))