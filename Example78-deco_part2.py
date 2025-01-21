def print_pri_spusteni(fnc):
    def upozorneni():
        print(f"Spouštím dvakrát funkci {fnc.__name__}")
        fnc()
        print(f"Dokončeno spouštění funkce {fnc.__name__}")
    return upozorneni

@print_pri_spusteni
def nihao():
    print("Nihao")

@print_pri_spusteni
def ahoj():
    print("Zdravím")

@print_pri_spusteni
def guten():
    print("Guten TAG!!")

guten()
nihao()