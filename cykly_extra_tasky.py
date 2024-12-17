import random
nahodne_cislo = random.randint(0,100)

#K vyřešení následujících úloh stačí doposud naučené znalosti - tzn prezentace.
# Není potřeba používat knihovny či něco, co jsme se ještě neučili.


#Extra 1
#Opravdová pyramida: pro vstup 4 bude vypsána pyramida viz níže. Vyřešit pomocí cyklů...
'''
   #
  ###
 #####
#######

'''

vyska_pyramidy = int(input("Zadej výšku pyramidy: "))
radek = 0

while radek < vyska_pyramidy:
    sloupec = 1
    k_tisku = ""
    delka_radku = vyska_pyramidy + radek
    while sloupec < vyska_pyramidy - radek: #přidáme mezery
        k_tisku += " "
        sloupec += 1
    while sloupec <= delka_radku: #přidáme hashtagy
        k_tisku += "#"
        sloupec += 1
    print(k_tisku)
    radek += 1

#Extra 2
#Diamant: pro vstup 4 bude vypsán diamant viz níže Vyřešit pomocí cyklů...
'''
   #
  ###
 #####
#######
 #####
  ###
   #
'''

velikost_diamantu = int(input("Zadej velikost diamantu: "))
radek = 0
vyska_diamantu = (velikost_diamantu * 2) - 1

while radek < vyska_diamantu: #cyklím dokud nejsem na
    while radek < velikost_diamantu:
        sloupec = 1
        k_tisku = ""
        delka_radku = velikost_diamantu + radek
        while sloupec < velikost_diamantu - radek: #přidáme mezery
            k_tisku += " "
            sloupec += 1
        while sloupec <= delka_radku: #přidáme hashtagy
            k_tisku += "#"
            sloupec += 1
        print(k_tisku)
        radek += 1
    else:
        sloupec = 1
        k_tisku = ""
        delka_radku = velikost_diamantu + (vyska_diamantu - radek)
        while sloupec < velikost_diamantu - (vyska_diamantu - radek - 1): #přidáme mezery
            k_tisku += " "
            sloupec += 1
        while sloupec <= delka_radku - 1: #přidáme hashtagy
            k_tisku += "#"
            sloupec += 1
        print(k_tisku)
        radek += 1

#Extra 3 - obrácená tipovačka.
# Myslete si v hlavě číslo. Počítač postupně tipuje.
# Počítač vždycky napíše číslo co tipl a vy odpovíte "vetsi", "mensi" nebo "trefa"
# př:
# Počítač "tipne" číslo 50.
# Pokud napisete 'vetsi' tak pocitac tipne 75.
# Pokud pak napisete 'nizsi', tak pocitac tipne 63
# Pokud pak napisete 'vetsi' tak pocitac tipne cislo mezi 75 a 63 tzn.. 69


spodniinterval = 0
horniinterval = 100
tip_pocitace = random.randint(spodniinterval,horniinterval)
odpoved = ""

while odpoved != "trefa" and odpoved != "t":
    odpoved = input(f"Tipnul jsem číslo {tip_pocitace}, je skutečné číslo větší, menší, nebo trefa? ")
    if odpoved == "větší" or odpoved == "vetsi" or odpoved == "v":
        spodniinterval = tip_pocitace
        tip_pocitace = (tip_pocitace + horniinterval) // 2
        if tip_pocitace + 1 == horniinterval: #oprava cyklení při zaokrouhlení u 99/100 - nevím, jak jinak řešit
            horniinterval += 1

    if odpoved == "menší" or odpoved == "mensi" or odpoved == "m":
        horniinterval = tip_pocitace
        tip_pocitace = (spodniinterval + tip_pocitace) // 2

print(f"Super, takže sis myslel číslo {tip_pocitace}")



#Extra 4
#Program se zeptá jaký obrazec chceme vykreslit na jakou souřadnici.
#Podle zvoleného obrazce dodáme ještě parametry
#Možné obrazce:
# Čtverec - parametr je strana
# Obdélník - parametr je a, b
# Pyramida - parametr je velikost
# Diamant - parametr je velikost
# Kruh - parametr je r. Tip: umíme porovnávat a umíme mocnit pomocí ** . Pythagorova věta
# Dále se program zeptá, na jakou souřadnici budeme vykreslovat x a y
#Obrazec se vykreslí.




#Extra 4b.
#Vykreslování je cyklické. Po vykreslení jednoho obrazce se opakovaně program ptá co dalšího budeme vykreslovat.
#Tip - vykreslujeme do vícerozměrného pole
#Velikost plátna zadáme na vstupu

#