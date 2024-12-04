print("test GITu")

print("druhý řádek pro druhý commit")

print("třetí řádek pro třetí commit")

#formátování proměnných do stringu
jmeno = "Honza"
jmenotrikrat = jmeno+jmeno+jmeno
nick = "666sniperererer"
cislo = 2/3

print("Ahoj, mé jméno je {jmeno}") #chybí f, složené závorky jsou pouze text
print(f"Ahoj, mé jméno je {jmeno}") #na začátku je f, složené závorky fungují pro definici proměnné
print(f"Můj nick je {nick} a .2f formátované číslo 2/3 je {cislo:.2f}")
print(f"Můj nick je {nick} a .4f formátované číslo 2/3 je {cislo:.4f}")

print(jmenotrikrat)
print(jmeno==jmeno)
print(jmeno==jmenotrikrat)
print(6>7)
print(1>cislo)
print(cislo>1)