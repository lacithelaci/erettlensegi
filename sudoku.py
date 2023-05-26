fajlnev = input(f"1. feladat\nAdja meg a bemeneti fájl nevét! konnyu.txt ")
f = open(f"{fajlnev}")

lista = []
db = 0
sor = int(input("Adja meg egy sor számát! 1 "))
oszlop = int(input("Adja meg egy oszlop számát! 1 "))

for i in f:

    db += 1
    lista.append((i.split()))

    if db == 9:
        break

muveletek = []
for i in f:
    muveletek.append(i.split())
print("3. feladat")


def resztabla(sor, oszlop):
    return 3 * ((sor - 1) // 3) + ((oszlop - 1) // 3) + 1


if lista[sor - 1][oszlop - 1] != "0":

    print(f"Az adott helyen szereplő szám:", lista[sor - 1][oszlop - 1])
    print(f"A hely a(z) {resztabla(sor, oszlop)} résztáblázathoz tartozik.\n4. feladat")

else:

    print(f"Az adott helyet még nem töltötték ki.")
    print(f"A hely a(z) {resztabla(sor, oszlop)} résztáblázathoz tartozik.\n4. feladat")

db = 0

for i in lista:

    for y in i:

        if y == "0":
            db += 1

print(f"Az üres helyek aránya: {db / 81 * 100:.1f}% ")
print("5. feladat")

for sor in muveletek:

    volt_sor = False
    volt_oszlop = False
    halmaz = set()
    print(f"A kiválasztott sor: {sor[1]} oszlop: {sor[2]} a szám: {sor[0]} ")
    sorocska = int(sor[1])
    oszlopocska = int(sor[2])

    if lista[sorocska - 1][oszlopocska - 1] != "0":
        print(f"A helyet már kitöltötték.\n")

    else:
        for i in range(0, 9):

            if lista[i][oszlopocska - 1] == sor[0]:
                print("Az adott oszlopban már szerepel a szám\n")
                volt_oszlop = True

            elif lista[sorocska - 1][i] == sor[0]:
                print(f"Az adott sorban már szerepel a szám\n")
                volt_sor = True

            else:
                for y in range(0, 9):

                    if resztabla(i + 1, y + 1) == resztabla(sorocska, oszlopocska):
                        halmaz.add(lista[i][y])

        if sor[0] in halmaz and not volt_sor and not volt_oszlop:
            print(f"A résztáblázatban már szerepel a szám.\n ")

        elif not volt_sor and not volt_oszlop:
            print(f"A lépés megtehető\n")
