#.count(x) - vypočte počet výskytů v listu
seznam_jmen = ["Ó velký Já", "Honza", "Jan", "John", "Jean"]
print(f"V seznam_jmen je 'Jan' {seznam_jmen.count('Jan')}x krát")

#.index(x) - na jakém indexu je x
print(f"V seznam_jmen na jakém indexu je 'Jan'? Na indexu č. {seznam_jmen.index('Jan')}")

#.insert(index, x) - vložení x na daný index
seznam_jmen.insert(2, "Jantar")
print(seznam_jmen)

#.pop() - odstranění prvku z posledního místa v seznamu
odebrany_prvek = seznam_jmen.pop()
print(seznam_jmen)
print(f"Odebrali jsme prvek: {odebrany_prvek}")

#.pop(index) - odstranění prvku z daného indexu
odebrany_prvek2 = seznam_jmen.pop(0)
print(seznam_jmen)
print(f"Odebrali jsme prvek: {odebrany_prvek2}")

#.remove(x) - odebere první výskyt daného prvku ze seznamu
odebrany_prvek3 = seznam_jmen.remove("Jantar")
print(f"Výsledek po odebrání pomocí Jantar je {seznam_jmen}")
#print(f"Odebrali jsme prvek: {odebrany_prvek3}")

#.clear() - smaže celý obsahu seznamu
seznam_jmen.clear()
print(f"Výsledek po seznam_jmen.clear() je tento: {seznam_jmen}")

#.reverse() - otočíme list/seznam
seznam_jmen = ["Ó velký Já", "Honza", "Jan", "John", "Jean"]
print(f"Neotočený seznam_jmen je tento: {seznam_jmen}")
seznam_jmen.reverse()
print(f"Výsledek po seznam_jmen.reverse() je tento: {seznam_jmen}")
#alternativní zápis
seznam_jmen = seznam_jmen[::-1]
print(f"Výsledek po 'seznam_jmen = seznam_jmen[::-1]' je zase tento: {seznam_jmen}")

#.sort() - seřadí seznam, jak číselný tak textový
seznam_jmen.sort()
print(f"Výsledek po 'seznam_jmen.sort()' je tento: {seznam_jmen}")
seznam_jmen.sort(reverse=True)
print(f"Výsledek po 'seznam_jmen.sort(reverse=True)' je tento: {seznam_jmen}")
seznam_cisel = [5,3,9,11,45,131,55]
print(f"Seznam_cisel je tento: {seznam_cisel}")
seznam_cisel.sort()
print(f"Výsledek po 'seznam_cisel.sort()' je tento: {seznam_cisel}")
seznam_cisel.sort(reverse=True)
print(f"Výsledek po 'seznam_cisel.sort(reverse=True)' je tento: {seznam_cisel}")

#.append(x) - vloží daný jeden prvek na konec listu
seznam_jmen.append('Přidaný')
print(f"Výsledek po 'seznam_jmen.append('Přidaný')' je tento: {seznam_jmen}")

#.extend(x) - vloží list x jako jednotlivé prvky
seznam_cisel.extend([646,879,1])
print(f"Výsledek po 'seznam_cisel.extend[646,879,1]' je tento: {seznam_cisel}")

#Task 17
nested_list = [
    [1, 2, [3, 4, [5, 6, 5], 5], 5],
    [7, 8, [5, 9, 5,5]],
    [10, [11, 5, 6], 12]
]

#pomocí indexování zvolte pole [5, 6, 5]
#pozn. indexování je např. nested_list[2][0]

# pomocí .count zjistěte, kolikrát se vyskytuje 5 v tomto poli.

vysledek = nested_list[0][2][2].count(5)

assert vysledek == 2, "Chybný výsledek"
print("Gratuluji, správný výsledek")

#seznam_jmen.insert(2, "Jantar")

#Task 18
jmena = ["Jura", ["Eliška"], "Katka"] #Tento řádek neupravujte
#pomocí příkazu .insert() rozšiřte jmena, tak aby obsahovala:
# ["Jura", ["Eliška", "Ruda"], "Božka", "Katka", ["Michal", "Liza"]]
jmena[1].insert(1, "Ruda")
jmena.insert(2, "Božka")
jmena.insert(4, ["Michal","Liza"])
print(jmena)

#Task 19 pop
#   ŘÁDKY níže neupravujte
vsechny_jmena = ["Jura", ["Eliška", "Ruda"], "Božka", "Katka", ["Michal", "Liza"]]
assert jmena==vsechny_jmena, f"Chyba, vyšlo {jmena}, ale mělo vyjít {vsechny_jmena} "
print("Gratuluji")

#Task 19
vsechny_jmena = ["Jura", ["Eliška", "Ruda"], "Božka", "Katka", ["Michal", "Liza"]] #Tento řádek neupravujte
#pomocí příkazu .pop(index) odeberte vsechny_jmena, tak aby obsahovala pouze:
# ["Jura", ["Eliška"], "Katka"]
#k odstranění - Ruda, Božka, [Michal, Liza]
vsechny_jmena[1].pop(1) #Ruda
vsechny_jmena.pop(2) #Božka
vsechny_jmena.pop(3) #[Michal, Liza]

#Task 20
vsechny_jmena = ["Jura", ["Eliška", "Ruda"], "Božka", "Katka", ["Michal", "Liza"]] #Tento řádek neupravujte
#pomocí příkazu .remove(x) odeberte vsechny_jmena, tak aby obsahovala pouze:
# ["Jura", ["Eliška"], "Katka"]
#k odstranění - Ruda, Božka, [Michal, Liza]
vsechny_jmena[1].remove("Ruda") #Ruda
vsechny_jmena.remove("Božka") #Božka
vsechny_jmena.remove(["Michal", "Liza"]) #[Michal, Liza]

#   ŘÁDKY níže neupravujte
jmena = ["Jura", ["Eliška"], "Katka"]
assert jmena==vsechny_jmena, f"Chyba, vyšlo {vsechny_jmena}, ale mělo vyjít {jmena} "
print("Gratuluji")

#Task 21
vsechny_jmena = ["Jura", ["Eliška", "Ruda"], "Božka", "Katka", ["Michal", "Liza"]] #Tento řádek neupravujte
#pomocí příkazu .clean() promažte vnořené listy tak, aby vsechny_jmena obsahovala pouze:
# ["Jura", [], "Božka", "Katka", []]
vsechny_jmena[1].clear()
vsechny_jmena[4].clear()
print(vsechny_jmena)

#   ŘÁDKY níže neupravujte
jmena = ["Jura", [], "Božka", "Katka", []]
assert jmena==vsechny_jmena, f"Chyba, vyšlo {vsechny_jmena}, ale mělo vyjít {jmena} "
print("Gratuluji")

#Task 22
puvodni_list = [1,4,9,[5,2],6] #Nesahat na toto
# Použijte dva příkazy .reverse() tak ať dostanete: [6, [2, 5], 9, 4, 1]
puvodni_list.reverse()
puvodni_list[1].reverse()

#Na řádky níže nesahat
assert puvodni_list == [6, [2, 5], 9, 4, 1], f"Chyba, má vyjít [6, [2, 5], 9, 4, 1], ale vyšlo {puvodni_list}"
print("Správně!!")

#Task 23
sportka = [3,5,8,1] #Nesahat
#Použijte příkaz insert, sort, reverse a pop, a získejte [8, 4, 3, 1]
'''
sportka.pop(1)
sportka.insert(0, 4)
sportka.sort()
sportka.reverse()
'''
sportka.insert(0, 4)
sportka.sort()
sportka.reverse()
sportka.pop(1)
print(sportka)

assert [8, 4, 3, 1] == sportka, f"Má vyjít [8, 4, 3, 1] a vyšlo {sportka}"
print("Výhra!!!!")