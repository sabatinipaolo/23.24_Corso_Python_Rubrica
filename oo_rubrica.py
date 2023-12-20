import csv 


class Rubrica:
    def __init__(self,nomeFile="rubrica.csv"):
        #TODO inserire controlli 
        self.nomeFile=nomeFile

        with open(self.nomeFile, 'r') as file:
            reader = csv.reader(file)
            self.lista = list(reader)
        

    def lista_contatti(self):
        return self.lista



class BrowserRubrica:
    def __init__(self,rubrica):
        #TODO inserire controlli 
        self.rubrica=rubrica
        self.comando={}
        self.comando["l"] = Comando_lista(rubrica)
        self.comando["L"] = self.comando["l"]
        self.comando["e"] = Comando_exit(rubrica)
        self.comando["E"] = self.comando["e"]


        # self.comando= { "l": Comando_lista(rubrica),
        #                 "e": Comando_exit(rubrica)
        #               }
        self.comando_lista = Comando_lista(rubrica)
        # self.comando_exit = Comando_exit(rubrica)


    def getComando(self):
        
        print(
            "\n[ L/l lista contatti] [ A/a aggiungi contatto ]  [ C/c cerca contatto ] [ R/r Rimuovi Contatto ] [ E/e Exit ]"
        )
        
        scelta = input("inserire commando: ")

        return self.comando[scelta]
        
        # if scelta in ("L", "l"):
        #     return self.comando_lista
        #     # return Comando_lista(self.rubrica)
        # elif scelta in ("A", "a"):
        #     return Comando_foo(self.rubrica)    
        # elif scelta in ("C", "c"):
        #     return Comando_foo(self.rubrica)  
        # elif scelta in ("R", "r"):
        #     return Comando_foo(self.rubrica)  
        # elif scelta in ("E", "e"):
        #     return Comando_exit(self.rubrica)  
        # else:
        #     print("comando no riconosciuto")
        #     return Comando_foo(self.rubrica)  
        
    



class Comando:
    def __init__(self,rubrica) -> None:
        self.rubrica = rubrica 
        self.is_exit = False

    def exec( self ):
        pass

    def isQuit():
        pass



class Comando_lista( Comando ):
    def __init__(self,rubrica) -> None:
        super().__init__(rubrica)


    def exec(self):
        print ( [x for x in self.rubrica.lista])


class Comando_exit( Comando ):
    def __init__(self,rubrica) -> None:
        super().__init__(rubrica)
        self.is_exit=True

    def exec(self):
        pass


class Comando_foo( Comando ):

    def exec(self):
        pass




