#  Copyright (c) 2022.4.19.
#  A forráskód készítője: Ladányi Attila

f = open("megoldas.txt", "r", encoding="utf-8")
lista = {}

darab = int(f.readline().strip())

for i in f:
    seged = []
    for sorok in range(10):
        seged.append(f.readline().strip().split())

    lista[i.strip()] = seged

feladvany = [i.strip().split() for i in open("feladvany.txt", "r", encoding="utf-8")]

beker = input("1. feladat\nAdja meg a torony adatait! ").split()

if int(beker[2]) > 3:
    print("Nehéz torony.")

bekersor = int(beker[0]) - 1
bekeroszlop = int(beker[1]) - 1


def nemlehet(sor, oszlop):
    # hol nem lehet hajó
    veg = []

    for i in range(10):
        for j in range(10):
            if i in range(sor - 1, sor + 2) and j in range(oszlop - 1, oszlop + 2) and [i, j] != [sor, oszlop]:
                veg.append([i + 1, j + 1])

    return veg


print("\n2. feladat\nEzekre a helyekre nem kerülhet biztosan: ")

hibasak = []

for i in nemlehet(bekersor, bekeroszlop):
    print(f"{i[0]}, {i[1]}")

nemerre = []

for nev, megoldas in lista.items():
    kiszed = []
    for i in megoldas:
        seged = []
        for j in i:
            if j == "11":
                seged.append("0")
            else:
                seged.append(j)
        kiszed.append(seged)

    if kiszed != feladvany:
        nemerre.append(nev)
        hibasak.append(nev)

print("\n3. feladat")

if len(nemerre) == 0:
    print("Mindegyik megoldás erre a heti feladványra érkezett.")
else:
    print("Nem erre érkeztek: ")

    for i in nemerre:
        print(i)

hanyhibas = 0

for nev, megoldas in lista.items():
    hanyhajo = 0

    for i in megoldas:
        for j in i:
            if j == "11":
                hanyhajo += 1

    if hanyhajo != 12:
        hanyhibas += 1
        hibasak.append(nev)

print(f"\n4. feladat\nEnnyi hibás megoldás van ilyen szempontból: {hanyhibas}")

hanyhibas = 0

for nev, megoldas in lista.items():
    holnemlehet = []

    for i in range(len(megoldas)):
        for j in range(10):
            if megoldas[i][j] != "0":
                for hol in nemlehet(i, j):
                    holnemlehet.append([hol[0] - 1, hol[1] - 1])

    ezhibas = False

    for i in range(10):
        for j in range(10):
            if megoldas[i][j] == "11" and [i, j] in holnemlehet:
                ezhibas = True

    if ezhibas:
        hanyhibas += 1
        hibasak.append(nev)

print(f"\n5. feladat\nEnnyi hibás megoldás van ilyen szempontból: {hanyhibas}")

helyes = []

for nev, megoldas in lista.items():
    if nev not in hibasak:
        hibase = False
        for i in range(10):
            for j in range(10):
                if megoldas[i][j] not in ["0", "11"]:
                    hanydarab = 0

                    # Abban a sorban

                    sorban = len([hely for hely in megoldas[i] if hely == "11"])

                    # Abban az oszlopban

                    oszlopban = 0

                    for sor in megoldas:
                        if sor[j] == "11":
                            oszlopban += 1

                    if not sorban + oszlopban == int(megoldas[i][j]):
                        hibase = True

        if not hibase:
            helyes.append(nev)

print(f"\n6. feladat\nHelyes megoldók nevei:")

for i in helyes:
    print(i)