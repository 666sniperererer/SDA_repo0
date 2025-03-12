"""
Task1 - SRP

Predstavte si systém pre malé internetové kníhkupectvo. Na začiatku je v kóde jedna trieda,
ktorá spracováva niekoľko úloh: správu zásob kníh, spracovanie predajných transakcií a generovanie správ o predaji.
Táto trieda porušuje princíp jedinej zodpovednosti, pretože má viac ako jeden dôvod na zmenu.

Prepracujte nasledujúcu triedu jazyka Python tak, aby dodržiavala princíp jedinej zodpovednosti.
Trieda v súčasnosti spracúva správu zásob, predajné transakcie a vytváranie správ,
ktoré by mali byť oddelené do samostatných tried.
"""


class BookStore:
    def __init__(self):
        self.inventory = {}
        self.sales = []

    def add_book(self, title, quantity):
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity

    def sell_book(self, title, quantity):
        if title in self.inventory and self.inventory[title] >= quantity:
            self.inventory[title] -= quantity
            self.sales.append((title, quantity))
        else:
            print("Book out of stock or not enough quantity.")

    def get_inventory(self):
        return self.inventory

    def get_sales_report(self):
        report = "Sales Report:\n"
        for sale in self.sales:
            report += f"Title: {sale[0]}, Quantity: {sale[1]}\n"
        return report


"""
V ideálnom prípade definujte samostatné triedy, ktoré budú
1 - starať sa o inventár (pridávanie, odstraňovanie)
2 - starať sa o proces predaja (predaj kníh, uchovávanie údajov o predaji).
3 - starať sa o vykazovanie predaja (generovanie prehľadu o predaji).
"""

class BookInventory:
    def __init__(self, name):
        self.name = name
        self.inventory = {"Score": 50}

    def add_book(self, title, quantity):
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity

    def remove_book(self, title, quantity):
        if title in self.inventory:
            self.inventory[title] -= quantity
        else:
            return None

    def get_inventory(self):
        return self.inventory

class BookSales:
    def __init__(self):
        self.sales = []

    @staticmethod
    def sell_book(BookInventory, title, quantity):
        if title in BookInventory.inventory and BookInventory.inventory[title] >= quantity:
            BookInventory.remove_book(title,quantity)
            BookSales.sales.append((title, quantity))
        else:
            print("Book out of stock or not enough quantity.")


class SalesReporting:

    @staticmethod
    def get_sales_report():
        report = "Sales Report:\n"
        for sale in BookSales.sales:
            report += f"Title: {sale[0]}, Quantity: {sale[1]}\n"
        return report

knihovna = BookInventory("Brno")
knihovna.add_book("Score", 10)
knihovna.add_book("Excalibur", 30)
print(knihovna.get_inventory())
BookSales.sell_book(knihovna, "Score", 20)