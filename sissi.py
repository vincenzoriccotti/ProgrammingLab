





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
    for element in time_series: #[[1958-03,123],[1959-04,456]]
        anno=int(element[0].split('-')[0]) 
        if first_year <= anno <= last_year:
            if anno not in diz.keys():
                diz[anno]=[]
            diz[anno].append(int(element[1]))
    
    for key in diz.keys():
        somma=sum(diz[key])
        lunghezza=len(diz[key])
        media=somma/lunghezza
        diz[key]=media
    diz_1={}
    anni=list(diz.keys())
    for i in range(1,len(anni)):
            chiave=f"{anni[i-1]}-{anni[i]}"
            valore=diz[anni[i]]-diz[anni[i-1]]
            diz_1[chiave]=valore                                                               
    return diz_1  
    
    
            

time_series_file = CSVTimeSeriesFile(name='dati.csv')
time_series = time_series_file.get_data()
#print(time_series)
c=compute_variations(time_series,1949,1952)
print(c)






















