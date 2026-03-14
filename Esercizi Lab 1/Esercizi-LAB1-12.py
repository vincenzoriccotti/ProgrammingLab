def dizconta(lista):
    my_diz={}
    for elementi in lista:
        if elementi in my_diz:
            my_diz[elementi]+=1
        else:
            my_diz[elementi]=1
    return my_diz

        

lista=["cane","gatto","leone","lupo","cane","leone","elefante"]
print(dizconta(lista))