
import threading, time

def write_into_file(filename):


    #jak zapsat číslo do cisla.txt ?
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(5000000):
            f.write(f"Číslo {i}")
start = time.time()

#nahraďte vlákny.
# varianta 1 - vytvořte 4 vlákna ručně
# varianta 2 - vytvořte 4 vlákna ve for cyklu

#write_into_file("cislo1.txt")
#write_into_file("cislo2.txt")
#write_into_file("cislo3.txt")
#write_into_file("cislo4.txt")

#porovnejte dobu zápisu

vlakno1 = threading.Thread(target=write_into_file, args=("cislo1.txt",))
vlakno2 = threading.Thread(target=write_into_file, args=("cislo2.txt",))
vlakno3 = threading.Thread(target=write_into_file, args=("cislo3.txt",))
vlakno4 = threading.Thread(target=write_into_file, args=("cislo4.txt",))
vlakno1.start()
vlakno2.start()
vlakno3.start()
vlakno4.start()
vlakno1.join()
vlakno2.join()
vlakno3.join()
vlakno4.join()

end = time.time()
print(f"Zápis čtyř souborů, vlákna bez for cyklu, trval {end-start:.2f} sekund")
soubory = ["cislo1.txt","cislo2.txt","cislo3.txt","cislo4.txt"]
vlakna = []

start = time.time()
for soubor in soubory:
    nove_vlakno = threading.Thread(target=write_into_file, args=(soubor,))
    nove_vlakno.start()
    vlakna.append(nove_vlakno)

for vlakno in vlakna:
    vlakno.join()

end = time.time()
print(f"Zápis čtyř souborů, verze for cyklus, trval {end-start:.2f} sekund")