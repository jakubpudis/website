f = open("mena.txt", "r")
mena = f.readlines()

for i in range(len(mena)):
    mena[i] = mena[i].strip()

print(mena)
pocet_mien = len(mena)
print(f"Počet mien v súbore: {pocet_mien}")

zadane_meno = input("Zadaj meno: ")
if zadane_meno in mena:
    print(f"Meno '{zadane_meno}' sa nachádza v zozname.")
else:
    print(f"Meno '{zadane_meno}' sa v zozname nenachádza.")

f.close()
