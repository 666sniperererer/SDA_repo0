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
text_t13 = input("Zadej text: ")
vsemale = text_t13 == text_t13.lower()
vsevelke = text_t13 == text_t13.upper()
print(f"Je text {text_t13} celý malými znaky? Odpověď: {vsemale}")
print(f"Je text {text_t13} celý velkými znaky? Odpověď: {vsevelke}")