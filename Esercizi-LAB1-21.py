class CsvFile:
    
    def __init__(self,name_file):
        if isinstance(name_file, str):
            self.name_file=name_file
        else:
            raise TypeError("Il nome del file deve essere una stringa")

    def get_data(self,start=None, end=None):
        lista=[]
        try:
            with open(self.name_file, 'r') as file:
                for line in file:
                    elements = line.strip().split(',')
                    lista.append(elements)     
        except FileNotFoundError:
    
            print("Stai cercando di aprire un file che non esiste")

        if not isinstance(start, int) and not isinstance(end, int):
            raise TypeError("I valori di start e end devono essere interi")
        else:    
            if start < 1 or end > len(lista):
                print("I valori di start e end non rispettano l'intervallo della lista")
                print("Input non valido, seleziono tutta la lista")
                start=1
                end=len(lista)
            if start >= end:
                print("Il valore di start deve essere minore di end")
                print("Input non valido, seleziono tutta la lista")
                start=1
                end=len(lista)
            
        return lista[start -1:end] 
        
 
            
class NumericalCSVFile(CsvFile):
    
    def __init__(self,name_file):
        super().__init__(name_file)
    
    def get_data(self):
        data=super().get_data()
        if data is None:
            return None
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
        
        

file = NumericalCSVFile("dati.csv")
file1=CsvFile("dati.csv")
#print(file.get_data())
print(file1.get_data(3,12))
