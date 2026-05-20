import random
minca = ["rub", "lice"]
hody = []

for i in range(100):
    hod=random.choice(minca)
    hody.append(hod)
    
print(hody)

x=hody.count("rub")
y=hody.count("lice")

print(f" výskyt rubu je {x}-krát")
print(f" výskyt rubu je {y}-krát")
