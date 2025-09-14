import random
# from modul import osszeg, szorzas
# import modul as m
from modul import osszeg as sum

''' első próbálkozás
    több soros

kor = 50
nev = "Guszti"
hazas = True

kor += 5

print("Felhasználó: ", nev, kor, hazas)

szoveg = "Rendszámtartó"

print(szoveg[0:4])
print(szoveg[4:8])
print(szoveg[-5:])

lista = ["Rend", "szám", "tartó"]
print(lista)
print(lista[0], lista[1], lista[2], sep="")

lista.append("tábla")
print(lista)

halmaz = {1, 2, 3, "négy", 1}
print(halmaz)

szotar = {"név": "Józsi", "kor": 40, "házas": True}
print(szotar)

'''

# kor = int(input("Hány évas vagy: "))

kor = 50
print("A felhasználó kora: ".center(50, "_"))

print("A felhasználó kora: ", kor)
print("A felhasználó kora: {0}".format(kor))

print(random.randint(5, 10))
sum()



