# Ez egy próba modul

def osszeg():
    egyik = int(input("Kérek egy számot:"))
    másik = int(input("Kérek egy másik számot:"))

    eredmeny = egyik + másik

    print(str(egyik).rjust(50, "_"))
    print(str(másik).rjust(50, "_"))
    print("+")
    print(str(eredmeny).rjust(50, "_"))
    return

def szorzas():
    egyik = int(input("Kérek egy számot:"))
    másik = int(input("Kérek egy másik számot:"))

    eredmeny = egyik * másik

    print(str(egyik).rjust(50, "_"))
    print(str(másik).rjust(50, "_"))
    print("*")
    print(str(eredmeny).rjust(50, "_"))
    return


