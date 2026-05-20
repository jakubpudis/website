import random

while True:
    
    od = int(input("Zadaj spodnú hranicu rozsahu: "))
    do = int(input("Zadaj hornú hranicu rozsahu: "))

    myslenecislo = random.randint(od, do)
    print("Myslím si číslo... Skús uhádnuť!")

    while True:
        tip = int(input("Tvoj tip: "))

        if tip == myslenecislo:
            print("TRAFIL SI!")
            break
        elif tip < myslenecislo:
            print("PRIDAJ!")
        else:
            print("UBER!")

    znova = input("Chceš hrať znova? (áno/nie): ").lower()
    if znova != "áno":
        print("Hra skončila. Ďakujem za hranie!")
        break