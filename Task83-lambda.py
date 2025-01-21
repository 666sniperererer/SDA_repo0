lide = ["Ruda", "Petr", "Pavla", "Petra"]

def porovnej_delku_jmen(jmeno1, jmeno2):
    return len(jmeno1) > len(jmeno2)

print(porovnej_delku_jmen(lide[2], lide[1]))

#Zde napište lambda funkci která udělá to samé( porovnej_delku_jmen)
porovnani_lambda = lambda jmeno1, jmeno2: len(jmeno1) > len(jmeno2)
print(porovnani_lambda(lide[2], lide[1]))

#---------------------------

def jsou_indexy_stejne(list_polozek):
    return list_polozek[2] == list_polozek[3]

print(jsou_indexy_stejne(lide))
#zde napište lambda funkci která udělá to samé( jsou_indexy_stejne)
jsou_index_stejne_lambda = lambda list_polozek: list_polozek[2] == list_polozek[3]
print(jsou_index_stejne_lambda(lide))