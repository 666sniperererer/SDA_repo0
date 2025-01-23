#Ukázka generátoru sudých čísel
'''
def gen_even(n):
    i = 0
    genereted_count = 0
    while genereted_count < n:
        print(f"Již jsme vygenerovali {genereted_count} čísel a i je {i}")
        if i % 2 == 0: #tzn.sudé číslo
            genereted_count += 1
            yield i
        i += 1


for sude_cislo in gen_even(5):
    print(f"Mám sudé číslo {sude_cislo}")


def gen_tri_jmena():
    yield "Zuzana"
    yield "Xenie"
    yield "Patrik"

for jmeno in gen_tri_jmena():
    print(jmeno)
'''
#Úloha, udělejte generátor, který generuje následující sekvenci:
'''
1
2
3
5
8
13
21
34
'''
'''
def generator_scitani(celkem_iteraci):
    aktualni_iterace = 0
    predchozi_cislo1 = 1
    predchozi_cislo2 = 0
    while aktualni_iterace < celkem_iteraci:
        aktualni_cislo = predchozi_cislo1 + predchozi_cislo2
        predchozi_cislo2 = predchozi_cislo1
        predchozi_cislo1 = aktualni_cislo
        yield aktualni_cislo
        aktualni_iterace += 1

for cislo in generator_scitani(8):
    print(cislo)
'''
'''
def generator_pismenek(pismena, delka):
    aktualni_start = 0
    posun = 0
    pismeno = ""
    vysledek = ""
    while delka + aktualni_start <= len(pismena):
        while delka >= posun + 1:
            pismeno = pismena[aktualni_start + posun]
            vysledek = vysledek + pismeno
            posun += 1
        yield vysledek
        posun = 0
        vysledek = ""
        aktualni_start += 1

for znaky in generator_pismenek(["A","C","E","R"],2):
    print(znaky)
'''
def gen(sekvence, delka): #Řešení od kolegy - geniální!
    for i in range(len(sekvence) - delka + 1):
        yield "".join(sekvence[i:i + delka])


for segment in gen(["A","C","E","R"], 2):
    print(segment)
for segment in gen(["A","C","E","R"], 3):
    print(segment)