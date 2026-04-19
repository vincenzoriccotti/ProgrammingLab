


class CSVTimeSeriesFile:
    
    def __init__(self,name):
        self.name=name
    
    def get_data(self):
        lista=[]
        with open(self.name,'r') as file:
            next(file)
            for line in file:
                line=line.strip().split(',')
                data=line[0]
                value=line[1]
                lista.append([data,value])
        return lista
    
def compute_variations(time_series, first_year, last_year, N):
    diz={}
    for element in time_series:
        anno=int(element[0].split('/')[0])
        if first_year <= anno <= last_year:
            if anno not in diz.keys():
                diz[anno]=[]
            diz[anno].append(float(element[1]))
    diz={anno:sum(valori)/len(valori) for anno,valori in diz.items()}
    lista_anni=sorted(diz.keys())
    lista_valori=[diz[anno] for anno in sorted(diz)]
    diz_1={}
    for i in range(N,len(lista_anni)):
        media_mobile=sum(lista_valori[i-N:i])/N
        anno_corrente=lista_anni[i]
        diff=diz[anno_corrente] - media_mobile
        diz_1[anno_corrente]=diff
       
    return diz_1
    






time_series_file = CSVTimeSeriesFile(name='GlobalTemperatures.csv')
time_series = time_series_file.get_data()
c=compute_variations(time_series, 1999, 2006, 3)
print(c)
