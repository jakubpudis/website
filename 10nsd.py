def delitel(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a 

a = 0
while a == 0 :
    a = int(input("Zadajte prvé číslo: "))
b = 0
while b == 0:
     b = int(input("Zadajte druhé číslo: "))
a = abs(a)
b = abs (b)

d = delitel(a,b)
print("Najväčší spoločný deliteľ čísel", a, "a", b, "je číslo", d)