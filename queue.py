class Queue:
    def __init__(self):
        self.__items = []

    # TODO: vloz prvek do fronty
    def insert_item(self, item):
        # self.__items.insert(0,item)
        self.__items.append(item)

    # TODO: odeber prvek z fronty
    def delete(self):
        return self.__items.pop(0)

    # TODO: vypis prvek z fronty, ktery je na rade, ale neodebirej, pouze precti
    def peek(self):
        return self.__items[0]

    # TODO: zkontroluj jestli je fronta prazdny
    def is_empty(self) -> bool:
        return len(self.__items) == 0

    # TODO: vrat pocet prvku ve fronte
    def size(self) -> int:
        return len(self.__items)

    def __str__(self):
        return str(self.__items)


my_quee = Queue()

my_quee.insert_item(1)
my_quee.insert_item(4)
my_quee.insert_item(5)
my_quee.insert_item(6)
print(my_quee)
print(my_quee.peek())
print(my_quee.size())
my_quee.insert_item(6)
print(my_quee)
print(my_quee.peek())
print(my_quee.size())
print(my_quee.delete())

print(my_quee)