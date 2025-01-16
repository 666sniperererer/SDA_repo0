'''
Task 73 - nákupní seznam
1. Pridať položku
2. Vypísať všetky položky
3. Zmazať položku
4. Upraviť položku
5. Uložiť zoznam do CSV
6. Načítať zoznam z CSV
7. Uložiť zoznam do pickle
8. Načítať zoznam z pickle
'''
import csv
import pickle

global seznam
seznam = []

def vypis_seznam():
    print("-------------------")
    print("Aktuální seznam je:")
    for index, item in enumerate(seznam):
        print(f"{index + 1} - {item}")
    print("-------------------")

while True:
    print("1. Přidat položku")
    print("2. Vypsat všechny položky")
    print("3. Smazat položku")
    print("4. Upravit položku")
    print("5. Uložit seznam do CSV")
    print("6. Načíst seznam z CSV")
    print("7. Uložit seznam do pickle")
    print("8. Načíst seznam z pickle")
    vyber = int(input("Zvol možnost: "))

    if vyber == 1: #1. Přidat položku"
        vypis_seznam()
        seznam.append(input("Jakou položku chceš přidat? "))
        vypis_seznam()

    if vyber == 2: #2. Vypsat všechny položky
        vypis_seznam()

    if vyber == 3: #3. Smazat položku
        vypis_seznam()
        seznam.pop(int(input("Jakou položku chceš odstranit? "))-1)
        vypis_seznam()

    if vyber == 4: #4. Upravit položku
        vypis_seznam()
        k_uprave = int(input("Jakou položku chceš upravit? ")) - 1
        seznam[k_uprave] = input("Zadej novou položku: ")
        vypis_seznam()

    if vyber == 5: #5. Uložit seznam do CSV
        nazev_souboru = input("Zadej název souboru CSV pro uložení: ")
        with open(nazev_souboru+".csv", 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            for item in seznam:
                writer.writerow([item])


    if vyber == 6: #6. Načíst seznam z CSV
        nazev_souboru = input("Zadej název souboru CSV pro otevření: ")
        with open(nazev_souboru+".csv") as in_file:
            reader = csv.reader(in_file)
            seznam = [row[0] for row in reader]
        vypis_seznam()

    if vyber == 7: #7. Uložit seznam do pickle
        nazev_souboru = input("Zadej název souboru PICKLE pro uložení: ")
        with open(nazev_souboru+".pickle", "wb") as f:
            pickle.dump(seznam, f)

    if vyber == 8: #8. Načíst seznam do pickle
        nazev_souboru = input("Zadej název souboru PICKLE pro otevření: ")
        with open(nazev_souboru+".pickle", "rb") as f:
            seznam = pickle.load(f)
        vypis_seznam()

    if vyber not in range(1,8) and not 99:
        print("Chybná volba, můžeš volit jen 1-8.")
        pass

    if vyber == 99: #ukončení uživatelem
        print("Au-revoir!")
        break