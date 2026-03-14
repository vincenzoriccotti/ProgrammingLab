def conteggio(file):
    my_diz={}
    with open(file,'r') as file:
        for line in file:
            parola=line.strip()
            if parola in my_diz:
                my_diz[parola]+=1
            else:
                my_diz[parola]=1
    return my_diz

print(conteggio('nomi.txt'))