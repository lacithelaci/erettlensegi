maganhangzo = ["a", "e", "o", "u", "i"]
szo = input("1. feladat Adjon meg egy szót:")
van_benne = False
for betu in szo:
    if betu in maganhangzo:
        van_benne = True
if van_benne:
    print("Van benne magánhangzó.")
else:
    print("Nincs benne magánhangzó.")
print("2. feladat")
f = open("szoveg.txt")
leghosszabb = ""
for szo in f:
    szo = szo.strip()
    if len(szo) > len(leghosszabb):
        leghosszabb = szo
print(
    f"A leghosszabb szó a szoveg.txt állományban: {leghosszabb}. Ennyi karakterből áll: {len(leghosszabb)}\n3. feladat")
lista = []
f = open("szoveg.txt")
for szo in f:
    szo = szo.strip()
    lista.append(szo)


def tobbmaganhagzo(szo):
    maganhangzo = ["a", "e", "o", "u", "i"]
    mgh = 0
    for betu in szo:
        if betu in maganhangzo:
            mgh += 1
    return mgh / len(szo) > 0.5


db = 0
for szo in lista:
    if tobbmaganhagzo(szo):
        db += 1
print(f"{db}/{len(lista)} : {(db / len(lista)):.2f}% ")
print("4. feladat")


def harombetu(szo):
    return szo[1:4]


otszavas = [szo for szo in lista if len(szo) == 5]
szoreszlet = input("Kérek egy szórészletet")
for szo in otszavas:
    if harombetu(szo) == szoreszlet:
        print(szo, end=" ")
print("\n5. feladat")
szotar = {}
letra = []
for szo in otszavas:
    szotar[harombetu(szo)] = szotar.get(harombetu(szo), 0) + 1
for betuk, db in szotar.items():
    for szo in otszavas:
        if db > 1 and betuk == harombetu(szo):
            letra.append(szo)
f = open("letra.txt", "w")
elozo = ""
jelenlegi = ""
db = 0
for szo in letra:
    jelenlegi = szo
    if db > 0:
        if harombetu(jelenlegi) == harombetu(elozo):
            f.write(f"{elozo}\n")
        else:
            f.write(f"{elozo}\n")
            f.write(f"\n")
    elozo = jelenlegi
    db += 1
f.write(letra[-1])
print(letra)

