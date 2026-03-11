
def somma(file,parola):
    with open(file,'r') as file:
        tot=0
        for line in file:
            if parola in line:
                tot+=1
    return tot
    

print(somma('shampoo_sales.txt','Sales')) 
