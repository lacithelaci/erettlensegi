lista = []
f = open("melyseg.txt")
for i in f:
    i = i.strip()
    lista.append(i)
print(f"1. feladat\nA fájl adatainak száma: {len(lista)} ")
print("2. feladat")
db = 0
bekert = 9
melyseg = None
szam = None
for i in lista:
    db += 1
    if bekert == db:
        szam = i
        print(f"Ezen a helyen a felszín {i} méter mélyen van. ")
        break
print(f"3. feladat ")
erintetlen = [i for i in lista if i == '0']
print(f"Az érintetlen terület aránya {len(erintetlen) / len(lista) * 100:.2f}%. ")
f = open("godrok.txt", "w")
godorlista = []
seged = []
for i in lista:
    seged.append(i)
    if i == "0":
        if len(seged) == 1 and "0" in seged:
            godorlista.append(seged)
            seged = []
        else:
            godorlista.append(seged[0:-1])
            godorlista.append([seged[-1]])
            seged = []
csak_godrok = [i for i in godorlista if "0" not in i]
for i in csak_godrok:
    for y in i:
        f.write(f"{y} ")
    f.write(f"\n")
print(f"5. feladat\nA gödrök száma: {len(csak_godrok)}\n6. feladat")
if szam != "0":
    db = 0
    db2 = 0
    elmentett_godor = None
    megvan = False
    for i in godorlista:
        db2 += 1
        for y in i:
            db += 1
            if db == bekert:
                elmentett_godor = i
                megvan = True
                break
        if megvan:
            break

    print(f"a)\nA gödör kezdete: {db2} méter, a gödör vége: {db2 + len(elmentett_godor) - 1} méter. ")
    print(f"b)")
    monoton = []
    for i in elmentett_godor:
        i = int(i)
        monoton.append(i)
    a = max(monoton)
    helye = None
    db = 0
    for i in monoton:
        db += 1
        if a == i:
            helye = db
            break
    no = monoton[0:helye]
    csokken = monoton[helye - 1:]
    elozo = None
    jelenlegi = "None"
    egyezo = False
    lehet = False
    if sorted(monoton[0:helye]) == no and sorted(csokken, key=lambda i: i, reverse=True) == monoton[helye - 1:]:
        lehet = True
        for i in monoton:
            elozo = i
            if elozo == jelenlegi:
                egyezo = True
            jelenlegi = elozo
    if lehet and not egyezo:
        print("Folyamatosan mélyül.")
    else:
        print("Nem mélyül folyamatosan.")
    print(f"c)\nA legnagyobb mélysége {max(monoton)} méter. ")
    print(f"d)\nA térfogata {sum(monoton) * 10} m^3. ")
    print(f"e)\nA vízmennyiség {(sum(monoton) - len(monoton)) * 10} m^3.  ")
else:
    print(f"Az adott helyen nincs gödör.")
