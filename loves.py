class Verseny:
    def __init__(self, rajtszam, loves):
        self.rajtszam = rajtszam
        self.loves = loves

    def __repr__(self):
        return f"{self.rajtszam} {self.loves}"

    def tobbtalalat(self):
        sor = self.loves.split("-")
        seged = []

        for i in sor:
            seged.append(len(i))

        return seged

    def celtero(self):
        db = 0
        seged = []

        for i in self.loves:

            db += 1
            if i == "+":
                seged.append(db)

        return seged


f = open("verseny.txt")
fajl_hossz = f.readline()
db = 0
lista = []

for i in f:

    i = i.strip()
    db += 1
    lista.append(Verseny(db, i))

print(f"2. feladat")

tobb_talalatos = [i.rajtszam for i in lista if max(i.tobbtalalat()) > 1]
print(f"Az egymast kovetoen tobbszor talalo versenyzok:", *tobb_talalatos)

print("3. feladat")

for i in sorted(lista, key=lambda i: len(i.loves), reverse=True):
    print(f"A legtobb lovest leado versenyzo rajtszama: {i.rajtszam}")
    break


def loertek(sor):
    aktpont = 20
    ertek = 0

    for i in range(0, len(sor)):

        if aktpont > 0 and sor[i] == '-':
            aktpont += -1

        else:
            ertek += aktpont

    return ertek


print(f"5. feladat\nAdjon meg egy rajtszamot! 2 ")
rajtszam = int(input())

for i in lista:

    if rajtszam == i.rajtszam:

        print(f"5a. feladat: Celt ero lovesek:", *i.celtero())
        print(f"5b. feladat: Az eltalalt korongok szama:", len(i.celtero()))
        print(f"5c. feladat: A leghosszabb hibatlan sorozat hossza: ", max(i.tobbtalalat()))
        print(f"5d. feladat: A versenyzo pontszama:", loertek(i.loves))

f = open("sorrend.txt", "w", encoding="utf-8")
elozo = ""
jelenlegi = None
helyezes = 0

for i in sorted(lista, key=lambda i: loertek(i.loves), reverse=True):
    jelenlegi = loertek(i.loves)

    if elozo != jelenlegi:
        helyezes += 1

    f.write(f"{helyezes} {i.rajtszam} {jelenlegi}\n")
    elozo = jelenlegi
