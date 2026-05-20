
zoznam_priezvisk = ["Horváth", "Novák", "Andres", "Kováč", "Bartoš"]

print(zoznam_priezvisk)

zoznam_priezvisk.sort()

print(zoznam_priezvisk)

hladane_priezvisko = input("Zadajte priezvisko na vyhľadanie: ")

if hladane_priezvisko in zoznam_priezvisk:
    print(f"Priezvisko {hladane_priezvisko} bolo nájdené v zozname.")
else:
    print(f"Priezvisko {hladane_priezvisko} nebolo nájdené v zozname.")