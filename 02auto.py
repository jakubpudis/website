# Zadanie vstupných údajov
rychlost_kmh = 60          # rýchlosť v km/h
spotreba_na_100km = 7.2    # l/100 km
spotreba_na_1km = spotreba_na_100km/100   # l/1 km
vzdialenost_m = float(input("Zadaj vzdialenosť medzi mestami (v metroch): "))

# Prevod rýchlosti na m/s 
rychlost_ms = rychlost_kmh / 3.6

# Výpočet času v sekundách
cas_s = vzdialenost_m / rychlost_ms

# Výpočet spotreby paliva

# Prevod vzdialenosti na km
vzdialenost_km = vzdialenost_m / 1000
# Spotreba v litroch
spotreba_l = vzdialenost_km * spotreba_na_1km
# Spotreba v ml
spotreba_ml = spotreba_l * 1000

# Výpis výsledkov
print(f"Čas jazdy: {round(cas_s,2)} sekúnd")
print(f"Spotreba benzínu: {round(spotreba_ml,2)} ml")