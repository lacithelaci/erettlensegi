class Kosar:
    def __init__(self, az, tartalom):
        self.az = az
        self.tartalom = tartalom

    def __repr__(self):
        return f"{self.az} {self.tartalom}"


lista = []
seged = []
f = open("penztar.txt")
az = 0
for termek in f:
    termek = termek.strip()
    if termek != "F":
        seged.append(termek)
    else:
        az += 1
        lista.append(Kosar(az, seged))
        seged = []
print(f"2. feladat\nA fizetések száma: {len(lista)}")
print(f"3. feladat\nAz első vásárló {len(lista[0].tartalom)} darab árucikket vásárolt. ")
print("4. feladat")
sorszam = int(input("Adja meg egy vásárlás sorszámát! 2 "))
arucikk = input("Adja meg egy árucikk nevét! kefe ")
darabszam = int(input("Adja meg a vásárolt darabszámot! 2 "))
print("5. feladat ")
termek = [termek.az for termek in lista if arucikk in termek.tartalom]
print(
    f"Az első vásárlás sorszáma: {termek[0]}\nAz utolsó vásárlás sorszáma: {termek[-1]}\n{len(termek)} vásárlás során vettek belőle.\n6. feladat")


def ertek(darabszam):
    if darabszam == 1:
        return 500
    elif darabszam == 2:
        return 950
    else:
        return 950 + (darabszam - 2) * 400


print(f"{darabszam} darab vételekor fizetendő: {ertek(darabszam)}")
szotar = {}
for termek in lista:
    if termek.az == sorszam:
        for sor in termek.tartalom:
            szotar[sor] = szotar.get(sor, 0) + 1
print("7. feladat")
for termek, db in szotar.items():
    print(f"{db} {termek}")
f = open("osszeg.txt", "w")
halmaz = set(i.az for i in lista)
osszeg = 0
szotar = {}
for az in halmaz:
    osszeg = 0
    szotar = {}
    for termek in lista:
        if termek.az == az:
            for kosar in termek.tartalom:
                szotar[kosar] = szotar.get(kosar, 0) + 1
    for szam in szotar.values():
        osszeg += ertek(szam)
    f.write(f"{az}: {osszeg}\n")
