import pomocne_funkce_0
from pomocne_funkce_0 import vyber_sekce, spust_tuto_sekci

vyber_sekce()

#Example / Task 55 OOP
if spust_tuto_sekci(55):
    class Zamestnanec:
        def __init__(self, jmeno, prijmeni, plat):
            self.jmeno = jmeno
            self.prijmeni = prijmeni
            self.plat = plat

        def pridat_plat(self, o_kolik_zvysit):
            self.plat += o_kolik_zvysit

        def printit(self):
            print(f"Zaměstnanec {self.jmeno} příjmením {self.prijmeni} má plat {self.plat}")

        def zmen_jmeno(self, nove_jmeno):
            self.jmeno = nove_jmeno

    petr = Zamestnanec("Petr", "Novák", 60000)
    petr.pridat_plat(5000)
    petr.printit() #Zaměstnanec Petr příjmením Novák má plat 65000

    lenka = Zamestnanec("Lenka", "Nováková", 55000)
    lenka.pridat_plat(11000)
    lenka.printit() #Zaměstnanec Lenka příjmením Nováková má plat 66000

    petr.zmen_jmeno("Josef")
    petr.printit()

#Example 56
if spust_tuto_sekci(56):
    pass