import example_45_46_47
from example_45_46_47 import soucet_nasobek_podil

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

