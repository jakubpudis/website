"""
def rozklad(suma):
    patsto = suma//500
    zvysok = suma%500
    print("Pocet patstoviek je:", patsto)
    suma = zvysok
    dvesto = suma//200
    zvysok = suma%200
    print("Pocet dvestoviek je:", dvesto)
    suma = zvysok
    sto = suma// 100
    zvysok = suma%100
    print("Pocet stoviek je:", sto)
    suma = zvysok
    patdesiat = suma// 50
    zvysok = suma%50
    print("Pocet patdesiatok je:", patdesiat)
    suma = zvysok
    dvadsat = suma// 20
    zvysok = suma%20
    print("Pocet dvadsiatok je:", dvadsat)
    suma = zvysok
    desat = suma// 10
    zvysok = suma%10
    print("Pocet desiatok je:", desat)
    suma = zvysok
    pat = suma// 5
    zvysok = suma%5
    print("Pocet patiek je:", pat)
    suma = zvysok
    dva = suma// 2
    zvysok = suma%2
    print("Pocet dvojok je:", dva)
    suma = zvysok
    print("Pocet jednotiek je:", zvysok)

suma = int(input("zadajte sumu: "))

rozklad(suma)
"""


def rozklad(suma):
    for i in 500, 200, 100, 50, 20, 10, 5, 2, 1: 
        cena = suma//i
        zvysok = suma%i
        suma = zvysok
        print(f"Pocet {i} je:", cena)

suma = int(input("zadajte sumu: "))
rozklad(suma)