def szovegge(i):
    i = i.split(" ")
    sz = ""
    for x in i:
        sz += x

    return sz


f = open("melyseg.txt")
lista = []
for i in f:
    i = i.strip()
    lista.append(int(i))
print(f"1. feladat\nA fájl adatainak száma: {len(lista)}\n2. feladat")
tavolsag = int(input("Adjon meg egy távolságértéket! 9"))
db = 0
ertek=None
for i in lista:
    db += 1
    if db == tavolsag:
        ertek=i
        print(f"Ezen a helyen a felszín {ertek} méter mélyen van. ")
        break
print("3. feladat")
db = 0
for i in lista:
    if i == 0:
        db += 1
print(f"Az érintetlen terület aránya {round(db / len(lista) * 100, 2)}%. ")
f = open("godrok.txt", "w")
lista2 = []
szoveg = ""
for i in lista:
    if i == 0:
        if szoveg != "":
            lista2.append(szoveg)
        szoveg = ""
    else:
        szoveg += str(i)
        szoveg += " "
for i in lista2:
    if i != "":
        f.write(f"{i}\n")
print("5. feladat")
print(f"A gödrök száma: {len(lista2)} ")
print("6. feladat")
if ertek!=0:
    lista2 = []
    szoveg = ""
    for i in lista:
        if i == 0:
            if szoveg == "":
                lista2.append("0")
            else:
                lista2.append(szoveg)
                szoveg = ""
        else:
            szoveg += str(i)
    sor = 0
    db = 0
    sor2 = ""
    volt = False
    for i in lista2:
        sor += 1
        sor2 = i
        for y in i:
            db += 1
            if db == tavolsag:
                volt = True
        if volt:
            break
    print(f"a)\nA gödör kezdete: {sor} méter, a gödör vége: {sor - 1 + len(sor2)} méter. ")
    f = open("godrok.txt", "r")
    lista3 = []
    for i in f:
        i = i.strip()
        lista3.append(i)

    kell = ""
    lista4 = []
    for i in lista3:
        if szovegge(i) == sor2:
            kell = (i.split(" "))
    for i in kell:
        i = int(i)
        lista4.append(i)
    a = max(lista4)
    helye = None
    db = 0
    for i in lista4:
        db += 1
        if a == i:
            helye = db
            break
    lista2 = lista[0:helye]
    lista3 = lista[helye - 1:]
    halmaz = set(lista4)
    elozo = None
    jelenlegi = "None"
    egyezo = False
    lehet = False
    if sorted(lista4[0:helye]) == lista2 and sorted(lista3, key=lambda i: i, reverse=True) == lista4[helye - 1:]:
        lehet = True
        for i in lista4:
            elozo = i
            if elozo == jelenlegi:
                egyezo = True
            jelenlegi = elozo
    if lehet and not egyezo:
        print("b)\nFolyamatosan mélyül.")
    else:
        print("b)\nNem mélyül folyamatosan.")

    print(f"c)\nA legnagyobb mélysége {max(lista4)} méter. ")
    print(f"d)\nA térfogata {sum(lista4) * 10} m^3. ")
    print(f"e)\nA vízmennyiség {(sum(lista4) - len(lista4)) * 10} m^3.  ")
else:
    print(f"Az adott helyen nincs gödör.")
