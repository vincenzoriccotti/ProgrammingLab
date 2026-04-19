



class ExamException(Exception):
    pass
class CSVTimeSeriesFile:
    
    def __init__(self, name):
        self.name=name
        try:
            with open (self.name, 'r') as file:
                pass
        except FileNotFoundError:
            raise ExamException("Errore: impossibile aprire il file")
        except :
            raise ExamException("il file è vuoto o non contiene dati validi")
        
    def get_data(self, country):
        lista=[]
        with open (self.name, 'r') as file:
            next(file)
            for line in file:
                line=line.strip().split(',')
                if len(line) < 3:
                    continue
                if line[2] == country:
                    
                    data=line[0]
                    value=line[1]
                    lista.append([data,value])
        if not lista:
           raise ExamException("il paese non è presente nel file")
                  
        return lista

def compute_variations(time_series_1, time_series_2, first_year, last_year):
    media_time_1=calcola_media(time_series_1,first_year,last_year)
    media_time_2=calcola_media(time_series_2,first_year,last_year)
    #print("Media anni Italia:",media_times_1)
    #print("Media anni Germania:",media_time_2)
    diz={}
    for key in media_time_2:
        diz[key]=media_time_2[key]-media_time_1[key]
    return diz
    
    
def calcola_media(time_series,first_year,last_year):
    diz={}
    for element in time_series:
        data=element[0].strip().split('-')
        anno=int(data[0])

        try:
            value = float(element[1])
        except:
            continue
        if first_year <= anno <= last_year:
            if anno not in diz:
                diz[anno]=[]
            diz[anno].append(value)
    for key in diz:
        diz[key]=(sum(diz[key])/len(diz[key]))
    return diz

time_series_file = CSVTimeSeriesFile(name="GlobalLandTemperaturesByCountry.csv")
time_series_italy = time_series_file.get_data(country="Italy")
time_series_germany = time_series_file.get_data(country="Germany")
compute_variations(time_series_italy, time_series_germany, 1843, 1855)
#print(time_series_italy)


