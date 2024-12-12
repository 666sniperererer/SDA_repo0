def soucet_nasobek_podil (cislo1, cislo2):
    soucet = cislo2 + cislo1
    nasobek = cislo2 * cislo1
    podil = cislo1 / cislo2
    print(f"Číslo {cislo1} + {cislo2} = {soucet}")
    print(f"Číslo {cislo1} * {cislo2} = {nasobek}")
    print(f"Číslo {cislo1} % {cislo2} = {podil:.3f}")

if '___main___' in __name__:
    soucet_nasobek_podil(7,89)
    soucet_nasobek_podil(9,3)
    soucet_nasobek_podil(80,5)