#dictionary/slovník se tvoří pomocí složených závorek (list je pomocí hranatých)
telefonni_seznam = {}

#párujeme klíč (v hranaté závorce) s hodnotou, kterou přiřadíme
telefonni_seznam["Nostradamus"] = 453131646
telefonni_seznam["Věrný Pátek"] = 987456321

print(telefonni_seznam) #celý
print(telefonni_seznam["Věrný Pátek"]) #hodnota patřící ke klíči

#definice celého slovníku
telefonni_seznam2 = {
    "Honza": 525525131,
    "Jan": 897456123,
    "Texťák": "text, já mám text, o o ó",
    "Velký_množinář": [1,6,7,8,9,3],
    "OSSZ": {
        "Odbor_dopravy": 454313989,
        "Odbor_zábavy": 999666111
    }
}
print(telefonni_seznam2)
print(telefonni_seznam2["OSSZ"]["Odbor_zábavy"]) #když víme cestu
print(telefonni_seznam2.get("Odbor_zábavy", "Neexistuje")) #když nenajde první argument, vrátí druhý