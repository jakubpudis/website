Z = float(input("Dĺžka základne (Z): "))
V = float(input("Výška (V): "))

obsah = (Z * V) / 2
print(f"Obsah trojuholníka: {obsah}")

D = float(input("Dolná hranica intervalu (D): "))
H = float(input("Horná hranica intervalu (H): "))

if D > H:
    print("Chyba: D musí byť ≤ H.")
elif D <= obsah <= H:
    print(f"Obsah ({obsah}) patrí do intervalu ({D}, {H}).")
else:
    print(f"Obsah ({obsah}) nepatrí do intervalu ({D}, {H}).")