

class CSVTimeSeriesFile:
    
    def __init__(self,name):
        self.name=name
        
    def get_data(self):
        lista=[]
        try:
            with open(self.name,'r') as file:
                next(file)
                for line in file:
                    row=line.strip().split(',')
                    try:
                        value=int(row[1])
                    except ValueError:
                        print('valore non convertibile in intero')
                        continue
                    
                    lista.append(row)
            return lista
        except FileNotFoundError:
            raise ExamException('Errore nell\'apertura del file')

def compute_variations(time_series,first_year,last_year):
    first_year=int(first_year)
    last_year=int(last_year)
    dict={}
    for element in time_series:
        data=element[0].split('-')
        anno=int(data[0])
        value=int(element[1])
        if first_year <=  anno <= last_year:
            if anno not in dict:
                dict[anno]=[]
            dict[anno].append(value)
    for key in dict:
        somma=sum(dict[key])
        media=somma/len(dict[key])
        dict[key]=media
    dict_1={}
    anni=list(dict.keys())
    for i in range(1,len(anni)):
        chiave=f"{anni[i-1]}-{anni[i]}"
        dict_1[chiave]=dict[anni[i]]-dict[anni[i-1]]
    return dict_1
    
class ExamException(Exception):
    pass

time_series_file = CSVTimeSeriesFile(name='dati.csv')
time_series = time_series_file.get_data()
bho=compute_variations(time_series,"1952","1957")
print(bho)