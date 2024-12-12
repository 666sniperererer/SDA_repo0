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