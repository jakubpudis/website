# nastavíme slovenské prostredie --> ale toto  nemusí byť!
import locale
locale.setlocale(locale.LC_COLLATE, 'sk_SK.UTF-8')


ziaci =[]
pocetZiakov = int(input('zadajte pocet ziakov: '))
for i in range(pocetZiakov):
    x=input(f"{i}. žiak")
    ziaci.append(x)
print('Neutriedene pole ziakov: ')
print(ziaci)
ziaci.sort()
print(f"Žiaci podľa abecedy: {ziaci}")


