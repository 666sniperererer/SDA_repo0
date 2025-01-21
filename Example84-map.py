jmena = ["Ruda", "Jura", "Petra", "Ivanovič"]

#Délky jmen pomocí map
delky = list(  map(lambda x: len(x),jmena)  )
print(delky)
#Délky jmen pomocí map
for delka in map(lambda x: len(x), jmena ):
    print(f"Prvek má delku {delka}")

#Délky jmen pomocí map
def ziskej_delku(jmeno):
    return len(jmeno)

for delka in map(ziskej_delku, jmena ):
    print(f"Prvek má delku {delka}")

#Vynásobení deseti pomocí map
def vynasob_deseti(prvek):
    return prvek * 10

for novy_prvek in map(vynasob_deseti, [2,30,500]):
    print(novy_prvek)


nazvy = ["václavák", "Václavské náměstí", "Rudná", "žitava"]

#Ponechání pouze s velkým písmenem pomocí filter
print(   list(     filter(lambda nazev: nazev[0] == nazev[0].upper()  ,nazvy)       )      )

#Ponechat pouze delší než délky 6 pomocí filter
def je_delsi_nez_6(prvek):
    return len(prvek) > 6
print(   list(    filter(    je_delsi_nez_6   , nazvy)       )     )


#sečtení celého listu pomocí reduce
veky = [30,20,40,44]
from functools import reduce
def secti_dva_prvky(a,b):
    print(f"Sčítám {a} a {b}")
    return a + b
soucet = reduce(secti_dva_prvky, veky)
print(soucet)