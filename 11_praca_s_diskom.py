pocet = int(input("Zadaj pocet priezvisk: "))
f = open("text.txt", "w")
for i in range (pocet):
    priezvisko = input("Zadaj priezvisko: ")
    f.write(f"{priezvisko}\n")
f.close()

f = open("text.txt", "r")

mena = f.readlines()   
for i in range (len(mena)):
    mena[i]=mena[i].strip()

pismeno = input("Zadaj pismeno: ")
for prvok in mena: 
    if prvok[0]==pismeno.capitalize():
        print(prvok)     

f.close()
