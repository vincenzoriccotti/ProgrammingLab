

class CSVTimeSeriesFile:
    def __init__(self,name):
        self.name_file=name
    

    def get_data(self, country):
        lista = []

        with open(self.name_file, 'r') as file:
            next(file)  # salta intestazione

            for row in file:
                element = row.strip().split(',')

                if len(element) < 3:
                    continue

                data = element[0]
                temp = element[1]
                paese = element[2]

                if temp == '':
                    continue

                if paese == country:
                    lista.append([data, float(temp)])

        return lista

time_series_file = CSVTimeSeriesFile(name="GlobalLandTemperaturesByCountry.csv")
time_series_italy = time_series_file.get_data(country="Italy")
print(time_series_italy)              