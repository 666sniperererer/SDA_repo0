#Navigace v programu (aby se nevykonával vždy celý program, ale jen ta sekce, kterou zrovna chci(
    #Dvojice funkcí, první patří nahoru v souboru a zeptá se na sekci (číslo) kam v programu skočit
    #Druhá patří vždy na začátek sekce vykonavatelného kódu, kam ta první nasměruje

def vyber_sekce():
    global cislosekce
    cislosekce = int(input("Na jakou sekci chceš skočit? Napiš číslo: "))
    return cislosekce

def spust_tuto_sekci(tatosekce): #Tato funkce vyhodí spustit = true pokud se tato sekce má spustit
    spustit = cislosekce == int(tatosekce)
    return spustit

#cislosekce = vyber_sekce()
vyber_sekce()

#1
if spust_tuto_sekci(1):
    print("Sekce 1")
#2
if spust_tuto_sekci(2):
    print("Sekce 2")
#3
if spust_tuto_sekci(3):
    print("Sekce 3")