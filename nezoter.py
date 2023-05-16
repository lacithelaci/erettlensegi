foglaltsag = []
kategoria = []
f = open("foglaltsag.txt")
f2 = open("kategoria.txt")
for i in f:
    i = i.strip()
    foglaltsag.append(i)
for i in f2:
    i = i.strip()
    kategoria.append(i)
print("2. feladat")
sor = int(input("sor"))
oszlop = int(input("oszlop"))
if foglaltsag[sor-1][oszlop-1] == "x":
    print(f"foglalt")
else:
    print(f"szabad")
print(f"3. feladat")
db = 0
for i in foglaltsag:
    for y in i:
        if y == "x":
            db += 1
print(f"Az előadásra eddig {db} jegyet adtak el, ez a nézőtér {db / (15 * 20) * 100:.0f}%-a. ")
print(f"4. feladat")
szotar = {}
for sor1 in range(0, 15):
    for oszlop1 in range(0, 20):
        if foglaltsag[sor1][oszlop1] == "x":
            szotar[kategoria[sor1][oszlop1]] = szotar.get(kategoria[sor1][oszlop1], 0) + 1
legtobb = max(szotar.values())
for index, i in szotar.items():
    if i == legtobb:
        print(f"A legtöbb jegyet a(z) {index}. árkategóriában értékesítették. ")
        break
print(f"5. feladat")


def fizetendo(a):
    lista = [5000, 4000, 3000, 2000, 1500]
    return lista[a - 1]


szum = 0
for index, i in szotar.items():
    szum += fizetendo(int(index)) * i
print(f"A színház bevétele:", szum)
ureshelyek = []
for i in foglaltsag:
    ureshelyek.append(i.split("x"))
db = 0
for i in ureshelyek:
    for y in i:
        if len(y) == 1:
            db += 1
print(f"6. feladat\n{db} ilyen „egyedülálló” üres hely van a nézőtéren! ")
f = open("szabad.txt", "w")
db = 0
for sor1 in range(0, 15):
    for oszlop1 in range(0, 20):
        db += 1
        if foglaltsag[sor1][oszlop1] == "o":
            f.write(kategoria[sor1][oszlop1])
        else:
            f.write("x")
        if db % 15 == 0:
            f.write("\n")
