class CsvFile:
    
    def __init__(self,name_file):
        self.name_file=name_file

    def get_data(self):
        lista=[]
        with open(self.name_file, 'r') as file:
            for line in file:
                elements = line.split(',')
                lista.append(elements)
        return lista
