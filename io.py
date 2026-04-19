

class ExamException(Exception):
    pass


class CSVTimeSeriesFile:
    
    def __init__(self,name):
        self.name=name
        try:
            file=open(self.name,'r')
        except:
            raise ExamException("Errore impossibile apire il file")
        contenuto=file.readlines()
        file.close()
        if len(contenuto)==0:
            raise ExamException("Errore: il file è vuoto o non contiene dati validi")
    
    def get_data(self,country):
        lista=[]
        file=open(self.name,'r')
        for line in file:
            line=line.strip().split(',')
            if line[0] != 'dt':
                if len(line)>2 and line[2] == country:
                    data=line[0]
                    try:
                        temp=float(line[1])
                    except:
                        continue
                    lista.append([data,temp])
        if len(lista)==0:
            raise ExamException("Errore: il nome del paese non è presente nel file")
        return lista


def calcola_media(time_series,first_year,last_year):
    diz={}
    for element in time_series:
        if len(element)>1:
            anno=int(element[0].split('-')[0])
            if first_year <= anno <= last_year:
                if anno not in diz.keys():
                    diz[anno]=[]
                diz[anno].append(element[1])
    diz={chiave: sum(valori)/len(valori) for chiave, valori in diz.items()}
    return diz

def compute_variations(time_series_1,time_series_2,first_year,last_year):
    if not isinstance(first_year,int) or not isinstance(last_year,int):
        raise ExamException("Errore: l'anno inserito non è un intero")
    media_1=calcola_media(time_series_1,first_year,last_year)
    media_2=calcola_media(time_series_2,first_year,last_year)
    print(media_1)
    print(media_2)
    anni=list(sorted(media_2.keys()))
    diz={}
    for i in range(len(anni)):
        chiave=anni[i]
        valore=media_2[chiave]-media_1[chiave]
        diz[chiave]=valore
    return diz









time_series_file = CSVTimeSeriesFile(name="GlobalLandTemperaturesByCountry.csv")
time_series_1= time_series_file.get_data(country="Italy")
time_series_2= time_series_file.get_data(country="Germany")
#c=compute_variations(time_series_1,time_series_2,1954,1959) 
time_serie_prova_1=[['1954-01-01', 10], ['1954-02-01', 12], ['1954-03-01', 15], ['1955-01-01', 20], ['1955-02-01', 22], ['1955-03-01', 25]]
time_serie_prova_2=[['1954-01-01', 5], ['1954-02-01', 7], ['1954-03-01', 10], ['1955-01-01', 15], ['1955-02-01', 17], ['1955-03-01', 20]]
d=compute_variations(time_serie_prova_1,time_serie_prova_2,1954,1955)
print(d)
 
