class Veicolo():
    
    def __init__(self,anno,modello,marca):
        self.modello = modello
        self.marca = marca
        self.anno=anno
        self.speed=0
    
    def __str__(self):
        return 'Marca della macchina: "{}" \nModello della macchina: "{}" \nAnno della macchina: "{}" \nVelocita  della macchina: "{}"'.format(self.marca,self.modello,self.anno,self.speed)
    
    def accelerare(self):
        self.speed+=5
    
    def frenare(self):
        if self.speed >= 5:
            self.speed-=5
    
    def get_speed(self):
        return self.speed

Audi=Veicolo('1987','A5 Sport','Audi')
Audi.accelerare()
Audi.accelerare()
Audi.accelerare()
Audi.accelerare()
Audi.frenare()
Audi.frenare()
print(Audi.get_speed())