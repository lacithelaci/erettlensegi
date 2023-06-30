class Vonatok:
    def __init__(self, vonataz, allomasaz, ora, perc, erkezik_indul):
        self.vonataz = int(vonataz)
        self.allomasaz = int(allomasaz)
        self.ora = int(ora)
        self.perc = int(perc)
        self.erkezik_indul = erkezik_indul

    def __repr__(self):
        return f"{self.vonataz} {self.allomasaz} {self.ora} {self.perc} {self.erkezik_indul}"

    def osszperc(self):
        return self.ora * 60 + self.perc


f = open("vonat.txt")
lista = []
for i in f:
    lista.append(Vonatok(*i.strip().split("\t")))

print(f"2. feladat ")
allomasok = set(i.allomasaz for i in lista)
vonatok = set(i.vonataz for i in lista)

print(f"Az állomások száma: {len(allomasok)}\nA vonatok száma: {len(vonatok)}\n3. feladat")
maximum = 0
vonataz = None
allomasaz = None

for vonat in vonatok:
    adatok = []

    for i in lista:
        if vonat == i.vonataz:
            adatok.append(i)

    for i in range(1, len(adatok) - 1):

        if maximum < adatok[i + 1].osszperc() - adatok[i].osszperc() and adatok[i + 1].allomasaz == adatok[i].allomasaz:
            maximum = adatok[i + 1].osszperc() - adatok[i].osszperc()
            allomasaz = adatok[i + 1].allomasaz
            vonataz = adatok[i + 1].vonataz

print(f"A(z) {vonataz}. vonat a(z) {allomasaz}. állomáson {maximum} percet állt.\n4. feladat")

vonataz = int(input("Adja meg egy vonat azonosítóját! 2"))
ora = int(input("Adjon meg egy időpontot (óra perc)! 7 16 "))
perc = int(input())
print(f"5. feladat")

megadott_vonat = [i for i in lista if vonataz == i.vonataz]

if megadott_vonat[-1].osszperc() - megadott_vonat[0].osszperc() == 2 * 60 + 22:
    print(f"A(z) {vonataz}. vonat útja pontosan az előírt ideig tartott.")

elif megadott_vonat[-1].osszperc() - megadott_vonat[0].osszperc() >= (2 * 60 + 22):

    print(
        f"A(z) {vonataz}. vonat útja {megadott_vonat[-1].osszperc() - megadott_vonat[0].osszperc() - (2 * 60 + 22)} perccel hosszabb volt az előírtnál")
else:

    print(
        f"A(z) {vonataz}. vonat útja {abs(megadott_vonat[-1].osszperc() - megadott_vonat[0].osszperc() - (2 * 60 + 22))} perccel rövidebb volt az előírtnál.")

f = open(f"halad{vonataz}.txt", "w", encoding="utf-8")

for i in megadott_vonat:

    if i.erkezik_indul == "E":
        f.write(f"{i.allomasaz}. állomás: {i.ora}:{i.perc}\n")

print(f"7. feladat")
for vonat in vonatok:

    megadott_vonat = []

    for i in lista:
        if i.vonataz == vonat:
            megadott_vonat.append(i)

    for i in range(0, len(megadott_vonat) - 1):

        if megadott_vonat[i].osszperc() < ora * 60 + perc and megadott_vonat[i + 1].osszperc() > ora * 60 + perc:
            print(
                f"A(z) {megadott_vonat[i].vonataz}. vonat a {megadott_vonat[i].allomasaz}. és a {1 + (megadott_vonat[i].allomasaz)}. állomás között járt. ")

        elif megadott_vonat[i].osszperc() <= ora * 60 + perc and megadott_vonat[i + 1].osszperc() > ora * 60 + perc:
            print(f"A(z) {megadott_vonat[i].vonataz}. vonat a {megadott_vonat[i].allomasaz}. állomáson állt. ")
