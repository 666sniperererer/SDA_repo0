pass
def hello():
    print("HELLO!!")

def dej_tam_hello(fnc):
    print(f"Funkci {fnc.__name__} nahradíme za hello")
    return hello

@dej_tam_hello
def ahoj():
    print("AHOJ!!")

@dej_tam_hello
def guten():
    print("GUTEN TAG!!")

print("Spustí se program")
guten()