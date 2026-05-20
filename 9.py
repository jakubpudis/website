import random

def nasobCisla(a,b):
    print("Vynásob tento príklad: ", a,"*",b,"= ?")
    vysledok = int(input("tvoj vysledok je: "))
    spravne = (a*b)
    if vysledok == spravne :
    	print("Správne")
    else:
        print("Zle. Správny výsledok je:", spravne)

cislo1 = int(input("zadajte prve cislo: "))
while  cislo1 < 0 or cislo1  > 10:
    print("Cislo1 musi byt medzi 0 a 10")       
    cislo1 = int(input("zadajte prve cislo: "))
    
cislo2 = int(input("zadajte prve cislo: "))
while  cislo2 < 0 or cislo2  > 10:
    print("Cislo2 musi byt medzi 0 a 10")     
    cislo2 = int(input("zadajte druhe cislo: "))

nasobCisla(cislo1,cislo2)

while True:
    odpoved =(input("Ak chcete ďalsi priklad stlačte a"))
    if (odpoved == "a" or odpoved == "A" ):
        prveCislo = random.randint(0, 10)
        druheCislo = random.randint(0, 10)
        nasobCisla(prveCislo,druheCislo)
    else:
        break