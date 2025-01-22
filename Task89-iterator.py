class NaVelkeZnaky:
    def __init__(self, seznam_jmen):
        self.u_jakeho_jsme_jmena = -1
        self.seznam_jmen = seznam_jmen
        self.kolik_mame_jmen = len(self.seznam_jmen)

    def __iter__(self):
        return self

    def __next__(self):
        self.u_jakeho_jsme_jmena += 1
        if self.u_jakeho_jsme_jmena == self.kolik_mame_jmen:
            raise StopIteration
        return self.seznam_jmen[self.u_jakeho_jsme_jmena].capitalize()

for velke in NaVelkeZnaky(["alice", "bety", "cecilie", "dan", "evzen"]):
    print(velke) #Alice, Bety, Cecilie,...