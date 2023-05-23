class Szinek:
    def __init__(self, piros, zold, kek):
        self.piros = int(piros)
        self.zold = int(zold)
        self.kek = int(kek)
        self.sor = 0
        self.oszlop = 0

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
for i in f:
    i = i.strip().split()
    seged.append(i)
seged2 = []
for i in seged:
    for y in i:
        seged2.append(y)
        db += 1
        if db == 3:
            db = 0
            lista.append(Szinek(*seged2))
            seged2 = []
sor = 1
oszlop = 0
db = 0
for i in lista:
    oszlop += 1
    db += 1
    i.oszlop = oszlop
    if oszlop == 640:
        oszlop = 0
    i.sor = sor
    if db == 640:
        db = 0
        sor += 1
sor = int(input("Sor:"))
oszlop= int(input("Oszlop:"))
for i in lista:
    if i.oszlop == oszlop and i.sor == sor:
        print(f"2. feladat\nA képpont színe RGB{i.szin()} ")
print(f"3. feladat")
db = 0
for i in lista:
    if i.ertek() > 600:
        db += 1
print(f"A világos képpontok száma: {db}\n4. feladat")
minimum = [i.ertek() for i in lista]
print(f"A legsötétebb pont RGB összege: {min(minimum)}\nA legsötétebb pixelek színe: ")
mint = min(minimum)
for i in lista:
    if i.ertek() == mint:
        print(f"{i.szin()}")


def hatar(sor, ertek):
    elteres = False
    for i in range(0, 639):
        if abs(sor[i + 1] - sor[i]) > ertek:
            elteres = True
    return elteres


print("6. feladat")
halmaz = set(i for i in range(1, 361))
seged_lista = []
seged2 = []
for y in halmaz:
    seged_lista = []
    for i in lista:
        if y == i.sor:
            seged_lista.append(i.kek)
    if (hatar(seged_lista, 10)):
        seged2.append(y)
print(f"A felhő legfelső sora: {min(seged2)} ")
print(f"A felhő legalsó sora: {max(seged2)} ")
