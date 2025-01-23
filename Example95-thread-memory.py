import threading
import time

posledni_clovek = "Nikdo"

def ctecka_cte():
    global posledni_clovek
    while True:
        vstup_ctecky = input("Zadej kdo vešel:")
        posledni_clovek = vstup_ctecky


def obrazovka_zobrazuje():
    global posledni_clovek
    while True:
        time.sleep(1)
        print(f"Poslední kdo prošel je {posledni_clovek}")


threading.Thread(target=ctecka_cte).start()
threading.Thread(target=obrazovka_zobrazuje).start()