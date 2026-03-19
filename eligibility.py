# 1. ievades dati
vecums = int(input("Ievadiet savu vecumu: "))
autoaplieciba = input("Vai jums ir autovadītāja apliecība? (yes/no): ").lower()
veterans = input("Vai esat veterāns? (yes/no): ").lower()
students = input("Vai esat students? (yes/no): ").lower()
print("\n--- ------------- ---")

# 2. Kompleksais loģiskais nosacījums
if (vecums >= 21 and autoaplieciba == "yes"):
    print("Auto īre:    Jā! ")
else:
    print("Auto īre:    Nē! (nav apliecības)")

if (vecums >= 18):
    print("Balsot:      Jā! ")
else:    print("Balsot:      Nē!")

if (vecums >= 65 or veterans == "yes"):
    print("Saņemt senioru atlaidi: Jā! ")
else:    print("Saņemt senioru atlaidi: Nē!")

if (students == "yes" and 16 <= vecums <= 26):
    print("Saņemt studentu atlaidi::    Jā! ")
else:    print("Saņemt studentu atlaidi:    Nē!")