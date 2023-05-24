class Szinek:
    def __init__(self, piros, zold, kek, sor, oszlop):
        self.piros = int(piros)
        self.zold = int(zold)
        self.kek = int(kek)
        self.sor = int(sor)
        self.oszlop = int(oszlop)

    def __repr__(self):
        return f"{self.piros} {self.zold} {self.kek} {self.sor} {self.oszlop}"

    def szin(self):
        return f"({self.piros},{self.zold},{self.kek})"

    def ertek(self):
        return self.kek + self.zold + self.piros


f = open("kep.txt")
lista = []
seged = []
db = 0
sor = 1
oszlop = 0

for i in f:
    i = i.strip().split()

    for y in i:
        db += 1
        seged.append(y)

        if db == 3:
            db = 0
            oszlop += 1
            lista.append(Szinek(*seged, sor, oszlop))
            seged = []

        if oszlop == 640:
            oszlop = 0
            sor += 1

print("2. feladat\nKérem egy képpont adatait! ")

sor = int(input("Sor:"))
oszlop = int(input("Oszlop:"))

for i in lista:

    if i.sor == sor and i.oszlop == oszlop:
        print(f"A képpont színe RGB{i.szin()} ")
        break

print("3. feladat")

megfelelo = [i.ertek() for i in lista if i.ertek() > 600]
print(f"A világos képpontok száma: {len(megfelelo)} ")

print("4. feladat")

osszes = [i.ertek() for i in lista if i.ertek()]
legsotetebb = min(osszes)
print(f"A legsötétebb pont RGB összege: {legsotetebb}\nA legsötétebb pixelek színe: ")

for i in lista:
    if i.ertek() == legsotetebb:
        print(f"RGB{i.szin()}")


def hatar(sor, ertek):
    elteres = False

    for i in range(0, 639):

        if sor[i + 1] - sor[i] > ertek:
            elteres = True

    return elteres


print("6. feladat")

seged_lista = []
seged2 = []

for y in range(1, 361):
    seged_lista = []

    for i in lista:

        if y == i.sor:
            seged_lista.append(i.kek)

    if (hatar(seged_lista, 10)):
        seged2.append(y)

print(f"A felhő legfelső sora: {min(seged2)} ")
print(f"A felhő legalsó sora: {max(seged2)} ")
