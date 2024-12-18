class Zvire(): #třídy pojmenováváme s velkým písmenem na začátku
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
        self.krmeno = False

    def vypis_zvire(self):
        if self.krmeno:
            print(f"Jméno: {self.jmeno} má {self.vek} let. A dnes bylo krmeno.")
        else:
            print(f"Jméno: {self.jmeno} má {self.vek} let. Potřeba nakrmit.")

vice_zvirat = []

vlk = Zvire("Vlk", 33)
vlk.vypis_zvire()
vice_zvirat.append(vlk)

zirafa = Zvire("Zirafa", 22)
zirafa.vypis_zvire()
vice_zvirat.append(zirafa)

print(vice_zvirat)
print(vice_zvirat[0].vypis_zvire())
print(vice_zvirat[1].vypis_zvire())