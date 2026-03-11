
class Persona:
    def __init__(self,ruolo,nome,cognome):
        self.ruolo=ruolo
        self.nome=nome
        self.cognome=cognome
    
    def saluta(self):
        print('Ciao sono',self.ruolo + ",",self.nome, self.cognome)

class Studente(Persona):
    def __init__(self,nome,cognome,materie_studente):
        super().__init__("Studente UNITS",nome,cognome)
        self.materie_studente=materie_studente

    def saluta(self):
        Persona.saluta(self)
        print(">Frequentante dei corsi:",self.materie_studente)

class Docente(Persona):
    def __init__(self,nome,cognome,materie_docente):
        super().__init__("Docente UNITS",nome,cognome)
        self.materie_docente=materie_docente

    def controllo(self,studente):
        check=1 
        for elements in studente.materie_studente: 
         if elements not in self.materie_docente: 
               check=0
               break 
       
        if check:
            print("Insegna tutti i corsi frequentati da questo studente")
        else:
            print("Non insegna tutti i corsi frequentati da questo studente")
        
    def saluta(self):
        Persona.saluta(self)
        print(">Docente dei corsi:",self.materie_docente)


materie_studente=["Analisi I","Psicopatologia","Programmazione","Algebra Lineare","Analisi dei Dati"]
materie_docente=["Analisi II","Sistemi Operativi","Laboratorio 1","Psicopatologia","Analisi dei Dati","Calcolo delle probabilita"]





Prof=Docente('Carmen','Trumello',materie_docente)
Students=Studente('Arianna','Liuzzo',materie_studente)


Students.saluta()
print("---------------")
Prof.saluta()
print("---------------")
Prof.controllo(Students)