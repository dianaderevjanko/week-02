#konstances
KM_TO_MILES = 0.621371
KG_TO_LBS = 2.20462
L_TO_GALLONS = 0.264172
USD_TO_EUR = 0.85235
print('Konversijas kalkulators')
izvele = input("Izvelies konvērsiju: 1)km<->mi, 2)kg<->lb 3)L<->gal 4)USD<->EUR   ")
#pārbaudam lai izvēle būtu pareiza
if izvele == "1":
    print('Izvelies virzienu: 1) KM/MI 2 )MI/KM ' )
    virziens = input("Ievadi virzienu: ")
    if virziens == "1":
        vertiba = float(input("Ievadi vērtību, kuru vēlies konvertēt: "))
        rezultats = vertiba * KM_TO_MILES
        print(f"Rezultāts: {vertiba :.2f} km ir {rezultats:.2f} mi.")  #:.2f - noapaļo rezultātu līdz 2 cipariem aiz komata
    elif virziens == "2":
        vertiba = float(input("Ievadi vērtību, kuru vēlies konvertēt: "))
        rezultats = vertiba / KM_TO_MILES
        print(f"Rezultāts: {vertiba :.2f} mi ir {rezultats:.2f} km.")
    else:
        print("Kļūda! Lūdzu, izvēlies pareizo virzienu.")