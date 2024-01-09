import csv
import gc


class Rubrica:
    def __init__(self, nomeFile="rubrica.csv"):
        # TODO inserire controlli
        self.nomeFile = nomeFile

        with open(self.nomeFile, "r") as file:
            reader = csv.reader(file)
            self.lista = list(reader)

    def salva(self, nomeFile ):
        with open(nomeFile, "w") as file:
            wr = csv.writer(file)
            wr.writerows(self.lista)



class BrowserRubrica:
    def __init__(self, rubrica):
        # TODO inserire controlli
        self.rubrica = rubrica
        # self.comando = {}
        # self.comando["l"] = Comando_lista(rubrica)
        # self.comando["L"] = self.comando["l"]
        # self.comando["e"] = Comando_exit(rubrica)
        # self.comando["E"] = self.comando["e"]

        # self.comando= { "l": Comando_lista(rubrica),
        #                 "e": Comando_exit(rubrica)
        #               }
        self.comando_lista = Comando_lista(rubrica)
        # self.comando_exit = Comando_exit(rubrica)

    def getComando(self):
        print(
            "\n[ L/l lista contatti] [ A/a aggiungi contatto ]  [ C/c cerca contatto ] [ R/r Rimuovi Contatto ] [S/s Salva ] [ E/e Exit ]"
        )

        scelta = input("inserire comando: ")

        # return self.comando[scelta]

        if scelta in "Ll":
            # return self.comando_lista
            return self.comando_lista
        elif scelta in "Aa":
            return Comando_aggiungi(self.rubrica)
        elif scelta in "Cc":
            return Comando_foo(self.rubrica)
        elif scelta in "Rr":
            return Comando_foo(self.rubrica)
        elif scelta in "Ee":
            return Comando_exit(self.rubrica)
        elif scelta in "Ss":
            return Comando_salva(self.rubrica)
        else:
            return Comando_non_riconosciuto(self.rubrica)


class Comando:
    def __init__(self, rubrica) -> None:
        self.rubrica = rubrica
        self.is_exit = False

    def exec(self):
        pass

    def isQuit():
        pass


class Comando_lista(Comando):
    def __init__(self, rubrica) -> None:
        super().__init__(rubrica)

    def exec(self):
        for riga in self.rubrica.lista :
            print ( ' ,'.join( riga))
       # print([x for x in self.rubrica.lista])
            

class Comando_aggiungi(Comando):
    def __init__(self, rubrica) -> None:
        super().__init__(rubrica)

    def exec(self):
        for riga in self.rubrica.lista :
            print ( ' ,'.join( riga))
       # print([x for x in self.rubrica.lista])
            






class Comando_salva(Comando):
    def __init__(self, rubrica) -> None:
        super().__init__(rubrica)
        
    def exec(self):
        nomeFile = input(f"nome con cui salvare [{self.rubrica.nomeFile}")
        if nomeFile=="" : 
              self.rubrica.salva( self.rubrica.nomeFile)
        else: self.rubrica.salva( nomeFile )



        
class Comando_non_riconosciuto(Comando):
    def __init__(self, rubrica) -> None:
        super().__init__(rubrica)
        
    def exec(self):
        print("comando non riconosciuto")

class Comando_exit(Comando):
    def __init__(self, rubrica) -> None:
        super().__init__(rubrica)
        self.is_exit = True

    def exec(self):
        pass
class Comando_foo(Comando):
    def __init__(self, rubrica) -> None:
        super().__init__(rubrica)
        
    def exec(self):
        pass


