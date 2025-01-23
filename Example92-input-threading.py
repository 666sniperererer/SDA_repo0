#Part 1

import threading

import time

def get_input_and_count():
    user_input = input("Zadej číslo")
    for i in range(6):
        print(int(user_input) + i)
        time.sleep(1)

vlakno1 = threading.Thread(target=get_input_and_count)
vlakno2 = threading.Thread(target=get_input_and_count)
vlakno1.start()
vlakno2.start()

vlakno1.join()
vlakno2.join()


import threading, time

def sbirej_snimky():
    for i in range(20):
        print(f"Vyfocen snímek v čase {time.time():.3f} sekund")
        time.sleep(0.5)

vlakno_kamery = threading.Thread(target=sbirej_snimky)
vlakno_kamery.start()
vstup_od_uzivatele = input("Zadej kolik čárových kodu chceš přečíst")
print(f"Dobře, přečtu {vstup_od_uzivatele} kódů ")

vlakno_kamery.join()
print("Hotovo")




#zadej dvě čísla a program začal zpracovávat ve dvou vláknech

import threading, time
def asfaltovani_silnice(nazev):
    for i in range(20):
        print(f"Asfaltuji silnici {nazev} na kilometru {i}")
        time.sleep(1)

vlakna = []
dalnice = input("Zadej názvy dálnic, které chceš asfaltovat. (odděl čárkou)")
for silnice in dalnice.split(","):
    nove_vlakno = threading.Thread(target=asfaltovani_silnice, args=(silnice,))
    nove_vlakno.start()
    vlakna.append(nove_vlakno)

for vlakno in vlakna:
    vlakno.join()



import threading, time

def nasobit_dvema(vstup):
    for i in range(10):
        time.sleep(1)
        print(vstup*i)

vlakno1 = threading.Thread(target=nasobit_dvema, args=(10,))
vlakno2 = threading.Thread(target=nasobit_dvema, args=(256,))
vlakno1.start()
vlakno2.start()
vlakno1.join() #počkám na dokončení
vlakno2.join()