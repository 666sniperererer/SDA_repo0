class Person:
    def __init__(self, name, age, height, gender):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender

    def __str__(self):
        return f'Name: {self.name} Age: {self.age} Height: {self.height} Gender: {self.gender}'

    def __repr__(self):
        return f'Name: {self.name} Age: {self.age} Height: {self.height} Gender: {self.gender}'

list_of_people = []

list_of_people.append(Person('Jan', 25, 160, 'Male'))
list_of_people.append(Person('Jindra', 15, 163, 'Male'))
list_of_people.append(Person('Tereza', 35, 172, 'Female'))
list_of_people.append(Person('Zikmund', 27, 198, 'Male'))
list_of_people.append(Person('Bohuta', 25, 155, 'Male'))
list_of_people.append(Person('Racek', 85, 169, 'Male'))
list_of_people.append(Person('Merkvart', 35, 179, 'Male'))

print(list_of_people)

for person in list_of_people:
    print(person)

# TODO: Upravte funkci bubble sort tak aby seradila osoby v seznamu podle veku nebo vysky
def bubble_sort_optimal(my_array):
    sort_by = int(input("Sort by: 1 - AGE, 2 - HEIGHT: "))
    n = len(my_array)
    if sort_by == 1:
        for i in range(n-1):
            swapped = False
            for j in range(n-1-i):
                if my_array[j].age > my_array[j+1].age:
                    my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
                    swapped = True
            if not swapped:
                break
    if sort_by == 2:
        for i in range(n-1):
            swapped = False
            for j in range(n-1-i):
                if my_array[j].height > my_array[j+1].height:
                    my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
                    swapped = True
            if not swapped:
                break

    return my_array

print("Sorted array:", bubble_sort_optimal(list_of_people))