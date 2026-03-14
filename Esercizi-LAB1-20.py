class CsvFile:
    
    def __init__(self,name_file):
        self.name_file=name_file

    def get_data(self):
        lista=[]
        try:
            with open(self.name_file, 'r') as file:
                for line in file:
                    elements = line.strip().split(',')
                    lista.append(elements)
                return lista
        except FileNotFoundError:
        
            print("Stai cercando di aprire un file che non esiste")
            


class NumericalCSVFile(CsvFile):
    
    def __init__(self,name_file):
        super().__init__(name_file)
    
    def get_data(self):
        data=super().get_data()
        data_float=[]

        for row in data[1:]:
            new_row=[row[0]]
            for element in row[1:]:
                try:
                    new_row.append(float(element))
                except ValueError:
                    print(f"Non è possibile convertire '{element}'in un float")
                    continue
            data_float.append(new_row)
            
        return data_float
        



file = NumericalCSVFile("/Data/dati.csv")
#file1=CsvFile("dato.csv")
print(file.get_data())
#print(file1.get_data())
