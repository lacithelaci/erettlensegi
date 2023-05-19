import random


class Vetelkedo:
    def __init__(self, kerdes, valasz, pont, temakor):
        self.kerdes = kerdes
        self.valasz = int(valasz)
        self.pont = int(pont)
        self.temakor = temakor

    def __repr__(self):
        return f"{self.kerdes} {self.valasz} {self.pont} {self.temakor}"


lista = []
f = open("felszam.txt")
for kerdes in f:
    kerdes = kerdes.strip()
    minden_mas = f.readline().strip().split()
    lista.append(Vetelkedo(kerdes, *minden_mas))
print(f"2. feladat\n{len(lista)} feladat van az adatfájlban\n3. feladat")
matek = [i.pont for i in lista if i.temakor == "matematika"]
szotar = {}
for i in matek:
    szotar[i] = szotar.get(i, 0) + 1
print(f"Az adatfajlban {len(matek)} matematika feladat van")
for index, i in szotar.items():
    print(f"{index} pontosból {i} darab", end=" ")
pontok = [i.valasz for i in lista]
print(f"4. feladat\n{min(pontok)}-tól {max(pontok)}-ig terjed a fájlban található válaszok számértéke\n5. feladat")
temakorok = set(i.temakor for i in lista)
temakorok = list(temakorok)
print("Ilyen témakörök szerepelnek ténylegesen az adatfájlban:", *temakorok)
print("6. feladat")
bekert = input("Adjon meg egy témakört")
temakoros = [i for i in lista if i.temakor == bekert]
random_kerdes = random.choice(temakoros)
print(random_kerdes.kerdes)
valasz = int(input("Adjon rá választ"))
if valasz == random_kerdes.valasz:
    print(f"A valasz {random_kerdes.pont} pontot er. ")
else:
    print(f"A valasz 0 pontot er.\nA helyes valasz: {random_kerdes.valasz} ")
tesztsor = []
f = open(f"tesztfel.txt", "w",encoding="utf-8")
while len(tesztsor) != 10:
    random_kerdes = random.choice(lista)
    if random_kerdes not in tesztsor:
        tesztsor.append(random_kerdes)
db = 0
for i in tesztsor:
    f.write(f"{i.pont} {i.valasz} {i.kerdes}\n")
    db += i.pont
f.write(f"maximalisan gyujtheto pontszam: {db}")
