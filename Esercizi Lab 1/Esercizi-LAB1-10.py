def scambia(lista):
    print("Inserisci due indici A,J compresi tra 0 e",len(lista)-1)
    x=int(input("Indice I: "))
    y=int(input("Indice J: "))
    lista[x],lista[y]=lista[y],lista[x]
    print("Lista dopo lo scambio:",lista)

scambia(lista=["cane", "gatto", "volpe","scoiattolo"])