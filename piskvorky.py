from random import randrange
import ai
import util

def vyhodnot(pole):
    "vyhodnoti retezec s hernim polem 1-D piskvorek"
    if 'xxx' in pole: # pole obsahuje "xxx"
        return 'x'       # vyhral hrac s krizky
    elif 'ooo' in pole: # pole obsahuje "ooo"
        return  'o'        # vyhral hrac s kolecky
    elif '-' not in pole: # pole neobsahuje "-", ale nikdo nevyhral
        return '!'           # remiza
    else:          # hra jeste neskoncila
        return '-'




def tah_hrace(pole):
    """
    Funkce dostane řetězec s herním polem,
    zeptá se hráče, na kterou pozici chce hrát,
    a vrátí herní pole se zaznamenaným tahem hráče (znak 'x').
    Funkce odmítá záporná nebo příliš velká čísla a
    tahy na obsazená políčka.
    Pokud uživatel zadá špatný vstup, funkce mu vynadá a zeptá se znova.
    """
    # hrac zada policko, na ktere chce hrat
    vstup_hrace = input("Zadej políčko, na které chceš hrát (čísla 0-19): ")

    # kontrola, zda hrac zadal pouze cisla
    if not vstup_hrace.isdigit():
        print("Nezadal/a jsi čísla! Lze zadat pouze číslo 0-19.")  # upozornime hrace, ze nezadal jen cisla
        return tah_hrace(pole)  # zavolame funkci znova, aby mohl hrac zadat pole znovu

    else:
        cislo_policka = int(vstup_hrace)  # hrac zadal pouze cisla -> prevedeme na integer cislo_policka

        # kontrola, zda muzeme zapsat tah
        if cislo_policka < 0 or cislo_policka > 19:  # kontrola, zda je zadáno číslo 0 - 19
            print("Nezadal/a jsi platné číslo políčka - platná čísla políček jsou pouze 0-19")  # upozornime hrace, ze zadal spatne cislo
            return tah_hrace(pole)  # zavolame funkci znova, aby mohl hrac zadat pole znovu

        elif pole[cislo_policka] != '-':  # kontrola, zda je pole volne (volne pole = '-', obsazene = 'x' nebo 'o')
            print("Pole už je obsazené!")  # upozornime hrace, ze pole uz je obsazene
            return tah_hrace(pole)  # zavolame funkci znova, aby mohl hrac zadat pole znovu
        else:
            nove_pole = util.tah(pole, cislo_policka, 'x') # vrátíme pole s doplněným tahem
            return nove_pole



def piskvorky1d():
    prubeh_hry = '--------------------'  # aktualni herni pole, defaultni hodnota je prazdne pole
    cislo_tahu = 1 # defaultni cislo tahu
    vysledek = '-' # defaultni vysledek

    while vysledek == '-': # dokud hra neskoncila, cyklus pokracuje
        if cislo_tahu % 2 == 1:  # hru zacina hrac
            prubeh_hry = tah_hrace(prubeh_hry)  #pridame tah hrace
            print("Hráč:", prubeh_hry)
        else: # pokracuje pocitac
            prubeh_hry = ai.tah_pocitace(prubeh_hry)  # do listu pridame tah pocitace
            print("Počítač:", prubeh_hry)

        vysledek = vyhodnot(prubeh_hry)  # vyhodnoti vysledek

        # pokud hra skoncila, vypise vysledek a posledni hrane pole, jinak zvysi cislo tahu a cyklus pookracuje
        if vysledek == '-':
            cislo_tahu += 1
            continue
        elif vysledek == 'x':
            print("Vyhral hrac!", prubeh_hry)
            break
        elif vysledek == 'o':
            print("Vyhral pocitac!", prubeh_hry)
            break
        elif vysledek == '!':
            print("Remiza", prubeh_hry)
            break