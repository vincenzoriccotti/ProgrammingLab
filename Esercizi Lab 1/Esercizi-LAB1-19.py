class Veicolo():
    
    def __init__(self,anno,modello,marca):
        self.modello = modello
        self.marca = marca
        self.anno=anno
        self.speed=0
    
    def __str__(self):
        return 'Marca della veicolo: "{}" \nModello della veicolo: "{}" \nAnno del veicolo: "{}" \nVelocita  del veicolo: "{}"'.format(self.marca,self.modello,self.anno,self.speed)
    
    def accelerare(self):
        self.speed+=5
    
    def frenare(self):
        if self.speed >= 5:
            self.speed-=5
    
    def get_speed(self):
        return self.speed

class Auto(Veicolo):
    
    def __init__(self,anno,modello,marca,numero_porte):
        super().__init__(anno,modello,marca)
        self.numero_porte=numero_porte
    
    def __str__(self):
        return Veicolo.__str__(self) + "\nNumero di porte: {}".format(self.numero_porte)
       

class Moto(Veicolo):
    
    def __init__(self,anno,modello,marca,tipo):
        super().__init__(anno,modello,marca)
        self.tipo=tipo

    def __str__(self):
       return Veicolo.__str__(self) + "\nTipo di moto:{}".format(self.tipo)
      
    

Audi=Auto('1987','A5 Sport','Audi','4')
Ducati=Moto('2014','Monster','Ducati','Sport')

print(Audi)
print('-------------------')
print(Ducati)

