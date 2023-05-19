import random

print(f"1. feladat")
lista = ["I", "F"]
fej_vagy_iras = random.choice(lista)
print(f"A pénzfeldobás eredménye:", fej_vagy_iras)
print(f"2. feladat\nTippeljen! (F/I)=")
tipp = input()
fej_vagy_iras = random.choice(lista)
print(f"A tipp {tipp}. a dobás eredménye {fej_vagy_iras} volt.")
if fej_vagy_iras == tipp:
    print(f"Ön eltalálta.")
else:
    print(f"Ön nem találta el.")
print(f"3. feladat")
f = open("kiserlet.txt")
fej = 0
db = 0
for i in f:
    db += 1
    if i.strip() == "F":
        fej += 1
print(f"A kísérlet {db} dobásból áll")
print(f"4. feladat\nA kísérlet során a fej relatív gyakorisága {fej / db * 100:.2f}% volt\n5. feladat")
f = open("kiserlet.txt")
db = 0
fej = 0
for i in f:
    i = i.strip()
    if i == "F":
        db += 1
    else:
        db = 0
    if db == 2:
        fej -= -1
    elif db == 3:
        fej += -1
print(f"A kísérlet során {fej} alkalommal dobtak pontosan két fejet egymás után\n6. feladat")
f = open("kiserlet.txt")
tisztafej = 0
db = 0
helye = 0
masz = 0
for i in f:
    i = i.strip()
    db += 1
    if i == "F":
        tisztafej += 1
    else:
        tisztafej = 0
    if masz < tisztafej:
        masz = tisztafej
        helye = db
print(f"A leghosszabb tisztafej sorozat {masz} tagból áll, kezdete a(z) {helye + 1 - masz}. dobás")
ffff = 0
fffi = 0


def eloallitas():
    lista = ["I", "F"]
    sztr = ""
    for i in range(0, 4):
        sztr += random.choice(lista)

    return sztr


lista = []
for i in range(0, 1000):
    lista.append(eloallitas())
f = open(f"dobasok.txt", "w")
for i in lista:
    if i == "FFFF":
        ffff += 1
    elif i == "FFFI":
        fffi += 1
f.write(f"FFFF: {ffff}, FFFI: {fffi}\n")
for i in lista:
    f.write(i + " ")
