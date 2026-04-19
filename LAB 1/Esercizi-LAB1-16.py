def duplicati(file):
    righe_uniche=[]
    with open(file,'r') as f:
       
        for parola in f:
            line=parola.strip()
            if line  not in righe_uniche:
                righe_uniche.append(line)
    with open("unique.txt",'w') as file1:
        for riga in righe_uniche:
            file1.write(riga + " ")

duplicati('nomi.txt')