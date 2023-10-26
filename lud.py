f = open("dobasok.txt")
dobasok = []
for i in f:
    i = i.split()
    for y in i:
        dobasok.append(int(y))
f = open("osvenyek.txt")
osvenyek = []
for i in f:
    osvenyek.append(i.strip())
print(f"2. feladat\nA dobások száma: {len(dobasok)}\nAz ösvények száma: {len(osvenyek)}")
print(f"3. feladat")
for i in sorted(osvenyek, key=lambda i: (len(i)), reverse=True):
    leghosszabb = len(i)
    break
for index, i in enumerate(osvenyek):
    if len(i) == leghosszabb:
        print(f"Az egyik leghosszabb a(z) {index + 1}. ösvény, hossza: {leghosszabb}")

print(f"4. feladat ")
osvenyszam = int(input("Adja meg egy ösvény sorszámát! "))
jatekosszam = int(input("Adja meg a játékosok számát! "))
print("5. feladat")
megadott_osveny = osvenyek[osvenyszam - 1]
szotar = {}
for i in megadott_osveny:
    szotar[i] = szotar.get(i, 0) + 1
for index, i in szotar.items():
    print(f"{index}: {i} darab ")
f = open("kulonleges.txt", "w")
for index, i in enumerate(megadott_osveny):
    if i != "M":
        f.write(f"{index + 1}\t{i}\n")
print("7. feladat")
db = 0
kezdet = db
osszeg = -1
lepesszam = 0
lepesek = []
while jatekosszam != db:
    if osszeg >= len(megadott_osveny):
        db += 1
        kezdet = db
        osszeg = -1
        lepesek.append(lepesszam)
        lepesszam = 0
    osszeg += dobasok[kezdet]
    kezdet += jatekosszam
    lepesszam += 1
leghamarabb_vegetert = min(lepesek)
db = 0
for i in lepesek:
    db += 1
    if leghamarabb_vegetert == i:
        print(f"A játék a(z) {leghamarabb_vegetert}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: {db} ")
print(f"8. feladat ")

db = 0
kezdet = db
osszeg = -1
lepesszam = 0
lepesek = []
szamlalo = 0
xedik = []
kulonlista = []
db3 = 0
while jatekosszam != db:
    osszeg += dobasok[kezdet]
    if osszeg >= len(megadott_osveny):
        db += 1
        kezdet = db
        osszeg = -1
        lepesek.append(lepesszam)
        lepesszam = 0
        db3 = 0
    if megadott_osveny[osszeg] == "V":
        osszeg -= dobasok[kezdet]
    elif megadott_osveny[osszeg] == "E":
        osszeg += dobasok[kezdet]
    kezdet += jatekosszam
    lepesszam += 1
    if osszeg > 0:
        db3 += 1
    if db3 == 55:
        kulonlista.append(osszeg)

db = 0
ugyanaz = [3, 1, 4]
print("Nyertes(ek):", end=" ")
leggyorsabbak = min(lepesek)
for i in lepesek:
    db += 1
    if leggyorsabbak == i:
        print(db, end=" ")
osszeg = 0
print("A többiek pozíciója: ")
for i in range(1, 4):
    print(f"{i}. játékos, {kulonlista[i - 1] + ugyanaz[i - 1]}. mező")
