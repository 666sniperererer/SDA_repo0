from importlib.metadata import pass_none

import example_45_46_47
from example_45_46_47 import soucet_nasobek_podil
from pomocne_funkce_0 import spust_tuto_sekci

#soucet_nasobek_podil(50,45)

# Definition of the function named print_hello_world
def print_hello_world():
    print("Hello world from inside the function!")


# Calling print_hello_world()
#print_hello_world()

# Function definition of greet_by_name (name)
def greet_by_name(name):
    print(f"Hello, {name}")


# Call function greet_by_name (name) with "John" as the name argument
#greet_by_name("John")

# Function for printing the name and surname
def print_full_name(name, surname):
    print(f"{name} {surname}")


# Calling a function without specifying thr parameter names
#print_full_name("Jon", "Snow")

# Function call with names of all parameters
#print_full_name(name="Jon", surname="Snow")

# Calling the function with the names of the last parameter
#print_full_name("Jon", surname="Snow")

#Task/Example 48
print_hello_world()
print_hello_world()
greet_by_name("John")
greet_by_name("Albert")
print_full_name("Jon", "Snow")
print_full_name("Stanis", "Baratheon")

greet_by_name("Lenka")
greet_by_name("František")
print_full_name("Karel", "Gott")
print_full_name("Leona", "Macháčková")
print_hello_world()
print_full_name("Patricie", "Stavová")

#Extra Task 5
def ukaz_vetsi_cislo(vstup1,vstup2):
    if vstup1 > vstup2:
        print(vstup1)
    else:
        print(vstup2)

ukaz_vetsi_cislo(51,50)

#Extra Task 5 - s pojmenovanými parametry
def ukaz_vetsi_cislo(vstup1=5,vstup2=3):
    if vstup1 > vstup2:
        print(vstup1)
    else:
        print(vstup2)
#výsledek všech pěti variant níže bude stejný (vstup1 a vstup2 jsou pojmenované parametry)
ukaz_vetsi_cislo()
ukaz_vetsi_cislo(5)
ukaz_vetsi_cislo(vstup2=3)
ukaz_vetsi_cislo(5,3)
ukaz_vetsi_cislo(5,vstup2=3)

#Funkce - návratová hodnoty
def calculate_square(a):
    return a * a


square = calculate_square(5)
print(square)  # Prints 25

#Funkce s libovolným počtem pozičních argumentů
def nekonecny_soucet(*args):
    suma = 0
    for n in args:
        suma += n
    return suma

soucet = nekonecny_soucet(1,3,5,7,9,33,654)
print(soucet)

#Task_51
#Vynasob list
#Varianta 1

def vynasob_list(cislo_listu, nasobitel=3):
    vysledek = []
    for cislo in cislo_listu:
        vysledek.append(cislo * nasobitel)
    return vysledek

print(vynasob_list([3,4,1,2])) #[9,12,3,6] - 3x
print(vynasob_list([1,4,1,2])) #[3,12,3,6] - 3x
print(vynasob_list([1,4,1,2],2)) #[2,8,2,4] - 2x

#Varianta2
def vynasob_list2(data, nasobek=3):
    for index, cislo in enumerate(data):
        data[index] = cislo*nasobek
    return data

print(vynasob_list2([3,4,1,2])) #[9,12,3,6] - 3x
print(vynasob_list2([1,4,1,2])) #[3,12,3,6] - 3x
print(vynasob_list2([1,4,1,2],2)) #[2,8,2,4] - 2x



def pocet_parametru(*args):
    print(f"Parametry jsou tyto: {args}")
    if len(args) == 0:
        return f"Zde je {len(args)} parametrů"
    if len(args) == 1:
        return f"Zde je {len(args)} parametr"
    if len(args) in range(2,4):
        return f"Zde jsou {len(args)} parametry"
    if len(args) > 4:
        return f"Zde je {len(args)} parametrů"

print(pocet_parametru()) #0 parametrů
print(pocet_parametru(2)) #1 parametr
print(pocet_parametru(2,3)) #2 parametry
print(pocet_parametru(2,3,4)) #3 parametry
print(pocet_parametru(2,3,4,2,2)) #5 parametrů !!! Pozor, musí to být česky


#Funkce s libovolným počtem pojmenovaných argumentů (**kwargs)
# Add any number of ingredients
def add_ingredients(**kwargs):
    print(kwargs)
    for key, value in kwargs.items(): #procházení klíčů i hodnot
        print(f"Ingredience {key} jsou v tomto počtu: {value} ")
    for klic, hodnota in kwargs.items(): #procházení klíčů i hodnot = můžeme pojmenovávat jak chceme!
        print(f"Ingredience {klic} jsou v tomto počtu: {hodnota} ")
    result = 0
    for key in kwargs:
        result += kwargs[key]
    return result


print(add_ingredients(eggs=3, spam=5, cheese=2))  # Will print 10
print(add_ingredients(prvnisada=10, druhasada=7, tretisada=20))  # Will print 37