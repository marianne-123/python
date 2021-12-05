######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Marianne Seppänen
# Opiskelijanumero: 568655 
# Päivämäärä: 8.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto:
# Harjoitustyö
######################################################################

import HT_kirjasto
import datetime

def paaohjelma():
    lista = []
    tulokset = []
    while True:
        print("Mitä haluat tehdä:")
        print("1) Anna havaintoasema ja vuosi")
        print("2) Lue säätilatiedosto")
        print("3) Analysoi päivittäiset säätilatiedot")
        print("4) Tallenna päivittäiset säätilatiedot")
        print("0) Lopeta")
        try:
            valinta = int(input("Valintasi: "))
        except ValueError:
            print("Anna valinta kokonaislukuna.")
            continue
        except:
            print("Valintaa ei tunnistettu, yritä uudestaan.")
            continue
        if valinta == 1:
            tiedosto = HT_kirjasto.valinta1()

        elif valinta == 2:
            HT_kirjasto.valinta2(tiedosto, lista)

        elif valinta == 3:
            HT_kirjasto.valinta3(lista, tulokset)

        elif valinta == 4:
            HT_kirjasto.valinta4(tulokset, tiedosto)

        elif valinta == 0:
            HT_kirjasto.valinta0()
            break
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.")
            print()

paaohjelma()

