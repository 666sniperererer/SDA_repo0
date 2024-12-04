text = "Naše staré hodiny bijí čtyři hodiny"
print(text.index("e")) #na které pozici ve stringu je "e"?
print(text.index("čtyři")) #na které pozici ve stringu je "čtyři"?
#text.index má počáteční pozici 0

print(len(text)) #délka stringu
print(f'len(text) {len(text)}')

#Task 9 - vyhledání v textu
retezec = input("Vložte řetězec: ")
hledat = input("Co hledat: ")
print(f'retezec.index() {retezec.index(hledat)}')
print(f'len(retezec) {len(retezec)}')
x = len(retezec)
print(f"Hledal jsi v textu {retezec}, "
      f"\nten je dlouhý {x} znaků, "
      f"\nv něm jsi se snažil najít text {hledat}, "
      f"\na ten je na pozici {retezec.index(hledat)}")

#Task 10
# - uživatel vloží dva řetězce a program vypíše True pokud je první retězec delší.
# - pokud je druhý řetězec delší, tak program vypíše False

text1 = input("Vlož první řetězec: ")
text2 = input("Vlož druhý řetězec: ")

print(len(text1)>len(text2))