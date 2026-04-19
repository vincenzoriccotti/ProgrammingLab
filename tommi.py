





class CSVTimeSeriesFile:
    
    def __init__(self,name):
        self.name=name
    
    def get_data(self):
        lista=[]
        file=open(self.name,'r')
        for line in file:
            line=line.strip().split(',')
            if line[0] != 'date':
                data=line[0]
                passengers=line[1]
                lista.append([data,passengers])
        return lista
    
    def compute_variations(time_series,first_year,last_year):
        diz={}
        for element in time_series:
            anno=int(element[0].split('-')[0]) 
            print(element, type(element[0]))
            if first_year <= anno <= last_year:
                if anno not in diz.keys():
                    diz[anno]=[]
                diz[anno].append(element[1])
        #diz={chiave: sum(valore)/len(valore) for chiave,valore in diz.items()}
        return diz
            

time_series_file = CSVTimeSeriesFile(name='dati.csv')
time_series = time_series_file.get_data()
#print(time_series)
#c=compute_variations(time_series,1952,1959)
#nt(c)














time_series_file = CSVTimeSeriesFile(name='dati.csv')
time_series = time_series_file.get_data()
print(time_series)













