f = 1
for i in range(1,11):
    f = f * i
print('1 . 2 . 3 . 4 . 5 . 6 . 7 . 8 . 9 . 10 =', f)
print('\n')
n = 0
while n <= 0:
    n = int(input('Zadajte prirodzené číslo, ktorého faktoriál chcete vypočítať: '))
f = 1
for i in range(1,n+1):
    f = f * i
print(str(n)+'! =', f)