import random
kocka = ["1", "2","3", "4","5", "6"]
pocty = [0]*6
n = int(input("koľko hodov?"))

for i in range(n):
    hod=random.randint(0,5)
    pocty[hod] += 1

print(kocka)
print (pocty)

for i in range(6):
    print(f" výskyt {kocka[i]} je {pocty[i]}-krát")
