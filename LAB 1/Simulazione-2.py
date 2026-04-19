


class CSVTimeSeriesFile:
    def __init__(self,name):
        self.name_file=name
        try:
            with open(self.name_file,'r') as file:
                pass
        except Exception:
            raise ExamException("Errore: impossibile aprire il file.")
    def get_data(self):
        
        with open(self.name_file,'r') as file:
            lista=[]
            #Salto l'intestazione
            next(file)
            for row in file:
                element=row.strip().split(',')
                data=element[0]
                temp=float(element[1])
                uncert=float(element[2])
                if uncert <5:
                    lista.append([data,temp])
                else:
                    print("Data saltata perchè valore troppo incerto")
        return lista
    
class ExamException(Exception):
    pass
    
def compute_month_variation(time_series,first_year,second_year):
    if type(first_year) != int or type(second_year) != int:
        raise ExamException("Errore: gli anni devono essere dit tipo intero.")
    if first_year >= second_year:
        raise ExamException("Errore: il secondo anno deve essere maggiore del primo.")
    
    year_temp={}
    for element in time_series:
        date=element[0]
        temp=element[1]
        anno=int(date.split('/')[2])
        mese=int(date.split('/')[1])
        if anno==first_year or anno==second_year:
            if anno not in year_temp:
                year_temp[anno]={}
            year_temp[anno][mese]=temp
    variations={}
    count=0
    for month in range(1,13):
        if month in year_temp[first_year] and month in year_temp[second_year]:
            diff=year_temp[second_year][month] - year_temp[first_year][month]
            variations[month]=diff
        else:
            print(f"La variazione per il mese {month} non calcolata perchè dati mancanti.")
            count+=1
    if count==12:
        raise ExamException("Gli anni considerati non hanno mesi validi.")
    return variations
    
    
   
time_series_file = CSVTimeSeriesFile(name="GloblTemperatures.csv")
data = time_series_file.get_data()
variazioni=compute_month_variation(data,1998,2001)
print(variazioni)