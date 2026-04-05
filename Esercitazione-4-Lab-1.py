class ExamException(Exception):
    pass


class CSVTimeSeriesFile:
    
    def __init__(self,name):
        self.name=name
    
    def get_data(self,city):
        
        lista=[]
        try:
            with open(self.name,'r') as file:
                next(file)
                for line in file:
                    line=line.strip().split(',')
                    if len(line)>2:
                        citta=line[2]
                        if citta == city:
                            try:
                                temp=float(line[1])
                                data=line[0]
                                lista.append([data,temp])
                            except:
                                continue
            if len(lista) == 0:
                raise ExamException("Errore: il nome della città non è presente nel file")
            return lista
        except FileNotFoundError:
            raise ExamException("Il file selezionato non esiste")


def compute_slope(time_series,first_year,last_year):
    diz={}
    for lista in time_series:
        anno=int(lista[0].strip().split('-')[0])
        if first_year <= anno <= last_year:
            if anno not in diz.keys():
                diz[anno]=[]
            diz[anno].append(lista[1])
    if len(diz) ==0:
        raise ExamException("Intervallo di anni vuoto o non valido")
    diz_1={}
    for anni in diz.keys():
        if len(diz[anni]) >=6:
            diz_1[anni]=sum(diz[anni])/len(diz[anni])
    media_x=sum(diz_1.keys())/len(diz_1)
    media_y=sum(diz_1.values())/len(diz_1)
    numeratore=0
    denominatore=0
    for chiave,valore in diz_1.items():
        numeratore+=(chiave-media_x)*(valore-media_y)
        denominatore+=(chiave-media_x)**2
    if denominatore !=0:
        m=numeratore/denominatore
    else:
        raise ExamException("Denominatore uguale a zero, operazione non possibile")
    return m
    
    

time_series_file = CSVTimeSeriesFile(name="GlobalLandTemperaturesByCountry.csv")
time_series_italy = time_series_file.get_data(city="Italy")
c=compute_slope(time_series_italy,1990,1996)
print(c)