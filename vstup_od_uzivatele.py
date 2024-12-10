#argumenty z příkazové řádky
import sys

'''
print(f"Spouštíme program: {sys.argv[0]}")
print(f"První argument z příkazové řádky: {sys.argv[1]}")
print(f"Druhý argument z příkazové řádky: {sys.argv[2]}")
print(f"Součet argumentů je: {int(sys.argv[1])+int(sys.argv[2])}") #musíme změnit na integer, originál je str
print(type(sys.argv[0]))
print(type(sys.argv[1]))
print(type(sys.argv[2]))
'''

#Task 29 (example)
#print(f"Spouštíme program: {sys.argv[0]}")
#print(f"První argument z příkazové řádky: {sys.argv[1]}")
#print(f"Druhý argument z příkazové řádky: {sys.argv[2]}")
#print(f"Třetí argument z příkazové řádky: {sys.argv[3]}")

print({sys.argv[1],sys.argv[2],sys.argv[3]})

film1 = sys.argv[1]
film2 = sys.argv[2]
film3 = sys.argv[3]

#nebo filmy = set(sys.argv[1:]) - libovolný počet argumentů

setfilmu = set([film1 , film2 , film3])
print(sys.argv)
print(setfilmu)