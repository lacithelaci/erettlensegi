print("1. feladat")
otvenkettes = []
for i in range(5):
    a = int(input("kérek egy számot"))
    otvenkettes.append(a)

print(f"2. feladat")
for i in sorted(otvenkettes):
    print(i, end=" ")
print("\n3. feladat")
bekert_szam = int(input("Kérem egy hét sorszámát"))
print("4. feladat")
lista = []
f = open("lottosz.dat")
for i in f:
    i = i.strip().split()
    lista.append(i)
db = 0
for kihuzott in lista:
    db += 1
    if db == bekert_szam:
        print(*kihuzott)
print("5. feladat")
szamok_ismetles_nelkul = set()
for kihuzott in lista:
    for szamok in kihuzott:
        szamok_ismetles_nelkul.add(int(szamok))
if len(szamok_ismetles_nelkul) == 90:
    print("Nincs")
else:
    print("Van")
print("6. feladat")
paratlan = 0
for kihuzott in lista:
    for szamok in kihuzott:
        if int(szamok) % 2 == 1:
            paratlan += 1
print(paratlan)
print("7. feladat")
otvenkettes = sorted(otvenkettes)
lista.append(otvenkettes)
f = open("lotto52.ki", "w", encoding="utf-8")
db = 0
for kihuzott in lista:
    for szamok in kihuzott:
        db += 1
        f.write(f"{(szamok)} ")
        if db % 5 == 0:
            f.write("\n")
print("Számok átírva\n8. feladat")
szamhalmaz = set(i for i in range(1, 91))
db = 0
db2 = 0
for osszes in szamhalmaz:
    db = 0
    for kihuzott in lista:
        for szamok in kihuzott:
            if osszes == int(szamok):
                db += 1
    db2 += 1
    if db2 % 15 != 0:
        print(db, end=" ")
    else:
        print(db, end="\n")
primek = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
kihuzott_primek = []

for kihuzott in lista:
    for szamok in kihuzott:
        if int(szamok) in primek:
            kihuzott_primek.append(int(szamok))
print("9. feladat")
ki_nem_huzott_primek = [prim for prim in primek if prim not in kihuzott_primek]
print(*ki_nem_huzott_primek)
