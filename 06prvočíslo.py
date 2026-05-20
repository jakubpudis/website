cislo = int(input("Zadaj číslo:"))
while cislo <= 1:
    cislo = int(input("Zadaj číslo:"))
pocetdelitelov = 0

for i in range(cislo):
    if cislo%(i+1) == 0:
        pocetdelitelov =  pocetdelitelov + 1

if pocetdelitelov == 2:
    print("prvocislo")
else:
    print("zlozene cislo")
