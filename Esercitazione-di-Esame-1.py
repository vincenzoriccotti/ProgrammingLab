

class MovingAverage:
    
    def __init__(self,window):
        if type(window) != int or window<0:
            raise ExamException('Valore inserito non valido')
        self.window=window
    
    def compute(self,lista):
       
        if type(lista) != list or not all(isinstance(element,int) for element in lista ):
            raise ExamException("Lista non valida")
        
        if len(lista) < self.window:
            raise ExamException("La lista contiene meno elementi della finestra")
        lista_new=[]
        for i in range(0,len(lista)-self.window+1):
            element=0
            for j in range(i,i+self.window):
                element+=lista[j]
            lista_new.append(element/self.window)
        return lista_new
      
    #v.2 (list comprehension)
    def compute_2(self,lista):
        return[sum(lista[i:i+self.window])/self.window 
                for i in range(0,len(lista)-self.window+1)]
        

class ExamException(Exception):
    pass

moving_average=MovingAverage(2)
result=moving_average.compute([2,4,8,16])
print(result)


