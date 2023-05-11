class Kerites:
    def __init__(self, hazszam, hossz, szin):
        self.hazszam = int(hazszam)
        self.hossz = int(hossz)
        self.szin = szin
        self.igazi_hazszam = 0

    def __repr__(self):
        return f"{self.hazszam} {self.hossz} {self.szin}"


f = open("kerites.txt")
lista = []
for i in f:
    i = i.strip().split()
    lista.append(Kerites(*i))
print(f"2. feladat\nAz eladott telkek száma: {len(lista)} ")
paros = 2
paratlan = 1
for i in lista:
    if i.hazszam == 0:
        i.igazi_hazszam = paros
        paros += 2
    else:
        i.igazi_hazszam = paratlan
        paratlan += 2
print("3. feladat")
if lista[-1].igazi_hazszam % 2 == 0:
    print(f"A páros oldalon adták el az utolsó telket.\nAz utolsó telek házszáma: {lista[-1].igazi_hazszam} ")
else:
    print(f"A páratlan oldalon adták el az utolsó telket.\nAz utolsó telek házszáma: {lista[-1].igazi_hazszam} ")
print(f"4. feladat")
paratlanok = [i for i in lista if i.hazszam == 1]
elozo = ""
jelenlegi = None
for i in paratlanok:
    jelenlegi = i.szin
    if jelenlegi == elozo and jelenlegi != "#" and jelenlegi != ":":
        print(f"A szomszédossal egyezik a kerítés színe: {i.igazi_hazszam} ")
        break
    elozo = jelenlegi
print("5. feladat")
hazszam = int(input(f"Adjon meg egy házszámot! 83 "))
szinek = "QWERTZUIOPLKJHGFDSAYXCVBNM"
festett_szinek = set()
halmaz = set()
for i in szinek:
    halmaz.add(i)
for i in lista:
    if i.igazi_hazszam == hazszam:
        print(f"A kerítés színe / állapota: {i.szin} ")
    if i.igazi_hazszam in [hazszam, hazszam + 2, hazszam - 2]:
        festett_szinek.add(i.szin)
lehetseges = halmaz.difference(festett_szinek)
for i in sorted(lehetseges):
    print(f"Egy lehetséges festési szín: {i} ")
    break
semmi = " "
f = open(f"utcakep.txt", "w")
for i in lista:
    if i.hazszam == 1:
        f.write(f"{i.szin * i.hossz}")
f.write(f"\n")
for i in lista:
    if i.hazszam == 1:
        i.igazi_hazszam = str(i.igazi_hazszam)
        f.write(f"{i.igazi_hazszam}{(i.hossz - (len(i.igazi_hazszam))) * semmi}")
