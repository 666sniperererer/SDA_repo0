from xml.sax.handler import property_interning_dict

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
    class Tovarna:
        def __init__(self, nazev):
            self.nazev = nazev
            self.pocet_zamestnancu = 0
            self.knowhow = []

        def nastavit_pocet_zamestnancu(self, novy_pocet):
            if novy_pocet < 0:
                print("Toto není možné, přiřazení nevykonám")
            else:
                self.pocet_zamestnancu = novy_pocet

        def pridat_HR_oddeleni(self):
            self.pocet_zamestnancu += 4

        def pridat_smenu(self):
            self.pocet_zamestnancu += 30

        def vymenit_knownow(self, jina_tovarna):
            self.knowhow.extend(jina_tovarna.knowhow)
            pass


    rolex = Tovarna("Rolex")
    rolex.nastavit_pocet_zamestnancu(40)
    rolex.pridat_HR_oddeleni()
    rolex.pridat_smenu()
    rolex.pridat_smenu()
    rolex.knowhow.append("cistota")
    print(f"Továrna na {rolex.nazev} má {rolex.pocet_zamestnancu} zaměstnanců")
    ikea = Tovarna("Ikea")
    ikea.pridat_smenu()
    ikea.knowhow.append("preciznost")
    rolex.vymenit_knownow(ikea)
    print(f"Továrna {rolex.nazev} má knowhow {rolex.knowhow}")

#Task_57_banka
if spust_tuto_sekci(57):
    class Banka:
        def __init__(self, jmeno, zustatek=0): #atribut jmeno a zustatek (poč. zůst = 0)
            self.jmeno = jmeno
            self.zustatek = zustatek

        def vklad(self, castka): #vložení částky zůstatku
            self.zustatek += castka


        def vyber(self, castka): #částka se odebere ze zůstatku
            if self.zustatek >= castka:
                self.zustatek -= castka
            else:
                print(f"Nelze vybrat {castka}, zůstatek je pouze {self.zustatek}")

        def print_info(self):
            print(f"Zůstatek v Bance {self.jmeno} je {self.zustatek}")

        def __repr__(self):
            return f"Zůstatek na účtu {self.jmeno} je {self.zustatek},-"

    #Vytvořte instanci třídy Banka

    airbank = Banka("Airbank")
    airbank.print_info()

    #Vložte 20000
    airbank.vklad(20000)
    #Vyberte 4000
    airbank.vyber(4000)
    #Print zůstatek a jméno
    airbank.print_info()
    print(airbank.jmeno, airbank.zustatek)
    airbank.vyber(17000)

    print(airbank)

#Task_58-obchod
if spust_tuto_sekci(58):
    class Polozka:
        def __init__(self, nazev, cena):
            self.nazev = nazev
            self.cena = cena

    class Kosik:
        def __init__(self):
            self.polozky = []

        def pridat_polozku(self, iteeem : Polozka):
            self.polozky.append(iteeem)
            print(f"Přidali jste item {iteeem.nazev} s cenou {iteeem.cena } do košíku")

        def vypsat_polozky(self):
            celkova_cena = 0
            print("V košíku je ", end='')
            pocty_polozek = {}
            for item in self.polozky:
                print(f"{item.nazev}, ", end='')
                celkova_cena += item.cena
                if item.nazev in pocty_polozek:
                    pocty_polozek[item.nazev] += 1 # pokud položka již v dict je
                else:
                    pocty_polozek[item.nazev] = 1 # pokud položka ještě v dict není


            print(f"Celková cena je {celkova_cena}")
            print(f"Celkový počet položek je {len(self.polozky)}")
            for key, value in pocty_polozek.items():
                print(f"Položka {key} je v košíku {value}x krát")

maslo = Polozka("Máslo", 80)
chipsy = Polozka("Chilli&Lime", 34)
propiska = Polozka("Propiska", 45)

katka = Kosik()
katka.pridat_polozku(maslo)
katka.pridat_polozku(chipsy)
katka.pridat_polozku(chipsy)
katka.vypsat_polozky() #V košíku je Máslo, Chlli, Chilli. Celková cena 148 Kč
#Extra - v košíku je 1x Máslo, 2x Chilli...

pavel = Kosik()
pavel.pridat_polozku(propiska)
pavel.pridat_polozku(maslo)
pavel.pridat_polozku(chipsy)
pavel.vypsat_polozky() #V košíku je Propiska, Máslo, Chilli. Celková cena 159 Kč

#Extra - v košíku je 1x Máslo, 2x Chilli...