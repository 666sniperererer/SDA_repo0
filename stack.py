class Stack:
    def __init__(self):
        self.__items = []

    # vloz prvek do zsobniku
    def push(self, item):
        self.__items.append(item)

    # vrat prvek ze zasobniku
    def stack_pop(self):
        return self.__items.pop()

    # vypis horni prvek ze zasobniku, ale neodebirej, pouze precti
    def peek(self):
        return self.__items[-1]

    # zkontroluj jestli je zasobnik prazdny
    def is_empty(self) -> bool:
        return len(self.__items) == 0

    # vrat pocet prvku v zasobniku
    def size(self) -> int:
        return len(self.__items)

    def __str__(self):
        return str(self.__items)
'''

my_stack = Stack()
print(my_stack.is_empty())
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print(my_stack.is_empty())
print(my_stack)
print(my_stack.peek())
print(my_stack.size())
my_stack.push(6)
print(my_stack)
print(my_stack.peek())
print(my_stack.size())
print(my_stack.stack_pop())
print(my_stack)

'''
'''
#TODO: vytvorte funkci, ktera s pouzitim zasobniku overi validitu zavorek "({["
def are_parenthesis_valid(string: str) -> bool:
    result = False
    valid_pairs = {")":"(",
                   "]":"[",
                   "}":"{"}
    open_parenthesis = Stack()
    for char in string:
        if char in valid_pairs.values():
            open_parenthesis.push(char)
        if char in valid_pairs.keys():
            if open_parenthesis.size() > 0:
                result = valid_pairs.get(char) == open_parenthesis.stack_pop()
            elif open_parenthesis.size() == 0:
                result = False
    return result #neověřuji, jestli je stack prázdný - nejsou podchycené všechny varianty!

input = "())"  #False
input0 = "({})" #True
input1 = "({({}[])[]})" #True
input2 = "({({}[])[})" #False
# ------------------------ Level 2 -------------------
input3 = "(8*5{8({3+8}-[5-8])+[9*0]})" #True
input4 = "(8*5{8({3+8-[5-8])+[9*0]})" #False
input5 = "(8*5{8(3+8}-[5-8])+[9*0]})" #False

print(are_parenthesis_valid(input))
print(are_parenthesis_valid(input0))
print(are_parenthesis_valid(input1))
print(are_parenthesis_valid(input2))
print(are_parenthesis_valid(input3))
print(are_parenthesis_valid(input4))
print(are_parenthesis_valid(input5))