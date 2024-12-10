#Množina (set)
#   Neindexovatelná a neuspořádaná kolekce.
#   Zapisuje se pomocí znaků {}.
#   Prázdná množina se vytvoří pomocí příkazu set().
#   Hodnoty sady se neopakují.
#   K prvkům není přístup, prvky množiny nemají indexy.

# Create a set
animals = {"dog", "cat", "elephant"}

# Add a new item
animals.add("mouse")

# Add several items at once
animals.update(["bird", "horse"])

# Add the same item again
animals.add("mouse")
print(animals)

# Remove an item, Python will throw an error if it is not in the set
animals.remove("cat")

# Remove an item, Python will NOT throw an error if it is not in the set
animals.discard("cat")

seznam_zvirat_jako_list = ["myš", "myš", "myš", "potkan", "myš"]
print(seznam_zvirat_jako_list) #v listu je možné mít hodnotu vícekrát

seznam_zvirat_jako_set = set(["myš", "myš", "myš", "potkan", "myš"])
print(seznam_zvirat_jako_set) #v množině je každá hodnota unikátní