from itertools import permutations
g= 0
for p in permutations(range(10), 10):
    S, A, G, O, N, F, E, L, I, C = p
    if S>=5 and F==1 and (S*1000 + A*100 + G*10 + O) + (S*1000 + A*100 + N*10 + O) == (F*10000 + E*1000 + L*100 + I*10 + C):
        print(f"SAGO={S*1000 + A*100 + G*10 + O}, SANO={S*1000 + A*100 + N*10 + O}, FELIC={F*10000 + E*1000 + L*100 + I*10 + C}")
        g += 1
print(g)
 

# V tomto kóde sa používa funkcia permutations z modulu itertools v Pythone, 
# ktorá generuje všetky permutácie čísel od 0 do 9 (v rozsahu range(10)), pričom každá permutácia má dĺžku 10. 
# Kód priraďuje tieto permutácie do premenných S, A, G, O, N, F, E, L, I a C.

#Prvá časť kódu, permutations(range(10), 10), vygeneruje všetky možné poradia desiatich čísel z množiny 
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, teda všetky možné spôsoby zoradenia týchto desiatich čísel. 
# Počet permutácií je teda 10! (10 faktoriál), čo je 3 628 800 rôznych usporiadaní.

#Druhá časť kódu, S, A, G, O, N, F, E, L, I, C = p, 
# priradí jednotlivé hodnoty permutácie do premenných S, A, G, O, N, F, E, L, I a C 
# podľa poradia v permutácii.