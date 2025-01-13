
try:
    print(2/0)
except Exception as e:
    print(e)
finally:
    print("Finally") #vykoná se ať nastane výjimka nebo ne

try:
    raise Exception("Nastala vyvolaná chyba pomocí raise")
except Exception as e:
    print(e)

print("Hotovo")