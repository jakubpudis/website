
# získanie čísla 
A = float(input("Zadajte kladné číslo (A): "))

# ošetrenie kladného čísla
while A < 0:
    print("Číslo musí byť kladné. Skúste to znova.")
    A = float(input("Zadajte kladné číslo (A): "))

# Získanie exponentu n
n = int(input("Zadajte exponent (n): "))

# Výpočet mocniny
vysledok = (A) ** n

# Výstup výsledku
print(f"{A} na {n} je {vysledok}")
