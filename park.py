class Park:
    def __init__(self, elso, utolso, szin, sorszam):
        self.sorszam = sorszam
        self.elso = int(elso)
        self.utolso = int(utolso)
        self.szin = szin

    def __repr__(self):
        return f"{self.elso} {self.utolso} {self.szin} {self.sorszam}"


f = open("felajanlas.txt")
ssz = 0
elso_sor = int(f.readline())
lista = []
for i in f:
    i = i.strip().split()
    ssz += 1
    lista.append(Park(*i, ssz))
print(f"2. feladat\nA felajánlások száma: {len(lista)} ")
kethelyen = []
for i in lista:
    if i.elso > i.utolso:
        kethelyen.append(i.sorszam)
print("3. feladat\nA bejárat mindkét oldalán ültetők:", *kethelyen)
print("4. feladat")
ssz = int(input("Adja meg az ágyás sorszámát!"))
db = 0
listas = []
listas.append(ssz)
volt = 0
elso_szin = None
szines_halmaz = set()
for i in lista:

    if i.elso < i.utolso:
        for y in range(i.elso, i.utolso + 1):
            if y in listas:
                db += 1
                volt += 1
                if volt == 1:
                    elso_szin = i.szin
                szines_halmaz.add(i.szin)
    else:
        for y in range(i.elso, elso_sor + 1):
            if y in listas:
                db += 1
                volt += 1
                if volt == 1:
                    elso_szin = i.szin
                szines_halmaz.add(i.szin)
            else:
                for y2 in range(1, i.utolso + 1):

                    if y2 in listas:
                        db += 1
                        volt += 1
                        if volt == 1:
                            elso_szin = i.szin
                        szines_halmaz.add(i.szin)

print(f"A felajánlók száma: {db}")
if elso_szin == None:
    print("Ezt az ágyást nem ültetik be.")
else:
    print(f"A virágágyás színe, ha csak az első ültet: {elso_szin}")
if len(szines_halmaz) != 0:
    print(f"A virágágyás színei:", *szines_halmaz)
print("5. feladat")


def kivonas(a, b, c):
    if a < b:
        return b - a + 1
    else:
        return (c - a) + b + 1


agyasos_halmaz = set()
for i in lista:
    if i.elso < i.utolso:
        for y in range(i.elso, i.utolso + 1):
            agyasos_halmaz.add(y)
    else:
        for y2 in range(1, i.utolso + 1):
            agyasos_halmaz.add(y2)
        for y in range(i.elso, elso_sor + 1):
            agyasos_halmaz.add(y)
szum = 0
for i in lista:
    szum += kivonas(i.elso, i.utolso, elso_sor)
if len(agyasos_halmaz) == elso_sor:
    print("Minden ágyás beültetésére van jelentkező.")
elif szum > elso_sor:
    print("Átszervezéssel megoldható a beültetés.")
else:
    print("A beültetés nem oldható meg.")
agyasok = set()
f = open("szinek.txt", "w")
ures = "# 0"
szamlalo = 0
volte = False
for y in range(1, elso_sor + 1):
    for i in lista:
        szamlalo += 1
        if i.elso < i.utolso:
            for xd in range(i.elso, i.utolso + 1):
                if xd == y:
                    if not volte:
                        ures = f"{i.szin} {i.sorszam}"
                        szamlalo = 0
                        volte = True
        else:
            for xd in range(i.elso, elso_sor + 1):
                if xd == y:
                    if not volte:
                        ures = f"{i.szin} {i.sorszam}"
                        szamlalo = 0
                        volte = True

                else:
                    for y2 in range(1, i.utolso + 1):

                        if y2 == y:
                            if not volte:
                                ures = f"{i.szin} {i.sorszam}"
                                szamlalo = 0
                                volte = True
        if szamlalo == elso_sor:
            ures = "# 0"
    f.write(f"{ures}\n")
    volte = False
