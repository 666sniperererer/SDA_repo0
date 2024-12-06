#text = input("Zadej text: ")
#print(text[4]) #zobrazí znak na indexu 4
#print(text[2:4]) #zobrazí znaky mezi indexy 2 a 3 (nezobrazí 4)
#print(text[2:4:2]) #zobrazí každý druhý znak mezi indexy 2 a 3 (nezobrazí 4)
#print(text[-1]) #obracení řetězce (zobrazí znaky v opačném pořadí)


#Task 11
text = "Pomocí speciálního příkazu s operátorem [] můžeme řetězec přečíst od konce?"
print(f"V textu {text} je znak s tolikrát: {text.count("s")}")
print(f"V textu {text} jsou mezi indexy 7 a 14 znaky {text[7:15]}")
print(f"V textu {text} je na indexu 4 znak {text[4]}")
print(f"V textu {text} je slovo operátorem vytaženo {text[29:40]}")
print(f"V textu {text} je každý druhý znak {text[::2]}")
print(f"V textu {text} je vypsaný naopak {text[::-1]}")

#hledej začátek slova "operátorem"
cohledam = "operátorem"
delkaslova = len(cohledam)
kdezacina = text.index(cohledam)
print(cohledam)
print(delkaslova)
print(kdezacina)

print(f"V textu {text} je slovo operátorem vytaženo: {text[kdezacina:kdezacina+delkaslova]}")

#Task 12
retezec_t12_0 = "qsxht!trfecdtcbgřáýčerdxdpsěš d21rřcřetčěpe**u?rsS"
retezec_t12_1 = retezec_t12_0[5:99]
retezec_t12_2 = retezec_t12_1[::-1]
retezec_t12_final = retezec_t12_2[::4]
print(retezec_t12_final)

print(retezec_t12_final.upper()) #vše velkými
print(retezec_t12_final.lower()) #vše malými
print(retezec_t12_final.lower()[:10]) #vše malými, jen do desátého indexu

slozenina = retezec_t12_final.lower()[:5] + retezec_t12_final.upper()[5:]
print(slozenina)

#Task 13
'''
text_t13 = input("Zadej text: ")
vsemale = text_t13 == text_t13.lower()
vsevelke = text_t13 == text_t13.upper()
print(f"Je text {text_t13} celý malými znaky? Odpověď: {vsemale}")
print(f"Je text {text_t13} celý velkými znaky? Odpověď: {vsevelke}")
'''

#Task 14
seznam_t14 = []
seznam_t14.append("Honza")
print(seznam_t14)
seznam_t14.append("Pavel")
seznam_t14.append("Jan")
seznam_t14.append("Executor")
print(f"Celý seznam seznam_t14 má obsah: {seznam_t14}")
print(f"První prvek v seznamu, tedy na indexu 0, je: {seznam_t14[0]}")
print(f"Třetí prvek v seznamu, tedy na indexu 2, je: {seznam_t14[2]}")
seznam_t14.extend(["Barbar","Conan","Strejda","Skrblík"])
print(f"Celý seznam seznam_t14 má obsah: {seznam_t14}")
#Program se postupně bude ptát na texty
#všechny texty přidáte do listu
#vypíšete celý list naráz
#vypíšete prvek na indexu 0
#vypíšete prvek na indexu 1
#vypíšete prvek na indexu 2

#Task 14 (stále)
novyseznam_t14 = []
novyseznam_t14.append(input("Zadej první prvek seznamu: "))
novyseznam_t14.append(input("Zadej druhý prvek seznamu: "))
novyseznam_t14.append(input("Zadej třetí prvek seznamu: "))
print(f"Celý seznam novyseznam_t14 má obsah: {novyseznam_t14}")
print(f"První prvek novyseznam_t14 má obsah: {novyseznam_t14[0]}")
print(f"Druhý prvek novyseznam_t14 má obsah: {novyseznam_t14[1]}")
print(f"Třetí prvek novyseznam_t14 má obsah: {novyseznam_t14[2]}")