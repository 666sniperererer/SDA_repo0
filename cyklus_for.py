'''
cisla = [3, 4, 5, 20, 30]

for element in cisla:
    print(element * 2)

#Task 39
#napsat for cyklus, který postupně vypíše
#Kočka běhá, Pes běhá, Had běhá
zvirata = ["Kočka", "Pes", "Had"]
for zvire in zvirata:
    print(zvire + " běhá")

#Druhá část úkolu
#napsat for cyklus přes stáří, pro každý prvek (list) vypsat:
#Žirafa má věk 20; Slon má věk 40, Dikobraz má věk 5
stari = [["Žirafa", 20], ["Slon", 40], ["Dikobraz", 5]]
for zvire_vek in stari:
    print(zvire_vek[0] + " má věk " + str(zvire_vek[1]))

#funkce range()
soucet = 0
for i in range(10): #vygeneruje list [0,1,2,3,4,5,6,7,8,9]
    soucet += i
    print(f"Číslo {i} a součet {soucet}")

for x in range(5,10): #vygeneruje list [5,6,7,8,9]
    print(x)

for telefony in range(7,20,3): #vygeneruje list [7,10,13,16,19]
    print(f"Na prodej je {telefony} telefonů")

#Task 41
#vypište čísla 0-5 pomocí for cyklu a funkce range()
for cisla_05 in range(6):
    print(cisla_05)

#vypište čísla 40-46 pomocí for cyklu a funkce range()
for cisla_40_46 in range(40,47):
    print(cisla_40_46)

#vypište čísla 10,20,30,...,80 pomocí for cyklu a funkce range()
for cisla_10_80 in range(10,81,10):
    print(cisla_10_80)

#vypište čísla -4,...,2 pomocí for cyklu a funkce range()
for cisla_m4_2 in range(-4,3):
    print(cisla_m4_2)

#end Task 41

#sestupně - od 8 do 4, pokaždé odečte jedno
for xex in range(8,3,-1):
    print(xex)

#funkce enumerate ()
fruits = ["jablko", "banán", "citrón"]

for index, fruit in enumerate(fruits):
    print(f"Druh ovoce: {fruit}, na indexu: {index}.")

for fruit, index in enumerate(fruits): #enumerate dává index vždy do první proměnné
    print(f"Druh ovoce: {fruit}, na indexu: {index}.")

for index, fruit in [[0,"jablko"], [1, "banán"], [2,"citrón"]]: #zápis toho, co enumerate dělá na pozadí
    print(f"Druh ovoce: {fruit}, na indexu: {index}.")

for index, fruit, animal in [[0,"jablko","Bird"], [1, "banán","Cat"], [2,"citrón","Lion"]]: #zápis toho, co enumerate dělá na pozadí
    print(f"Druh ovoce: {fruit}, na indexu: {index}, se zvířetem {animal}")
'''
'''
#Task 43
platby = [3000,200,18,34444]
#ke každé platbě vypíšeme fakturu
ICO = 3455432
#Vystavuji fakturu ID 0 od firmy s IČO 3455432 na částku 3000
#Vystavuji fakturu ID 1 od firmy s IČO 3455432 na částku 200
#Vystavuji fakturu ID 2 od firmy s IČO 3455432 na částku 18
#Vystavuji fakturu ID 3 od firmy s IČO 3455432 na částku 34444

for faktura, platba in enumerate(platby):
    print(f"Vystavuji fakturu ID {faktura} s IČO {ICO} na částku {platba}")
'''
#Task 44
faktury_k_vystaveni = [
    ["Panasonic", 30000, "Martin Novotný"],
    ["Oracle", 22000, "Petr Lukoš"],
    ["Porsche", 32345, "Ivo Gira"],
    ["Siemens", 2000, "Luboš Šejk"],
]
ico_moji_firmy = 3456785
#Vypište
#Faktura ID 0. Vystavuje firma 3456785. Faktura pro Martin Novotný na částku 30000 pro firmu Panasonic

for index, faktura in enumerate(faktury_k_vystaveni):
    firma = faktura[0]
    platba = faktura[1]
    k_rukam = faktura[2]
    print(f"Faktura ID {index} Vystavuje firma {ico_moji_firmy}. "
          f"Faktura pro {k_rukam} na částku {platba} pro firmu {firma}")

#Řešení při použití indexování
for index, prvek_nepouziju in enumerate(faktury_k_vystaveni): #jako prvek_nepouziju se často používá podtržítko
    #print(index)
    i = index
    ic = ico_moji_firmy
    jm = faktury_k_vystaveni[index][2]
    czk = faktury_k_vystaveni[index][1]
    fir = faktury_k_vystaveni[index][0]
    print(f"Faktura ID {i} Vystavuje firma {ic}. "
          f"Faktura pro {jm} "
          f"na částku {czk} "
          f"pro firmu {fir}")

#Automatické rozbalení tuplu
clovek = ("Aleš", 33, "Programátor")
jmeno, vek, prace = clovek
print(f"{jmeno}, {vek}, {prace}")