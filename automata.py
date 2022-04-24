class Csoki:
    def __init__(self, sorszam, db, ar):
        self.sorszam = int(sorszam)
        self.db = int(db)
        self.ar = int(ar)

    def __repr__(self):
        return f"{self.sorszam} {self.db} {self.ar}"

    def ertek(self):
        return self.ar * self.db


class Fabatka:
    def __init__(self, sorszam, vett, egy, ketto, ot, tiz, husz, otven, szaz):
        self.sorszam = int(sorszam)
        self.vett = int(vett)
        self.egy = int(egy)
        self.ketto = int(ketto)
        self.ot = int(ot)
        self.tiz = int(tiz)
        self.husz = int(husz)
        self.otven = int(otven)
        self.szaz = int(szaz)

    def __repr__(self):
        return f"{self.sorszam} {self.vett}"

    def fizetett(self):
        return self.szaz * 100 + self.otven * 50 + self.husz * 20 + self.tiz * 10 + self.ot * 5 + self.ketto * 2 + self.egy


f = open("csoki.txt")
elso_sor = f.readline()
csoki = []
for i in f:
    i = i.strip().split()
    csoki.append(Csoki(*i))
f = open("vasarlas.txt")
elso_sor = f.readline()
vasarlas = []
for i in f:
    i = i.strip().split()
    vasarlas.append(Fabatka(*i))
szum = 0
for i in csoki:
    szum += i.ertek()
print(f"2. feladat\nAz automatában {szum} fabatka értékű csokoládé van.\n3. feladat")
probaltak = set()
for i in vasarlas:
    probaltak.add(i.sorszam)
print("Ezekből a rekeszekből próbáltak venni:", end=" ")
for i in probaltak:
    print(i, end=" ")
print("\n4. feladat")
jorekesz = [i for i in csoki if i.db >= 7]
osszeg = 500
vehet = []
for i in jorekesz:
    if osszeg >= i.ar * 7:
        vehet.append(i.sorszam)
if len(vehet) != 0:
    print("Ezekből a rekeszekből vehet: ", *vehet)
else:
    print("Nincs elég pénze")
print("5. feladat")


def cimlet(a, b):
    fizetendo = a * b
    szoveg = ""
    szazas = fizetendo // 100
    fizetendo = fizetendo - (szazas * 100)
    if szazas != 0:
        szoveg += f"szazas:{szazas}"
    otven = fizetendo // 50
    fizetendo = fizetendo - (otven * 50)
    if otven != 0:
        szoveg += f" otven:{otven}"
    huszas = fizetendo // 20
    fizetendo = fizetendo - (huszas * 20)
    if huszas != 0:
        szoveg += f" huszas:{huszas}"
    tiz = fizetendo // 10
    fizetendo = fizetendo - (tiz * 10)
    if tiz != 0:
        szoveg += f" tizes:{tiz}"
    ot = fizetendo // 5
    fizetendo = fizetendo - (ot * 5)
    if ot != 0:
        szoveg += f" ötös:{ot}"
    ket = fizetendo // 2
    fizetendo = fizetendo - (ket * 2)
    if ket != 0:
        szoveg += f" kettes:{ket}"
    egy = fizetendo // 1
    fizetendo = fizetendo - (egy)
    if ket != 0:
        szoveg += f" egy:{egy}"
    return szoveg


rekesz = 5
dbszam = 5
for i in csoki:
    if i.sorszam == rekesz:
        print(f"{cimlet(dbszam, i.ar)}")
print("6. feladat")
f = open("rekesz7.txt", "w",encoding="utf-8")
dbszam = 0
ar = 0
for i in csoki:
    if i.sorszam == 7:
        ar = i.ar
        dbszam = i.db
rekesz7 = [i for i in vasarlas if i.sorszam == 7]
for index,i in enumerate(rekesz7):
    if dbszam >= i.vett:
        dbszam -= i.vett
        if i.vett * i.fizetett() >= ar * i.vett:
            f.write(f"{index+1}:{i.vett}\n")
        else:
            dbszam += i.vett
            f.write(f"{index+1}:nem volt elég pénz\n")
    else:
        f.write(f"{index+1}:kevés a csoki\n")
