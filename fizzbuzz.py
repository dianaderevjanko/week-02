import sys
# sys.argv ir saraksts ar visu, ko raksti terminālī.
# sys.argv[0] ir faila nosaukums (fizzbuzz.py)
# sys.argv[1] būs pirmais skaitlis, ko ierakstīsi aiz nosaukuma

if len(sys.argv) > 1:
    # Paņemam pirmo argumentu un pārvēršam par int
    n = int(sys.argv[1])
else:
    # Ja lietotājs aizmirsa ierakstīt skaitli, pajautājam to
    n = int(input("N netika norādīts. Ievadi ciklu skaitu N: "))

print(f"\n--- Python FIZZBUZZ līdz {n} ---")
 # Pirmo pārbaudām kopīgo dalāmību (ar 3 UN 5)
    # Izmantojam modulo operatoru %, kas atgriež atlikumu (0 nozīmē, ka dalās)
if skaitlis % 3 == 0 and skaitlis % 5 == 0: #skaitlis dalās ar 3 un 5
        print("FizzBuzz")
        
    elif skaitlis % 3 == 0:  #Dalot skaitli ar 3, atlikums ir nulle." (Tātad skaitlis dalās ar 3).
        print("Fizz")
        
    elif skaitlis % 5 == 0:  #Dalot skaitli ar 5, atlikums ir nulle." (Tātad skaitlis dalās ar 5)
        print("Buzz")
        
    else:
        print(skaitlis)