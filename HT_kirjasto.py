######################################################################
# CT60A0203 Ohjelmoinnin perusteet kurssin harjoitustyö
# Tekijä: Marianne Seppänen 
# Päivämäärä: 18.11.2019
# Harjoitustyön kirjasto löytyy tästä tiedostosta. Pääohjelma löytyy tiedostosta Harkkatyo.py
######################################################################

import datetime
import sys

class TIEDOT:
    pvm = ""
    kello = ""
    paiste = 0


def valinta1():
    nimi = input("Anna havaintoaseman nimi: ")
    while True:
        try:
            vuosi = input("Anna analysoitava vuosi: ")
            break
        except ValueError:
            print("Anna vuosiluku kokonaislukuna.")
    tiedosto = nimi+vuosi+".txt"
    print()
    return tiedosto


def valinta2(file, lista):
    lkm = 1
    lista.clear()
    try:
        tiedosto = open(file, "r")
    except:
        print("Tiedoston '"+file+"' avaaminen epäonnistui.")
        sys.exit(0)

    try:
        tiedosto.readline() # luetaan ensimmäinen rivi pois alta
        while True:
            rivi = tiedosto.readline()
            lkm = lkm+1
            if (len(rivi) == 0):
                break
            sarake = rivi.split(";")
            data = TIEDOT()
            data.pvm = datetime.datetime.strptime(sarake[0], "%Y-%m-%d")
            data.kello = datetime.datetime.strptime(sarake[1], "%H:%M")
            data.paiste = int(sarake[2])
            lista.append(data)
    except:
        print("Tiedoston '"+file+"' lukeminen epäonnistui.")
        tiedosto.close()
        return None
            
    print("Tiedosto '{0}' luettu. Tiedostossa oli {1} riviä.".format(file, lkm))
    print()
    tiedosto.close()
    return lista


def valinta3(lista, tulokset):
    # täällä lasketaan päivien paisteajat yhteensä
    tulokset.clear()
    try:
        eka_paiva = lista[0].pvm
        vika_paiva = lista[-1].pvm
    except:
        print("Lista on tyhjä. Lue ensin tiedosto.")
        return lista
    aurinko = 0
    for alkio in lista:
        if alkio.pvm == eka_paiva:
            aurinko = aurinko + alkio.paiste
            
        else:
            data = TIEDOT()
            data.paiste = aurinko
            data.pvm = eka_paiva
            tulokset.append(data)
            eka_paiva = eka_paiva + datetime.timedelta(days=1)
            aurinko = aurinko + alkio.paiste


    if eka_paiva == vika_paiva:
            data = TIEDOT()
            data.paiste = aurinko
            data.pvm = eka_paiva
            tulokset.append(data)
    
    
    eka = lista[0].pvm.strftime("%d.%m.%Y")
    vika = lista[-1].pvm.strftime("%d.%m.%Y")
    print("Data analysoitu ajalta "+eka+" - "+vika+".")
    print()
    return tulokset

def valinta4(tulokset, asema):
    tulostied = input("Anna tulostiedoston nimi: ")
    try:
        tiedosto = open(tulostied, "w")
    except:
        print("Tiedoston '"+tulostied+"' avaaminen epäonnistui.")
        sys.exit(0)

    havainto = asema[:-8]

    try:
        tiedosto.write("Pvm")
        luku = 0
        try:
            for alkio in tulokset:
                tiedosto.write(";" + tulokset[luku].pvm.strftime("%d.%m.%Y"))
                luku = luku + 1
        except:
            print("Lista on tyhjä. Analysoi data ennen tallennusta.")
            return tulokset
        
        tiedosto.write("\n" + havainto)
        luku = 0
        for alkio in tulokset:
            aurinko = tulokset[luku].paiste
            aurinko = int(aurinko / 60)
            tiedosto.write(";" + str(aurinko))
            luku = luku + 1
        tiedosto.write("\n")
    except:
        print("Tiedoston '"+tulostied+"' kirjoittaminen epäonnistui.")
        tiedosto.close()
        return None
    
    print("Paisteaika tallennettu tiedostoon '"+tulostied+"'.")
    tiedosto.close()
    print()
    return None


def valinta0():
    print("Kiitos ohjelman käytöstä.")
    return None

