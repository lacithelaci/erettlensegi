import random

lista = []
f = open("ajto.txt")

for i in f:
    i = i.strip()
    lista.append(i)

print(f"2. feladat\nAdja meg, mi nyitja a zárat! 239451")

szam = input()
seged = []
db = 0

for i in lista:
    db += 1

    if i == szam:
        seged.append(db)

print(f"3. feladat\nA nyitó kódszámok sorai:", *seged)
print(f"4. feladat")


def ismetlodo(szam):
    return len(set(i for i in szam))


db = 0
volt = False

for i in lista:
    db += 1

    if len(i) != ismetlodo(i):
        volt = True
        print(f"Az első ismétlődést tartalmazó próbálkozás sorszáma:", db)
        break

if not volt:
    print(f"nem volt ismétlődő számjegy")

print("5. feladat")


def karakter(hossz):
    kod = ""
    karakterek = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while len(kod) != hossz:
        character = random.choice(karakterek)

        if character not in kod:
            kod += character

    return kod


print(f"Egy {len(szam)} hosszú kódszám: {karakter(len(szam))} ")


def nyit(jo, proba):
    egyezik = len(jo) == len(proba)

    if egyezik:
        elteres = int(jo[0]) - int(proba[0])

        for i in range(1, len(jo)):
            if (elteres - (int(jo[i]) - int(proba[i]))) % 10 != 0:
                egyezik = False

    return egyezik


f = open("siker.txt", "w", encoding="utf-8")
for i in lista:

    if len(i) != len(szam):
        f.write(f"{i} hibás hossz\n")

    else:

        if nyit(i, szam):
            f.write(f"{i} sikeres\n")

        else:
            f.write(f"{i} hibás kódszám\n")
