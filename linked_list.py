class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print_node(self):
        if self.next is None:
            print(f"NODE - hodnota je {self.value} a ukazatel je 'None'")
        else:
            print(f"NODE - hodnota je {self.value} a ukazatel ukaze ja node s cislem {self.next.value}")

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def list_add_to_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def list_add_to_front(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_on_index(self, index, value):
        new_node = Node(value)
        current_node = self.head

        for _ in range(index - 1):
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node


    def remove_on_index(self, index):
        current_node = self.head

        for _ in range(index - 1):
            current_node = current_node.next

        current_node.next = current_node.next.next

    def node_count(self):
        counter = 0
        current_counted_node = self.head

        if self.head != None:
            while current_counted_node != self.tail:
                counter += 1
                current_counted_node = current_counted_node.next
            else:
                counter += 1

        return int(counter)

    # TODO: napist metodu ktera najde prvni prvek (vrati index) obsahujici danou hodnotu v linkovanem seznamu
    def find_value(self, value):

        if self.head != None:
            actual_index = 0
            current_counted_node = self.head
            while actual_index + 1 <= self.node_count():
                if value != current_counted_node.value:
                    current_counted_node = current_counted_node.next
                    actual_index += 1
                else:
                    return(f"Hodnota {value} nalezena v Node s indexem {actual_index}")
            else:
                return("Tato hodnota v linked listu není.")


    # TODO: uprav funkci print values tak aby vypsala vsechny prvky, ktere jsou v seznamu
    def print_values(self):

        if self.head is None:
            print("List je prazdny - Hodnota head i tail je 'None'")

        else:
            current_node = self.head
            all_nodes = [current_node.value]
            while current_node != self.tail:
                current_node = current_node.next
                all_nodes.append(current_node.value)
            print(all_nodes)





linked_list0 = LinkedList()
linked_list0.print_values()
print()

linked_list0.list_add_to_end(1)
linked_list0.print_values()
print()

linked_list0.list_add_to_end(2)
linked_list0.print_values()
linked_list0.head.next.print_node()
print()

linked_list0.list_add_to_end(2)
linked_list0.print_values()
linked_list0.head.next.print_node()
print()


linked_list0.list_add_to_end(3)
linked_list0.print_values()
linked_list0.head.next.print_node()
print()

linked_list0.list_add_to_front(5)
linked_list0.print_values()
linked_list0.head.next.print_node()
linked_list0.head.next.next.print_node()

current_node0 = linked_list0.head

print(linked_list0.find_value(3))

print(linked_list0.node_count())
# print(linked_list0.print_values())