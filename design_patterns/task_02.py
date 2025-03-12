"""
Predstavte si scenár systému na objednávanie pizze, v ktorom si zákazníci môžu prispôsobiť pizzu výberom rôznych príloh,
a veľkosti pizze. Použite nástroj Pattern Builder a určitým spôsobom zapúzdrite dizajn pizze,
ktorý udržiava proces konštrukcie oddelený od reprezentácie, čo uľahčuje pridávanie nových možností bez úpravy existujúceho kódu.
"""

class Pizza:
    def __init__(self):
        self.topping: list
        self.dough = None
        self.size = None

    def __str__(self):
        return f"Pizza with {self.topping}, {self.dough} dough and size {self.size}."


class PizzaBuilder:
    def __init__(self):
        self._pizza = Pizza()

    def choose_dough(self, dough: str):
        self._pizza.dough = dough
        return self

    def choose_topping(self, topping: str):
        self._pizza.topping = topping
        return self

    def choose_size(self, size: int):
        self._pizza.size = size
        return self

    def build(self):
        if self._pizza.dough is None:
            print("Pizza without dough")

        if self._pizza.size is None:
            print("Size is not defined")

        return self._pizza

builder = PizzaBuilder()
pizza = builder.choose_dough("standard").choose_topping("tomato").choose_size(34).build()

print(pizza)

# skontrolujte ci ma pizza cesto a nejaku velkost

