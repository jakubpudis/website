while True:
    # Zadanie koeficientov od používateľa
    a = float(input("Zadajte koeficient a: "))
    
    # Kontrola, či a nie je 0
    if a == 0:
        print("Koeficient 'a' nemôže byť 0, pretože to nie je kvadratická rovnica. Zadajte nové hodnoty.")
        continue

    b = float(input("Zadajte koeficient b: "))
    c = float(input("Zadajte koeficient c: "))

    # Výpočet diskriminantu
    D = b**2 - 4*a*c

    # Kontrola počtu riešení na základe diskriminantu
    if D > 0:
        x1 = (-b + (D)**0.5) / (2 * a)
        x2 = (-b - (D)**0.5) / (2 * a)
        print(f"Rovnica má dve rôzne reálne riešenia: x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"Rovnica má jedno reálne riešenie: x = {x}")
    else:
        print(f"Rovnica nemá riešenie")

    # Spýtať sa používateľa, či chce pokračovať
    pokracovat = input("Chcete zadať nové parametre? (áno/nie): ").strip().lower()
    if pokracovat != 'áno':
        print("Program sa ukončuje.")
        break