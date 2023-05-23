class Szalag:
    def __init__(self, ido, hely1, hely2, tomeg, sor):
        self.ido = int(ido)
        self.hely1 = int(hely1)
        self.hely2 = int(hely2)
        self.tomeg = int(tomeg)
        self.sor = sor

    def __repr__(self):
        return f"{self.ido} {self.hely1} {self.hely2} {self.tomeg}"


f = open("szallit.txt")
lista = []
elso_sor = f.readline().strip().split()
db = 0
for i in f:
    db += 1
    i = i.strip().split()
    lista.append(Szalag(*i, db))
print(f"2. feladat")
sor = int(input("Adja meg, melyik adatsorra kíváncsi! 3 "))
for i in lista:
    if i.sor == sor:
        print(f"Honnan: {i.hely1} Hova: {i.hely2} ")
        break


def tav(szalaghossz, indulashelye, erkezeshelye):
    if erkezeshelye > indulashelye:
        return erkezeshelye - indulashelye
    else:
        return szalaghossz - indulashelye + erkezeshelye


kulonbseg = [tav(int(elso_sor[0]), i.hely1, i.hely2) for i in lista]
print(f"4. feladat\nA legnagyobb távolság: {max(kulonbseg)} ")
print(f"A maximális távolságú szállítások sorszáma:", end=" ")
for i in lista:
    if max(kulonbseg) == tav(int(elso_sor[0]), i.hely1, i.hely2):
        print(i.sor, end=" ")
print(f"\n5. feladat")
kezdohely = int(elso_sor[0])
szum = 0
for i in lista:
    if (i.hely1 and i.hely2) != 0:
        if i.hely1 > i.hely2:
            szum += i.tomeg
print(f"A kezdőpont előtt elhaladó rekeszek össztömege: {szum}\n6. feladat ")
bekert = int(input("Adja meg a kívánt időpontot! 300 "))
seged = []


def szalitasi_ido(tav, idoegyseg):
    return tav * idoegyseg


for i in lista:
    if i.ido <= bekert and bekert < szalitasi_ido(tav(int(elso_sor[0]), i.hely1, i.hely2), int(elso_sor[1])):
        seged.append(i.sor)
if len(seged) != 0:
    print("A szállított rekeszek halmaza:", *seged)
else:
    print("A szállított rekeszek halmaza: üres")
f = open(f"tomeg.txt", "w", encoding="utf-8")
szotar = {}
for i in lista:
    szotar[i.hely1] = szotar.get(i.hely1, 0) + i.tomeg
for index, i in sorted(szotar.items()):
    f.write(f"{index} {i}\n")
