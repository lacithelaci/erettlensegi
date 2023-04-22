class Hianyzasok:
    def __init__(self, honap, nap, vnev, knev, hianyzas):
        self.honap = int(honap)
        self.nap = int(nap)
        self.vnev = vnev
        self.knev = knev
        self.hianyzas = hianyzas

    def __repr__(self):
        return f"{self.honap} {self.nap} {self.vnev} {self.knev} {self.hianyzas}"

    def ossz_hiany(self):
        db = 0
        for hianyzasok in self.hianyzas:
            if hianyzasok == "X" or hianyzasok == "I":
                db += 1
        return db

    def teljes_nev(self):
        return f"{self.vnev} {self.knev}"


lista = []
f = open("naplo.txt")
nevek = ""
for adatok in f:
    adatok = adatok.strip().split()
    if adatok[0] == "#":
        datum = adatok
        nev = ""
    else:
        nev = adatok
    if nev != "":
        lista.append(Hianyzasok(datum[1], datum[2], *nev))
print(f"2. feladat\nA naplóban {len(lista)} bejegyzés van. ")
igazolt = 0
igazolatlan = 0
for tanulo in lista:
    for orak in tanulo.hianyzas:
        if orak == 'X':
            igazolt += 1
        elif orak == "I":
            igazolatlan += 1
print(f"3. feladat\nAz igazolt hiányzások száma {igazolt}, az igazolatlanoké {igazolatlan} óra. ")


def hetnapja(honap, nap):
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap - 1] + nap) % 7
    return napnev[napsorszam]


print("5. feladat")
honap = int(input("A hónap sorszáma=2 "))
nap = int(input("A nap sorszáma=3 "))
print(f"Azon a napon {hetnapja(honap, nap)} volt. ")
print("6. feladat")
hianyzasok = []
napnev = input("A nap neve=szerda ")
sorszama = int(input("Az óra sorszáma=3 "))
for tanulo in lista:
    if hetnapja(tanulo.honap, tanulo.nap) == napnev:
        if tanulo.hianyzas[sorszama - 1] == "I" or tanulo.hianyzas[sorszama - 1] == "X":
            hianyzasok.append(tanulo.hianyzas[sorszama - 1])
print(f"Ekkor összesen {len(hianyzasok)} óra hiányzás történt. ")
print("7. feladat ")
szotar = {}
for tanulo in lista:
    szotar[tanulo.teljes_nev()] = szotar.get(tanulo.teljes_nev(), 0) + tanulo.ossz_hiany()
legtobb_hianyzas = max(szotar.values())
print("A legtöbbet hiányzó tanulók:", end=" ")
for tanulo, hianyzas in szotar.items():
    if legtobb_hianyzas == hianyzas:
        print(tanulo, end=" ")


