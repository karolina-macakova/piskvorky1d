import util

def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače (znak 'o')"
    # kontrola herni situace
    if '-oo' in pole:  # pocitac uz ma dva symboly vedle sebe a muze doplnit dalsi vlevo
        cislo_policka = pole.find('-oo')  # najdu zacatek substringu '-oo'
        return util.tah(pole, cislo_policka, 'o')  # doplnim symbol pocitace do hraciho pole
    elif 'oo-' in pole:  # pocitac uz ma dva symboly vedle sebe a muze doplnit dalsi vpravo
        cislo_policka = pole.find('oo-') + 2  # najdu konec substringu 'oo-'
        return util.tah(pole, cislo_policka, 'o')  # doplnim symbol pocitace do hraciho pole
    elif '-xx' in pole:  # hrac uz ma dva symboly vedle sebe a muze doplnit dalsi vlevo -> pocitac ho zablokuje
        cislo_policka = pole.find('-xx')  # najdu zacatek substringu '-xx'
        return util.tah(pole, cislo_policka, 'o')  # doplnim symbol pocitace do hraciho pole
    elif 'xx-' in pole:  # hrac uz ma dva symboly vedle sebe a muze doplnit dalsi vpravo -> pocitac ho zablokuje
        cislo_policka = pole.find('xx-') + 2   # najdu konec substringu 'xx-'
        return util.tah(pole, cislo_policka, 'o')  # doplnim symbol pocitace do hraciho pole
    elif '-o' in pole:  # pocitac uz ma jeden symbol a muze doplnit dalsi vlevo
        cislo_policka = pole.find('-o')  # najdu zacatek substringu '-o'
        return util.tah(pole, cislo_policka, 'o')   # doplnim symbol pocitace do hraciho pole
    elif 'o-' in pole:  # pocitac uz ma jeden symbol a muze doplnit dalsi vpravo
        cislo_policka = pole.find('o-') + 1   # najdu konec substringu 'o-'
        return util.tah(pole, cislo_policka, 'o')  # doplnim symbol pocitace do hraciho pole
    elif '-x' in pole:  # hrac ma jeden symbol a muze doplnit dalsi vlevo -> pocitac toto misto obsadi
        cislo_policka = pole.find('-x')  # najdu zacatek substringu '-x'
        return util.tah(pole, cislo_policka, 'o')  # doplnim symbol pocitace do hraciho pole
    else:  # hrac ma jeden symbol a muze doplnit dalsi vlevo -> pocitac toto misto obsadi
        cislo_policka = pole.find('x-') + 1   # najdu konec substringu 'x-'
        return util.tah(pole, cislo_policka, 'o')  # doplnim symbol pocitace do hraciho pole