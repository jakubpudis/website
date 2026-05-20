hmotnosti = []
for i in range(4):
    hmotnost = float(input(f"Zadaj hmotnosť žiaka {i+1}: "))
    hmotnosti.append(hmotnost)

najmensia_hmotnost = min(hmotnosti)

print(f"Najmenšia hmotnosť je: {najmensia_hmotnost} kg")