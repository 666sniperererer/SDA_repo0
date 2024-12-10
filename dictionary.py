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
print(telefonni_seznam2.get("OSSZ",{}).get("Odbor_zábavy","Neexistuje")) #víceúrovňový zápis
print(telefonni_seznam2.get("OSSZ",{}).get("Odbor_ktery_neexistuje","Neexistuje")) #víceúrovňový zápis

del telefonni_seznam2["Velký_množinář"] #odstranění záznamu

#Task 25
data = {
    "Albus": "Brumbál",
    "Alice": {
        "age": 29,
        "hobbies": ["reading", "cycling", "gardening"],
        "contacts": {
            "email": "alice@example.com",
            "phone": "555-1234"
        }
    },
    "Bob": {
        "age": 34,
        "hobbies": ["hiking", "chess", "coding"],
        "contacts": {
            "email": "bob@example.com",
            "phone": "555-5678"
        }
    },
    "Charlie": {
        "age": 25,
        "hobbies": ["photography", "traveling", "music"],
        "contacts": {
            "email": "charlie@example.com",
            "phone": "555-9101"
        }
    },
}

print(f"Získejte hodnotu 25: {data['Charlie']['age']}")
print(f"Získejte hodnotu Brumbál: {data['Albus']}")
print(f"Získejte hodnotu 555-1234: {data['Alice']['contacts']['phone']}")
print(f"Získejte hodnotu reading: {data['Alice']['hobbies'][0]}")
print(f"Získejte hodnotu traveling: {data['Charlie']['hobbies'][1]}")
print(f"Získejte hodnotu bob@example.com: {data['Bob']['contacts']['email']}")
print(f"Získejte hodnotu 29: {data['Alice']['age']}")

#Task 26
contacts = {
    "Alice": {"email": "alice@example.com", "phone": "555-1234"},
    "Bob": {"email": "bob@example.com", "phone": "555-5678"},
    "Charlie": {"email": "charlie@example.com", "phone": "555-9101"},
    "Diana": {"email": "diana@example.com", "phone": "555-3456"}
}
#pomocí .get() získejte telefon na Charlieho. Pokud telefon neexistuje, vypište
#'Číslo není v záznamu'

charlie_telefon = contacts.get("Charlie", {}).get("phone","Číslo není v záznamu")
print(charlie_telefon)

#smažte "Charlie" z kontaktů
del contacts["Charlie"]
print(contacts)

#použijte úplně stejný kód jako na řádku 9 (77). Program nesmí vypsat chybu

#Dianě smažte telefon, ale email jí ponechejte
#del contacts["Diana"]["phone"] #možnost 1
#del contacts.get("Diana")["phone"] #možnost 2
#contacts.get("Diana").pop("phone") #možnost 3
smazany_telefon = contacts["Diana"].pop("phone") #možnost 4

print(contacts)
print(smazany_telefon)