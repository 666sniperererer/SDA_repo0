

class Knihovna:
    def __init__(self):
        self.vypujcena_kniha = 64 #64 = kniha A

    def __iter__(self):
        return self

    def __next__(self):
        self.vypujcena_kniha += 1
        if self.vypujcena_kniha == 91: #konec knihovny == 91 tzn.Z
            raise StopIteration
        print("Jdu do sklepa, pro knihu")
        return f"Půjčil sis knihu, která začíná na písmeno {chr(self.vypujcena_kniha)}"

for kniha in Knihovna():
    print(kniha)


class Autobazar:
    def __init__(self):
        self.u_jakeho_jsme_auta = 0
        self.auta = ["Škoda", "Audi", "BMW", "Bentley", "Porsche"]
        self.kolik_mame_aut = 5

    def __iter__(self):
        return self

    def __next__(self):
        if self.u_jakeho_jsme_auta >= self.kolik_mame_aut:
            raise StopIteration
        auto = self.auta[self.u_jakeho_jsme_auta]
        self.u_jakeho_jsme_auta += 1
        return auto

for auto in Autobazar():
    print(f"Stojím u auta {auto}")
