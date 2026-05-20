while True:
    cislo = int(input("Zadajte číslo, ktoré chcete premeniť na dvojkovú sústavu: "))
    
    
    binarne = "" 
    while cislo > 0:
        binarne = str(cislo % 2) + binarne  
        cislo = cislo // 2
    
    print(f"Premenené číslo je v dvojkovej sústave {binarne}")
    
    opakovat = input("Ak chcete program zopakovať, stisnite a. Ak chcete skončiť, stisnite iný kláves: ")
    if opakovat.lower() != "a":
        break
