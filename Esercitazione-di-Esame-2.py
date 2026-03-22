class CSVTimeSeriesFile:
    
    def __init__(self,name):
        self.name_file=name
    
    def get_data(self):
        try:
            with open(self.name_file,'r') as file:
                next(file)
                lista=[]
                prev_time_stamp=None
                for line in file:
                 row=line.strip().split(',')
                 time_stamp=row[0]
                 if prev_time_stamp is not None:
                     if prev_time_stamp == time_stamp:
                         raise ExamException("Valore duplicato")
                     if prev_time_stamp > time_stamp:
                         raise ExamException("Valori non ordinati")
                        
                 prev_time_stamp=time_stamp
                 lista.append(row)
                return lista
        except:
            raise ExamException('Errore nell\'apertura del file')
    




def compute_variations(time_series,first_year,second_year):
    #if first_year not in time_series or second_year not in time_series:
     #   raise ExamException('Anno/i non presente nei dati')
    diz={}
    for element in time_series:
        data=element[0]
        #print('data=',data)
        parti=data.split('-')
        #print("parti=",parti)
        try:
            anno=int(parti[0])
        except:
            pass
        try:
            value=int(element[1])
        except: 
            print('valore non convertibile in intero')
            pass
        if anno >= int(first_year) and anno <= int(second_year):
            if anno not in diz:
                diz[anno]=[]
            diz[anno].append(value)
    for key in diz:
        diz[key] = sum(diz[key]) / len(diz[key])  
    diz_1={}
    anni=list(diz.keys())
    for i in range(1,len(anni)):
        chiave=f"{anni[i-1]}-{anni[i]}"
        valore=diz[anni[i]]-diz[anni[i-1]]
        diz_1[chiave]=valore                                                               
    return diz_1                                                
    
class ExamException(Exception):
    pass

time_series_file=CSVTimeSeriesFile(name='dati.csv')
time_series=time_series_file.get_data()
prov=compute_variations(time_series,"1950","1955")
print(prov)


