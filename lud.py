f = open("dobasok.txt")
for i in f:
    dobasok = list(map(int, i.split()))
f = open("osvenyek.txt")
osvenyek = []
for i in f:
    osvenyek.append(i.strip())
print(f"2. feladat\nA dobások száma: {len(dobasok)}\nAz ösvények száma: {len(osvenyek)}\n3. feladat")
leghosszabb = ""
szama = None
for index, i in enumerate(osvenyek, 1):
    if len(leghosszabb) < len(i):
        leghosszabb = i
        szama = index
print(f"Az egyik leghosszabb a(z) {szama}. ösvény, hossza: {len(leghosszabb)}\n4. feladat")
osveny = int(input("Adja meg egy ösvény sorszámát! 9 "))
jatekos_szam = int(input("Adja meg a játékosok számát! 5 "))
print("5. feladat")
megadott_osveny = osvenyek[osveny - 1]
szotar = {}
for i in megadott_osveny:
    szotar[i] = szotar.get(i, 0) + 1
for index, i in szotar.items():
    print(f"{index}: {i} darab ")
# 6. feladat
f = open("kulonleges.txt", "w", encoding="utf-8")
for index, i in enumerate(megadott_osveny, 1):
    if i != "M":
        f.write(f"{index}\t{i}\n")
print("7. feladat")
hanyadik_mezon_vagyunk = [0 for i in range(jatekos_szam)]
palyahossz = len(megadott_osveny)
db = 0
korok_szama = 0
for i in dobasok:
    hanyadik_mezon_vagyunk[db] = hanyadik_mezon_vagyunk[db] + i
    db += 1
    if db == 5:
        db = 0
        korok_szama += 1
    if max(hanyadik_mezon_vagyunk) >= palyahossz:
        break
for index, i in enumerate(hanyadik_mezon_vagyunk, 1):
    if max(hanyadik_mezon_vagyunk) == i:
        print(f"A játék a(z) {korok_szama}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: {index} ")
        break
print("8. feladat")
hanyadik_mezon_vagyunk = [0 for i in range(jatekos_szam)]
db = 0
for i in dobasok:
    hanyadik_mezon_vagyunk[db] = hanyadik_mezon_vagyunk[db] + i
    if max(hanyadik_mezon_vagyunk) < palyahossz:
        if megadott_osveny[hanyadik_mezon_vagyunk[db] - 1] == "E":
            hanyadik_mezon_vagyunk[db] = hanyadik_mezon_vagyunk[db] + i
        elif megadott_osveny[hanyadik_mezon_vagyunk[db] - 1] == "V":
            hanyadik_mezon_vagyunk[db] = hanyadik_mezon_vagyunk[db] - i
    db += 1
    if db == 5:
        db = 0
    if max(hanyadik_mezon_vagyunk) >= palyahossz and 0 == db:
        break
gyoztesek = []
vesztesek = []
for index, i in enumerate(hanyadik_mezon_vagyunk, 1):
    if max(hanyadik_mezon_vagyunk) == i:
        gyoztesek.append(index)
    else:
        vesztesek.append(index)
print(f"Nyertes(ek):", *gyoztesek)
print(f"A többiek pozíciója: ")
for i in vesztesek:
    print(f"{i}. játékos, {hanyadik_mezon_vagyunk[i - 1]}. mező")
