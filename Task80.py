import time
#start = time.time()
#time.sleep(1.2)
#end = time.time()
#print(f"Rozdíl mezi end a start je {(end-start):.2f} sekund")

def print_pred_a_za(fnc):

    def nahradni_funkce(nasobitel):
        #print("Jdeme vykonat funkci")
        start = time.time()
        fnc(nasobitel)
        end = time.time()
        print(f"Funkce trvala {(end - start):.2f} sekund")
        #print("Funkce vykonána")

    return nahradni_funkce

@print_pred_a_za
def zadej_cislo(nasobitel):
    vstup = int(input("Zadej číslo:"))
    #nasobitel = int(input("Zadej násobitel:"))
    print(f"Číslo {vstup} vynásobeno číslem {nasobitel} je {vstup * nasobitel}")


zadej_cislo(223)

# řešení od Alberta:
#Task - udělat dekorátor, který vypíše, jak dlouho funkce trvala.
import time
def print_pred_a_za(fnc):

    def nahradni_fukce(*args, **kwargs):
        print("Jdeme vykonat funkci")
        start = time.time()  # zaznamená aktuální čas v době vykonání řádku
        navratova_hodnota = fnc(*args, **kwargs)
        end = time.time()  # zaznamená aktuální čas v době vykonání řádku
        print(f"Funkce vykonána během {end - start:.2f} sekund")
        return navratova_hodnota

    return nahradni_fukce

@print_pred_a_za
def zadej_cislo(cislo):
    vstup = int(input("Zadej číslo:"))
    print(f"Dvojnásobek čísla {vstup} je {vstup * cislo}")

zadej_cislo(5)
