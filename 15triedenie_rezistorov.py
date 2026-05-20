pole =[]
pocetRezistorov = int(input('zadajte pocet rezistorov: '))
for i in range(pocetRezistorov):
    x=int(input(f"zadaj odpor {i+1}. rezistora"))
    pole.append(x)
print('Neutriedene pole: ')
print(pole)
pole.sort()
print()
print('Utriedene pole: ')
print(pole)

