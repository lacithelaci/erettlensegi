class Cegesauto:
    def __init__(self, nap, ora_perc, rendszam, az, km, kibe):
        self.nap = int(nap)
        self.ora_perc = ora_perc
        self.rendszam = rendszam
        self.az = int(az)
        self.km = int(km)
        self.kibe = int(kibe)

    def __repr__(self):
        return f"{self.nap} {self.ora_perc} {self.rendszam} {self.az} {self.km} {self.kibe}"

    def kibe_szoveg(self):
        if self.kibe == 0:
            return "ki"
        else:
            return "be"


lista = []
f = open("autok.txt")
for i in f:
    i = i.strip().split()
    lista.append(Cegesauto(*i))
kivittek = [i for i in lista if i.kibe == 0]
print(f"2. feladat\n{kivittek[-1].nap}. nap rendszám: {kivittek[-1].rendszam} ")
print(f"3. feladat")
nap = int(input("Nap:"))
print(f"Forgalom a(z) {nap}. napon: ")
for i in lista:
    if i.nap == nap:
        print(f"{i.nap} {i.rendszam} {i.az} {i.kibe_szoveg()} ")
print(f"4. feladat")
szotar = {}
for i in lista:
    szotar[i.rendszam] = szotar.get(i.rendszam, 0) + 1
db = 0
for i in szotar.values():
    if i % 2 == 1:
        db += 1
print(f"A hónap végén {db} autót nem hoztak vissza. ")
print(f"5. feladat")
halmaz = set(i.rendszam for i in lista)
szum = 0
kint = False
bent = False
kintkm = 0
bentkm = 0
for y in sorted(halmaz):
    kint = False
    bent = False
    szum = 0
    for i in lista:
        if i.rendszam == y:
            if i.kibe == 0:
                kint = True
                kintkm = i.km
            else:
                bent = True
                bentkm = i.km
            if kint and bent:
                szum += bentkm - kintkm
    print(f"{y} {szum} km ")
print(f"6. feladat ")
halmaz = set(i.az for i in lista)
szum = 0
masz = 0
kint = False
bent = False
kintkm = 0
bentkm = 0
az=None
for y in sorted(halmaz):
    kint = False
    bent = False
    szum = 0
    for i in lista:
        if i.az == y:
            if i.kibe == 0:
                kint = True
                kintkm = i.km
            else:
                bent = True
                bentkm = i.km
            if kint and bent:
                kint = False
                bent = False
                szum = bentkm - kintkm
        if masz < szum:
            az=y
            masz = szum
print(f"Leghosszabb út: {masz} km, személy: {az} ")
print(f"7. feladat ")
rendszam=input("Rendszám: CEG304 ")
f=open(f"{rendszam}.txt","w")
for i in lista:
    if i.rendszam==rendszam:
        if i.kibe_szoveg()=="ki":
            f.write(f"{i.az}\t{i.nap}\t{i.ora_perc}\t{i.km} km")
        else:
            f.write(f"\t{i.az}\t{i.nap}\t{i.ora_perc}\t{i.km} km\n")
print(f"Menetlevél kész. ")
