# Načítanie prvého intervalu od užívateľa
a = int(input("Zadajte začiatok prvého intervalu: "))
b = int(input("Zadajte koniec prvého intervalu: "))

if a>b:
   print("zadal si to zle, ale ja som to opravil")
   b,a = a,b

# Načítanie druhého intervalu od užívateľa
c = int(input("Zadajte začiatok druhého intervalu: "))
d = int(input("Zadajte koniec druhého intervalu: "))

if c>d:
   print("zadal si to zle, ale ja som to opravil")
   d,c = c,d

# Prienik je prázdny, ak sa intervaly neprekrývajú
if b < c or d < a:
   print ( f"Prienik je prázdna množina." )
    
# Prienik je bod, ak sa intervaly dotýkajú v jednom bode
elif b == c or d == a:
   print( f"Prienik je bod: {max(a, c)}")
    
# Prienikom je interval
else:
    prienik_zaciatok = max(a, c)
    prienik_koniec = min(b, d)
    print (f"Prienik je interval: [{prienik_zaciatok}, {prienik_koniec}]")




