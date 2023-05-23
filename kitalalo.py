import random

lista = ["fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas", "almafa", "babona", "gerinc", "dervis",
         "bagoly", "ecetes", "angyal", "boglya"]


def rajz(a, b):
    szoveg = ""
    for i in range(0, len(a)):
        if a[i] == b[i]:
            szoveg += a[i]
        else:
            szoveg += "."
    return szoveg


kivalasztott_szo = random.choice(lista)
bekert = input(f"Kérem a tippet: ")
db = 1
while kivalasztott_szo != bekert:
    if bekert == "stop":
        break
    print(f"Az eredmény: {rajz(kivalasztott_szo, bekert)}")
    bekert = input(f"Kérem a tippet: ")
    db += 1
if db != 0:
    print(f"{db} tippeléssel sikerült kitalálni. ")
