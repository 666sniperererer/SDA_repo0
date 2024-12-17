import random

#Vygenerujte čísla 'a' a 'b', které jsou 0-100
a = random.randint(0,100)
b =  random.randint(0,100)
#Ve while cyklu se uživatele ptejte, kolik je a//b. Pokud uživatel odpoví chybně, pak se cyklus vykoná znovu.
#tzn. dokud uživatel nevyřeší úlohu správně, tak program neskončí

spravne = False
while spravne == False:
    odpoved = int(input(f"Kolik je {a}//{b}? Napiš: " ))
    if odpoved == a // b:
        spravne = True
