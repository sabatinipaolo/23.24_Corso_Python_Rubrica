import csv
import os

def creaCsv(csvFile):

    if not os.path.exists(csvFile):
        with open(csvFile, 'a'): 
            pass

def listaContatti(csvFile):
    with open(csvFile, 'r') as file:
        reader = csv.reader(file)
        stampaSelezioneDiContatti(reader)

def aggiungeContatto(csvFile, nome, telefono):
    with open(csvFile, 'a', newline='') as file:
        writer = csv.writer(file)
        # scrive la riga rimuovendo spazi iniziali,finali e multipli...
        writer.writerow([" ".join(nome.split()).strip(), " ".join(telefono.split()).strip()])


def contattiDaRicerca(csvFile,stringaRicerca):
    contattiRicercati=[]
    with open(csvFile, 'r') as file:
        reader = csv.reader(file)
        for (nome,telefono) in reader:
            if ( stringaRicerca in nome or
                 stringaRicerca in telefono ):
                    contattiRicercati.append([nome,telefono])
    return contattiRicercati

def rimuoviContatti( csvFile , contattiDaRimuovere ):
    contattiDaMantenere = []
    with open(csvFile, 'r') as file:
        reader = csv.reader(file)
        for riga in reader:
            if riga not in contattiDaRimuovere :
                contattiDaMantenere.append(riga)

    with open(csvFile, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contattiDaMantenere)


def stampaSelezioneDiContatti(contattiRicercati ):

    if not contattiRicercati :
        print ( "la selezione non ha prodotti risultati")
        return
    
    for (nome,telefono) in contattiRicercati:
        print( f"{nome} => {telefono}")

