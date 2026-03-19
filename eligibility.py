# 1. ievades dati
vecums = int(input("Ievadiet savu vecumu: "))
autoaplieciba = input("Vai jums ir autovadītāja apliecība? (yes/no): ").lower()
veterans = input("Vai esat veterāns? (yes/no): ").lower()
students = input("Vai esat students? (yes/no): ").lower()

# 2. Kompleksais loģiskais nosacījums
if (vecums >= 18 and autoaplieciba == "yes"):
    print("Auto īre:    Jā! ")
else:
    print("Auto īre:    Nē! (nav apliecības)")
