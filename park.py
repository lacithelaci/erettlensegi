class Agyasok:
    def __init__(self, kezdet, veg, szin, sorszam):
        self.kezdet = int(kezdet)
        self.veg = int(veg)
        self.szin = szin
        self.sorszam = sorszam

    def __repr__(self):
        return f"{self.kezdet} {self.veg} {self.szin}"


f = open("felajanlas.txt")
lista = []
agyas_szam = int(f.readline().strip())
db = 0

for i in f:
    db += 1
    lista.append(Agyasok(*i.strip().split(), db))

print(f"2. feladat\nA felajánlások száma: {len(lista)}\n3. feladat")
mindket_oldalt = [i.sorszam for i in lista if i.kezdet > i.veg]

print(f"A bejárat mindkét oldalán ültetők:", *mindket_oldalt)
print(f"4. feladat\nAdja meg az ágyás sorszámát! 100 ")

agyas = int(input())
beultetett = [i.szin for i in lista if
              (i.kezdet <= agyas <= i.veg) or (i.kezdet >= agyas <= i.veg and i.veg < i.kezdet)]

minden_egyszer = set(i for i in beultetett)

if len(beultetett) != 0:
    print(
        f"A felajánlók száma: {len(beultetett)}\nA virágágyás színe, ha csak az első ültet: {beultetett[0]}\nA virágágyás színei:",
        *list(minden_egyszer))

else:
    print(f"A felajánlók száma: 0\nEzt az ágyást nem ültetik be.")
print(f"5. feladat ")

agyasok = set()
db = 0
for i in lista:

    if i.kezdet < i.veg:

        for ultetveny in range(i.kezdet, i.veg + 1):
            db += 1
            agyasok.add(ultetveny)

    else:

        for ultetveny in range(i.kezdet, agyas_szam + 1):
            agyasok.add(ultetveny)
            db += 1

        for ultetveny in range(1, i.veg + 1):
            agyasok.add(ultetveny)
            db += 1

if len(agyasok) == agyas_szam:
    print(f"Minden ágyás beültetésére van jelentkező.")

elif agyas_szam <= db:
    print(f"Átszervezéssel megoldható a beültetés.")

else:
    print(f"A beültetés nem oldható meg.")

f = open("szinek.txt", "w")
agyasok = set(i for i in range(1, agyas_szam + 1))

for ultetveny in sorted(agyasok):
    szine = "# 0"

    for i in lista:
        if i.kezdet <= ultetveny <= i.veg:
            szine = f"{i.szin} {i.sorszam}"
            break

        elif i.kezdet >= ultetveny <= i.veg and i.veg < i.kezdet:
            szine = f"{i.szin} {i.sorszam}"
            break
            
    f.write(f"{szine}\n")
