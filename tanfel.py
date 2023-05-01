class Felosztas:
    def __init__(self, nev, targy, osztaly, oraszam):
        self.nev = nev
        self.targy = targy
        self.osztaly = osztaly
        self.oraszam = int(oraszam)

    def __repr__(self):
        return f"{self.nev} {self.targy} {self.osztaly} {self.oraszam}"


lista = []
f = open("beosztas.txt")
seged = []
db = 0
for i in f:
    db += 1
    i = i.strip()
    seged.append(i)
    if db == 4:
        lista.append(Felosztas(*seged))
        seged = []
        db = 0
print(f"2. feladat\nA fájlban {len(lista)} bejegyzés van. ")
oraszam = [i.oraszam for i in lista]
print(f"3. feladat\nAz iskolában a heti összóraszám: {sum(oraszam)} ")
print(f"4. feladat")
nev = input("Egy tanár neve= Albatrosz Aladin ")
tanar = [i.oraszam for i in lista if i.nev == nev]
print(f"A tanár heti óraszáma: {sum(tanar)} ")
f = open(f"of.txt", "w")
for i in sorted(lista, key=lambda i: i.osztaly):
    if i.targy == "osztalyfonoki":
        f.write(f"{i.osztaly} - {i.nev}\n")
print("6. feladat")
osztaly = input("Osztály= 10.b ")
targy = input("Tantárgy= kemia ")
bontas = True
for i in lista:
    if i.targy == targy:
        if i.osztaly[0:len(osztaly) - 1] == osztaly[0:-1]:
            if i.osztaly[-1] == 'x':
                bontas = False
if bontas:
    print(f"Csoportbontásban tanulják. ")
else:
    print(f"Nem csoportbontásban tanulják.")
print("7. feladat")
tanarok=set(i.nev for i in lista)
print(f"Az iskolában {len(tanarok)} tanár tanít.")
