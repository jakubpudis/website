ziaci = []
vysky = []

pocetZiakov = int(input('Zadajte počet žiakov: '))

for i in range(pocetZiakov):
    x = input(f'Zadaj meno {i+1} žiaka: ')
    ziaci.append(x)
    vyskaZiaka = int(input('Zadajte výšku žiaka: '))
    vysky.append(vyskaZiaka)

print('Neutriedené pole žiakov:', ziaci)
print('Neutriedené pole výšok:', vysky)

# spojíme, zotriedime podľa výšky a rozpojíme
spolu = list(zip(vysky, ziaci))
spolu.sort()

vysky, ziaci = zip(*spolu)

# premeníme späť na zoznamy
vysky = list(vysky)
ziaci = list(ziaci)

print("Utriedené osoby")
for i in range(len(ziaci)):
    print(f"{ziaci[i]}, {vysky[i]}cm")





