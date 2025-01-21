def pridej_podpis(text):
    return "Albert napsal: " + text

print(pridej_podpis("Dnes je úterý"))

podpis = lambda text: "Albert napsal: " + text
print(podpis("Zítra je středa"))

def je_prvni_vetsi(hodnota1, hodnota2):
    return hodnota1 > hodnota2

print(je_prvni_vetsi(4,3))

je_prvni_vetsi_lambda = lambda hodnota1, hodnota2: hodnota1 > hodnota2
print(je_prvni_vetsi_lambda(4,3))