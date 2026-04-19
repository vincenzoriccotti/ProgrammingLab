
class ExamException(Exception):
    pass


class CSVTimeSeriesFile:
    
    def __init__(self,name):
        self.name=name
        try:
            f=open(self.name,'r')
        except FileNotFoundError:
            raise ExamException('File inesistente o non leggibile')
        else:
            f.close()

    def get_data(self):
        
        file=open(self.name,'r')
        lista=[]
        for line in file:
            line=line.strip().split(',')
           
            if line[0] != 'dt':
                data=line[0]
                if line[1] == '':
                    continue
                try:
                    temp=float(line[1])
                except ExamException:
                    continue
                  
                if temp < 0:
                    continue
                    
                lista.append([data,temp])
        file.close()
        return lista


def compute_variations(time_series, first_year, last_year, N):
    
    if not isinstance(first_year,str) or not isinstance(last_year,str):
        raise ExamException("first_year e last_year devono essere stringhe")
    first_year=int(first_year)
    last_year=int(last_year)
    diz={}
    for element in time_series:
        anno=int(element[0].split('/')[0])
        if first_year <= anno <= last_year:
            if anno not in diz.keys():
                diz[anno]=[]
            diz[anno].append(float(element[1]))
    diz={chiave: sum(x for x in diz[chiave])/len(diz[chiave]) for chiave in diz}
    lista_anni=list(sorted(diz.keys()))
    
    if N >= len(lista_anni):
        raise ExamException("N non valido")
    diz_1={}
    for i in range(N,len(lista_anni)):
        anno=(lista_anni[i])
        media_mobile=sum(diz[lista_anni[j]] for j in range(i-N,i))/N
        diff=diz[anno]-media_mobile
        diz_1[anno]=diff
    return diz_1
    
    
def temperatura(time_series,first,last):
    
    lista=[]
    for element in time_series:
        anno=element[0].strip().split('/')[0]
        temp=element[1]
        if not(first <= temp <= last):
            if anno not in lista:
                lista.append(anno)
    return lista
            

time_series_file = CSVTimeSeriesFile(name='GlobalTemperatures.csv')
time_series = time_series_file.get_data()
c=compute_variations(time_series, "1910", "1916", 3)
d=temperatura(time_series,0,15)
print(c)
#print(d)
