print("Vyberte operáciu:")
print("1. Súčet (+)")
print("2. Rozdiel (-)")
print("3. Násobenie (*)")
print("4. Delenie (/)")

volba = input("Zadajte číslo operácie (1/2/3/4): ")

cislo1 = float(input("Zadajte prvé číslo: "))
cislo2 = float(input("Zadajte druhé číslo: "))

if volba == '1':
    print(f"Výsledok: {cislo1} + {cislo2} = {cislo1 + cislo2}")
elif volba == '2':
    print(f"Výsledok: {cislo1} - {cislo2} = {cislo1 - cislo2}")
elif volba == '3':
    print(f"Výsledok: {cislo1} * {cislo2} = {cislo1 * cislo2}")
elif volba == '4':
    if cislo2 != 0:
        print(f"Výsledok: {cislo1} / {cislo2} = {cislo1 / cislo2}")
    else:
        print("Chyba: Delenie nulou nie je povolené.")
else:
    print("Neplatná voľba. Skúste znova.")
    

