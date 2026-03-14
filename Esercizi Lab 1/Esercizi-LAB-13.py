def somma(file):
    totale=0
    my_file=open(file, 'r')
    next(my_file)
    for line in my_file:
        data, vendite=line.split(",")
        totale+=float(vendite)
    my_file.close()
    return totale


print(somma('shampoo_sales.txt'))