
class ExamException(Exception):
    pass


class CSVTimeSeriesFile:
    
    def __init__(self,name):
        self.name=name
    
    def get_data(self):
        lista=[]
        try:
            file=open(self.name,'r')
        except:
            raise ExamException("File inesistente o non apribile")
        for line in file:
            line=line.strip().split(',') 
            if line[0] != 'date': 
                try:
                    data=line[0] 
                    passengers=int(line[1]) 
                    lista.append([data,passengers])
                except:
                    print("Valore ignorato")
                    continue            
        file.close()
        return lista

# Posso scrivere la funzione compute_variations fuori
# dalla classe CSVTimeSeriesFile,in quanto non è un 
# metodo della classe, ma una funzione a sé stante 
# che prende in input una serie temporale e restituisce 
# un dizionario con le variazioni percentuali tra gli anni specificati.                    
def compute_variations(time_series,first_year,last_year):
    diz={}
    for element in time_series:
        anno=int(element[0].split('-')[0])
        if first_year <= anno <= last_year:
            diz.setdefault(anno,[]).append(element[1])
    diz = {key: sum(values)/len(values) for key, values in diz.items()}
    diz_1={}
    lista_anni=list(sorted(diz.keys()))
    for a,b in zip(lista_anni,lista_anni[1:]):
        diz_1[f"{a}-{b}"]=diz[b]-diz[a]
    return diz_1
            
            
    

time_series_file = CSVTimeSeriesFile(name='dati.csv')
time_series = time_series_file.get_data()
c=compute_variations(time_series,1952,1959)
#print(c)
