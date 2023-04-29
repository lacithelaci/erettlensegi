class Epitmenyado:
    def __init__(self, az, utca, hazszam, kategoria, alapterulet):
        self.az = int(az)
        self.utca = utca
        self.hazszam = hazszam
        self.kategoria = kategoria
        self.alapterulet = int(alapterulet)

    def __repr__(self):
        return f"{self.az} {self.utca} {self.hazszam} {self.kategoria} {self.alapterulet}"


f = open("utca.txt")
adosavok = f.readline().split()
lista = []
for i in f:
    i = i.strip().split()
    lista.append(Epitmenyado(*i))
print(f"2. feladat. A mintában {len(lista)} telek szerepel. ")
print(f"3. feladat. Egy tulajdonos adószáma: 68396 ")
az = 68396
adoszamos_lista = [i for i in lista if i.az == az]
for i in adoszamos_lista:
    print(f"{i.utca} utca {i.hazszam}")


def ado(adosav, adoterulet, fizetendo):
    szum = 0
    if adosav == 'A':
        szum = adoterulet * int(fizetendo[0])
    elif adosav == 'B':
        szum = adoterulet * int(fizetendo[1])
    else:
        szum = adoterulet * int(fizetendo[2])
    if szum < 10000:
        return 0
    else:
        return szum


print(f"5. feladat ")
tipusok = set(i.kategoria for i in lista)
db = 0
szum = 0
for y in sorted(tipusok):
    db = 0
    szum = 0
    for i in lista:
        if i.kategoria == y:
            db += 1
            szum += ado(i.kategoria, i.alapterulet, adosavok)
    print(f"A sávba {db} telek esik, az adó {szum} Ft. ")
print("6. feladat")
utcak = set(i.utca for i in lista)
db = 0
kategoriak = []
for y in sorted(utcak):
    kategoriak = []
    for i in lista:
        if i.utca == y:
            if i.kategoria not in kategoriak:
                kategoriak.append(i.kategoria)
    if len(kategoriak) > 1:
        print(y)
f = open("fizetendo.txt", "w", encoding="utf-8")
szotar = {}
for i in lista:
    szotar[i.az] = szotar.get(i.az, 0) + ado(i.kategoria, i.alapterulet, adosavok)

for index, i in szotar.items():
    f.write(f"{index} {i}\n")
