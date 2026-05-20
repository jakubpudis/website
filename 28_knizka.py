p = int(input('Zadajte úrok (v %): '))  # Ročný úrok v percentách
ciastka = int(input('Zadajte cieľovú sumu: '))  # Cieľová suma na prekročenie
vklad = 500
suma = 0
rok = 0

# Výpočet sumy po 10 rokoch s ročnými vkladmi
for i in range(10):
    suma = (vklad + suma) * (1 + p / 100)   # pridáme nový vklad a aplikujem úrok
print(f'Za 10 rokov bude na knižke suma:  {round(suma, 2)} €')

# Výpočet počtu rokov na prekročenie zadané cieľovej sumy
suma = 0 #obnoviť sumu 
while suma <= ciastka:
    rok += 1
    suma = (vklad + suma) * (1 + p / 100) 
print(f'Úspory prekročia cieľovú sumu  {ciastka} € za {rok} rokov')