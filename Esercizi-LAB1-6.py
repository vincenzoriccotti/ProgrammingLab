def somman():
     i=int(input("Inserisci un numero (0 per terminare): ")  )
     somma=0
     while(i !=0):
        somma+=i
        i=int(input("Inserisci un numero (0 per terminare): ")  )
       
     return somma    


print("La somma dei numeri e': ",somman())
