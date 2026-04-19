




class CSVTimeSeriesFile:
    
    def __init__(self,name):
        self.name=name
    
    def get_data(self):
        lista=[]
        file=open(self.name,'r')
        for line in file:
            
            line=line.strip().split(",")
            if line[0] != "dt":
                data=line[0]
                temp=line[1]
                lista.append([data,temp])
        return lista



def compute_variations(time_series,first_year,last_year,N):
    
    diz={}
    for element in time_series:
        data=element[0].split('/')
        anno=int(data[0])
        if first_year <= anno <= last_year:
            if anno not in diz.keys():
                diz[anno]=[]
            diz[anno].append(element[1])
    for anni in diz.keys():
        somma=sum(diz[anni])
        lunghezza=len(diz[anni])
        media=somma/lunghezza
        diz[anni].append(media)
    sorted_anni=sorted(diz.keys())
    risultati={}
    for i in range(len(sorted_anni)):
        anno=sorted_anni[i]
        if i >=N:
            anni=sorted_anni[i-N:i]
            media_mobile=sum(diz[y] for y in anni) /N
            diff = diz[anno] - media_mobile
            risultati[anno]=diff
    return risultati


time_series_file = CSVTimeSeriesFile(name='GlobalTemperatures.csv')
time_series = time_series_file.get_data()
c=compute_variations(time_series,1850,1857,3)
print(c)

    
    
    