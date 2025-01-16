def matika(cislo):                                      #cislo
    print(f"Pouštíme funkci matika s cislo {cislo}")    #2              1       0
    if cislo > 0:                                       #True           True    False
        cislo -= 1                                      #1              0
        matika(cislo)                                   #--------->     ------->
        print(cislo)                                    #1              0
        print(f"Dokončuji puštění funkce matika s {cislo + 1}")

matika(3)

