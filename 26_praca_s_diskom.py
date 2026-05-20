while True:
    f = open("text.txt", "r")

    mena = f.readlines()   
    for i in range (len(mena)):
        mena[i]=mena[i].strip()

    mena2 = []
    pocet = 0
    pismeno = input("Zadaj pismeno: ")
    for prvok in mena: 
        if prvok[0]==pismeno.upper():
            mena2.append(prvok)
            pocet+=1

    print(f"počet mien so žiatočným písmenom {pismeno} je: {pocet}")
    print(f"mena v kalendári so začiatočným písmenom {pismeno}:")
    for meno in mena2:
        print(meno)

    f.close()
    pokracovat = input("chcete pokračovať? a/n").lower()
    if pokracovat == "n":
        break
