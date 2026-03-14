def fattoriale(numero):
    if(numero==0 | numero==1):
        return 1
    else:
        for i in range(numero-1, 0,-1):
            numero*=i

    
    return numero
    

print(fattoriale(5))