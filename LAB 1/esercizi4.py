
class ExamException(Exception):
    pass


class MovingAverage:
    
    def __init__(self,len_window):
        try:
            len_window=int(len_window)
        except ValueError:
            raise ExamException("Valore non intero")
        if len_window <=0:
            raise ExamException("Valore minore o uguale di zero")
        else:
            self.len_window=len_window
            
    
    def compute(self,lista):
        if len(lista) < self.len_window:
            raise ExamException("Lunghezza finestra non valida")
        if not isinstance(lista,list):
            raise ExamException("Non è una lista")
        for x in lista:
            if not isinstance(x,(int,float)):
                raise ExamException("Non sono tutti numeri")
        lista_new=[]
        for i in range(0,len(lista)-self.len_window+1):
            somma=0
            for j in range(0,self.len_window):
                somma+=lista[j+i]
            media=somma/self.len_window
            lista_new.append(media)
        return lista_new
        
moving_average = MovingAverage(2)
result = moving_average.compute([2,4,8,16])
print(result) # Deve stampare [3.0, 6.0, 12.0]