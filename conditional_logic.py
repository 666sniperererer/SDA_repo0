#IF, ELSE, a podobně

vek = 20
if vek > 17:
    print(f"Jsi dospělý, je Ti {vek}") #za IFem vykoná při splnění podmínky jen odsazené řádky

if vek < 18:
    print(f"Nejsi dospělý, je Ti {vek}")

vek2 = 16
if vek2 > 17:
    print(f"Jsi dospělý2, je Ti {vek2}")
else:
    print(f"Nejsi dospělý2, je Ti {vek2}")

if True:
    print("Toto se vykoná vždy")

if False:
    print("Toto se nikdy nevykoná")

vek3 = -8
if 98 >= vek3 > 17:
    print(f"Jsi dospělý2, je Ti {vek3}")
elif vek3 > 98:
    print(f"Ty jsi stařešina! Je Ti {vek3}")
elif vek3 < 0:
    print(f"To bude nějaká blbost. Tobě je {vek3}?")
else:
    print(f"Nejsi dospělý2, je Ti {vek3}")

#cislo = int("18")

#Task 31,32,33

cislotasku = int(input("Vlož číslo tasku k provedení: "))

if cislotasku == 31:
    vek4 = int(input("Zadej svůj věk: "))
    if vek4 < 12:
        print(f"Jsi dítě, je Ti {vek4}")
    elif 12 <= vek4 <= 18:
        print(f"Jsi teenager, je Ti {vek4}")
    elif 19 <= vek4 <= 59:
        print(f"Jsi dospělý, je Ti {vek4}")
    else:
        print(f"Jsi senior, je Ti {vek4}")

elif cislotasku == 32:
    znamka = int(input("Zadej známku: "))
    if znamka == 1:
        print("Výborně!")
    elif znamka == 2:
        print("Chvalitebně!")
    elif znamka == 3:
        print("Dobře!")
    elif znamka == 4:
        print("Dostatečně!")
    elif znamka == 5:
        print("Nedostatečně!")
    else:
        print("Taková známka neexistuje!")

elif cislotasku == 33:
    prijem = int(input("Zadej příjem firmy: "))
    if prijem > 0:
        print("Firma je v zisku")
    elif prijem == 0:
        print("Firma je na nule")
    else:
        print("Brzy bude krach!")
else:
    print("Vybral jsi task, který teď neřešíme.")

#Task 31
'''
Zadání:
Napiš program, který požádá uživatele o zadání věku.
Program zkontroluje a vypíše, do které věkové kategorie patří:

"Dítě", pokud je věk menší než 12 let,
"Teenager", pokud je věk od 12 do 18 let,
"Dospělý", pokud je věk od 19 do 59 let,
"Senior", pokud je věk 60 a více let.
'''

#Task 32
'''
Zadání:
Napiš program, který požádá uživatele o zadání čísla odpovídající známce (1 až 5). Program vypíše hodnocení:

1 = "Výborně"
2 = "Chvalitebně"
3 = "Dobře"
4 = "Dostatečně"
5 = "Nedostatečně"
Pokud uživatel zadá jiné číslo než 1–5, vypiš: "Neplatná známka".
'''

#Task 33
'''
Zadání:
Napiš program, který požádá uživatele o zadání čísla odpovídající přijmu firmy:

pokud je číslo kladné, tak se vypíše "Firma je v zisku"
pokud je číslo nula, tak se vypíše "Firma je na nule"
pokud je číslo záporné, tak se vypíše "Brzo bude krach"

'''