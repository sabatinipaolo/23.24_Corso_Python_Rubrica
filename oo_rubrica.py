import csv
from itertools import zip_longest


class Rubrica:
    def __init__(self, nomeFile="rubrica.csv"):
        # TODO inserire controlli
        self.nomeFile = nomeFile
        self.modificata = False

        with open(self.nomeFile, "r") as file:
            reader = csv.reader(file)
            self.lista = list(reader)

    def salva(self, nomeFile):
        if nomeFile == "":
            nomeFile = self.nomeFile
        with open(nomeFile, "w") as file:
            wr = csv.writer(file)
            wr.writerows(self.lista)
        self.modificata = False

    def aggiunge_contatto(self, contatto):
        self.lista.append(contatto)
        self.modificata = True

    def ricerca_contatti(self, stringaRicerca):
        contattiRicercati = []
        for riga in self.lista:
            if any(stringaRicerca in s for s in riga):
                contattiRicercati.append(riga)
        return contattiRicercati

    def rimuove_contatti(self, contatti_da_rimuovere):
        self.lista = [x for x in self.lista if x not in contatti_da_rimuovere]
        self.modificata = True


class BrowserRubrica:
    def __init__(self, rubrica):
        # TODO: inserire controlli per validazione del file
        self.rubrica = rubrica

        self.comando_lista = Comando_stampa_completa(rubrica)

    def getComando(self):
        print(
            f"\nrubrica: { self.rubrica.nomeFile} \n"
            + "[ L/l lista contatti    ] [ LG/lg lista per gruppi ] [ C/c cerca contatto/i ]\n"
            + "[ CC/cc cerca contatto x colonne] \n"            
            + "[ A/a aggiungi contatto ] [ R/r Rimuovi Contatto   ] [ S/s Salva            ] [ E/Q/e/q Exit ]"
        )

        scelta = input("inserire comando: ")

        if scelta in "Ll":
            return Comando_stampa_completa(self.rubrica)
        elif scelta in ("LG", "lg", "Lg", "lG"):
            return Comando_stampa_a_gruppi(self.rubrica)
        elif scelta in "Aa":
            return Comando_aggiungi(self.rubrica)
        elif scelta in ("C","c"):
            return Comando_cerca_contatti(self.rubrica)
        elif scelta in ("CC","cc"):
            return Comando_cerca_contatti_per_colonne(self.rubrica)
        
        elif scelta in "Rr":
            return Comando_rimuovi(self.rubrica)
        elif scelta in "EeQq":
            return Comando_exit(self.rubrica)
        elif scelta in "Ss":
            return Comando_salva(self.rubrica)
        else:
            return Comando_non_riconosciuto(self.rubrica)


class Comando:
    lastRicerca = ""
    lastDimensioneGruppo = ""

    lastRicercaPerColonne = ("","","","","")

    def aggiorna_last_ricerca(classe, stringa):
        Comando.lastRicerca = stringa

    def __init__(self, rubrica) -> None:
        self.rubrica = rubrica
        self.is_exit = False

    def stampa_contatti(self, contatti):
        print("\n")
        for riga in contatti:
            if riga is not None:
                # print ( ' ,'.join( riga))
                print(*riga, sep=", ")

    def seleziona_contatti(self, messaggio, stringaDaRicercare):
        pass

    def input_con_msg_default_valori_ammessi(
        self, messaggio, default, valoriAmmessi=""
    ):
        risposta = input(f"{messaggio} {valoriAmmessi} [{default}] =")
        risposta = default if risposta == "" else risposta
        if valoriAmmessi == "":
            return risposta
        while risposta not in valoriAmmessi:
            print("risposta non ammessa")
            risposta = input(f"{messaggio} {valoriAmmessi} [{default}] =")
            risposta = default if risposta == "" else risposta

        return risposta

    def exec(self):
        pass


class Comando_stampa_completa(Comando):
    def __init__(self, rubrica) -> None:
        super().__init__(rubrica)

    def exec(self):
        self.stampa_contatti(self.rubrica.lista)


class Comando_stampa_a_gruppi(Comando):
    def __init__(self, rubrica) -> None:
        super().__init__(rubrica)
        # self.dimensioneGruppo = dimensioneGruppo

    def exec(self):
        # TODO: modificare input_con_messa.... in modo che passi una funzione
        # che determini se il valore inserito verifichi se sia ammesso

        dimensione = self.input_con_msg_default_valori_ammessi(
            "inserisci la dimensione del gruppo", "5", ""
        )
        # TODO: inserire controlli  vedi sopra
        dimensione = int(dimensione)
        self.lastDimensioneGruppo = dimensione

        # https://realpython.com/python-itertools/
        args = [iter(self.rubrica.lista)] * dimensione
        gruppi = zip_longest(*args, fillvalue=None)

        for gruppo in gruppi:
            print("\n---------------------------------------------- ")
            self.stampa_contatti(gruppo)

            risposta = self.input_con_msg_default_valori_ammessi(
                "\nancora ?", "s", ("s", "S", "n", "N")
            )
            if risposta in ("n", "N"):
                break

        print("\n stampa per gruppi completata")


class Comando_aggiungi(Comando):
    def __init__(self, rubrica) -> None:
        super().__init__(rubrica)

    def exec(self):
        # TODO: controllare se non inserisce virgole
        # TODO: inserire controlli (nomi alfabetici, m/f , telefoni numerici ...)
        nome = input("nome =")
        cognome = input("cognome=")
        sesso = input("sesso =")
        citta = input("città =")
        telefono = input("telefono =")

        contatto = [
            " ".join(nome.split()).strip(),
            " ".join(cognome.split()).strip(),
            " ".join(citta.split()).strip(),
            " ".join(sesso.split()).strip(),
            " ".join(telefono.split()).strip(),
        ]

        self.rubrica.aggiunge_contatto(contatto)


class Comando_cerca_contatti(Comando):
    def __init__(self, rubrica) -> None:
        super().__init__(rubrica)

    def exec(self):
        stringaDaRicercare = self.input_con_msg_default_valori_ammessi(
            "Inserisci stringa di ricerca per i contatti da visualizzare:",
            self.lastRicerca,
        )
        self.aggiorna_last_ricerca(stringaDaRicercare)

        contattiTrovati = self.rubrica.ricerca_contatti(stringaDaRicercare)

        if contattiTrovati:
            self.stampa_contatti(contattiTrovati)
        else:
            print("\n nulla da visualizzare \n")

class Comando_cerca_contatti_per_colonne(Comando):
    def __init__(self, rubrica) -> None:
        super().__init__(rubrica)

    def exec(self):

        return

class Comando_rimuovi(Comando):
    def __init__(self, rubrica) -> None:
        super().__init__(rubrica)

    def exec(self):
        stringaDaRicercare = self.input_con_msg_default_valori_ammessi(
            "Inserisci stringa di ricerca per i contatti da rimuovere:",
            self.lastRicerca,
        )
        self.aggiorna_last_ricerca(stringaDaRicercare)

        contattiDaRimuovere = self.rubrica.ricerca_contatti(stringaDaRicercare)
        if not contattiDaRimuovere:
            print("nulla da rimuovere")
        else:
            print("ATTENZIONE I SEGUENTI CONTATTI SOTTOELENCATI VERRANNO CANCELLATI")
            self.stampa_contatti(contattiDaRimuovere)
            print("ATTENZIONE I SOPRAELENCATI CONTATTI CONTATTI VERRANNO CANCELLATI")

            risposta = self.input_con_msg_default_valori_ammessi(
                "Sei sicuro di voler procedere? ", "N", ("s", "S", "n", "N", "tutti")
            )

            if risposta == "tutti":
                self.rubrica.rimuove_contatti(contattiDaRimuovere)
                print("contatti rimossi")
            elif risposta in ("s", "S"):
                for contatto in contattiDaRimuovere:
                    risposta = self.input_con_msg_default_valori_ammessi(
                        f"rimuovo il contatto { contatto } \n confermi?",
                        "n",
                        ("s", "S", "n", "N", "esci"),
                    )
                    if risposta == "esci":
                        return
                    if risposta in ("n", "N"):
                        continue
                    # risposta in ("s","S")
                    self.rubrica.rimuove_contatti(
                        [contatto]
                    )  # TODO vedi se è il caso di migliorare
                    print("contatto rimosso ")


class Comando_salva(Comando):
    def __init__(self, rubrica) -> None:
        super().__init__(rubrica)

    def exec(self):
        nomeFile = self.input_con_msg_default_valori_ammessi(
            "\n nome con cui salvare ", self.rubrica.nomeFile, ""
        )
        self.rubrica.salva(nomeFile)


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
        if not self.rubrica.modificata:
            return

        risposta = self.input_con_msg_default_valori_ammessi(
            "La rubrica è stata modificata, salvo su disco?", "s", ("s", "S", "n", "N")
        )

        if risposta in ("s", "S"):
            self.rubrica.salva(self.rubrica.nomeFile)


class Comando_foo(Comando):
    def __init__(self, rubrica) -> None:
        super().__init__(rubrica)

    def exec(self):
        pass
