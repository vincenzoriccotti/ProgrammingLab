

class CSVTimeSeriesFile:
    def __init__(self,name):
        self.name_file=name
    def get_data(self):
        lista=[]
        with open(self.name_file,'r') as file:
            for line in file:
                element=line.strip().split(',')
                lista.append(element)
        return lista

def compute_variations(time_series,first_year,last_year,N):
    temperatures_per_year={}
    for element in time_series[1:]:
        data=element[0]
        tmp=float(element[1])
        anno=int(data.split('/')[0])
        if anno not in temperatures_per_year:
            temperatures_per_year[anno]=[]
        temperatures_per_year[anno].append(tmp)
    yearly_average={}
    for anno, temps in temperatures_per_year.items():
        yearly_average[anno]=sum(temps)/len(temps)
    result={}
    for year in range(first_year,last_year+1):
        previous_years=list(range(year-N,year))
        moving_average=sum(yearly_average[y] for y in previous_years)/N
        difference=yearly_average[year]- moving_average
        result [str(year)]=difference
    return result
        
    
    






time_series_file = CSVTimeSeriesFile(name='GlobalTemperatures.csv')
time_series = time_series_file.get_data()
prova=compute_variations(time_series, 1904, 1998, 3)
print(prova)