


class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    
    def __init__(self,name):
        self.name=name
    
    def get_data(self):
        try:
            with open(self.name,'r') as file:
                next(file)
                lista=[]
                for line in file:
                    data,passengers=line.strip().split(',')
                    try:
                        lista.append([data,int(passengers)])
                    except ValueError:
                        print(f"Impossibile convertire'{passengers}'in un intero")
                        continue
            return lista
        except FileNotFoundError as e:
            raise ExamException("Impossibile aprire il file")

def compute_variations(time_series,first_year,last_year):
    
    diz={}
    for element in time_series:
        anno=int(element[0].split('-')[0])
        if first_year <= anno <= last_year:
            if anno not in diz.keys():
                diz[anno]=[]
            diz[anno].append(int(element[1]))
    diz={ key: sum(diz[key])/len(diz[key]) for key in diz.keys()}
    diz_1={}
    lista_anni=list(diz.keys())
    lista_valori=list(diz.values())
    for i in range(1,len(lista_anni)):
        chiave=f"{lista_anni[i-1]}- {lista_anni[i]}"
        valore=lista_valori[i]-lista_valori[i-1]
        diz_1[chiave]=valore
    return diz_1
    
time_series_file = CSVTimeSeriesFile(name='dati.csv')
time_series = time_series_file.get_data()
c=compute_variations(time_series, 1955, 1959)
print(c)
    
        
            
        
