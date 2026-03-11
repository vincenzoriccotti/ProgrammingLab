#ESERCIZIO 3
def paridispari(numero):
    if(numero % 2 == 0):
        return "Il numero è pari"
    else:
        return "Il numero è dispari"

    
numero=int(input("Inserisci un numero: "))

print(paridispari(numero))

