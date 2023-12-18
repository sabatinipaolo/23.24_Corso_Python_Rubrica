from enum import nonmember
from RubricaMod import *

csvFile = "rubrica.csv"
creaCsv(csvFile)

while True:
    print(
        "\n[ L/l lista contatti] [ A/a aggiungi contatto ]  [ C/c cerca contatto ] [ R/r Rimuovi Contatto ] [ E/e Exit ]"
    )

    scelta = input("inserire commando: ")

    if scelta in ("L", "l"):
        print("\nLista dei contatti:\n")
        listaContatti(csvFile)

    elif scelta in ("A", "a"):
        nome = input("Nome: ")
        telefono = input("Telefono: ")
        aggiungeContatto(csvFile, nome, telefono)
        print("contatto aggiunto alla rubrica")

    elif scelta in ("C", "c"):
        stringaRicerca = input("Inserisci nome e/o tel da cercare: ")
        contattiRicercati = contattiDaRicerca(csvFile, stringaRicerca)
        print("\nrisultato ricerca: \n")
        stampaSelezioneDiContatti(contattiRicercati)

    elif scelta in ("R", "r"):
        stringaRicerca = input("Inserisci nome e/o tel da Cancellare: ")
        contattiRicercati = contattiDaRicerca(csvFile, stringaRicerca)
        if contattiRicercati:
            print("ATTENZIONE I SEGUNETI CONTATTI VERRANNO CANCELLATI")
            stampaSelezioneDiContatti(contattiRicercati)
            risposta = input("Sei sicuro di voler procedere? (S/n)")
            if risposta in ("S", "s"):
                rimuoviContatti(csvFile, contattiRicercati)
                print ("contatti cancellati")
        else:
            print("nilla da cancellare")

    elif scelta in ("E", "e"):
        print("arrivederci")
        break

    else:
        print("comando no riconosciuto")
