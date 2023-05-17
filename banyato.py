f = open("melyseg.txt")
sor_oszlop = []
for i in range(0, 2):
    sor_oszlop.append(int(f.readline().strip()))
lista = []
for i in f:
    i = i.strip().split()
    lista.append(i)
print(f"2. feladat ")
sor = int(input(f"A mérés sorának azonosítója=12 "))
oszlop = int(input("A mérés oszlopának azonosítója=6 "))
print(f"A mért mélység az adott helyen {lista[sor - 1][oszlop - 1]} dm ")
szum = 0
db = 0
for i in lista:
    for y in i:
        if y != "0":
            db += 1
            szum += int(y)
print(f"3. feladat\nA tó felszíne: {db} m2, átlagos mélysége: {szum / (db * 10):.2f} m ")
print(f"4. feladat")
masz = 0
for i in lista:
    for y in i:
        if masz < int(y):
            masz = int(y)
print(f"A tó legnagyobb mélysége: 98 dm\nA legmélyebb helyek sor-oszlop koordinátái: ")
for sor1 in range(0, sor_oszlop[0]):
    for oszlop1 in range(0, sor_oszlop[1]):
        if int(lista[sor1][oszlop1]) == masz:
            print(f"({sor1 + 1}; {oszlop1 + 1})", end=" ")
print(f"\n5. feladat")
hossz = 0
for i, sor in enumerate(lista):
    for j, melyseg in enumerate(sor):
        if int(melyseg) > 0:
            if int(sor[j - 1]) == 0:
                hossz += 1
            if int(sor[j + 1]) == 0:
                hossz += 1
            if int(lista[i - 1][j]) == 0:
                hossz += 1
            if int(lista[i + 1][j]) == 0:
                hossz += 1
print(f'A tó partvonala {hossz} m hosszú')
bekert = int(input(f"6. feladat\nA vizsgált szelvény oszlopának azonosítója=6 "))
adatok = []
for sor1 in range(0, sor_oszlop[0]):
    for oszlop1 in range(0, sor_oszlop[1]):
        if oszlop1 == bekert - 1:
            adatok.append(int(lista[sor1][bekert - 1]))
f = open("diagram.txt", "w")
db = 0
csillag = "*"
for i in adatok:
    db += 1
    i = round(i / 10)
    if db < 10:
        f.write(f"0{db} {csillag * i}\n")
    else:
        f.write(f"{db} {csillag * i}\n")
