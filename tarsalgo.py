class Tarsalgo:
    def __init__(self, ora, perc, az, kibe):
        self.ora = int(ora)
        self.perc = int(perc)
        self.az = int(az)
        self.kibe = kibe

    def __repr__(self):
        return f"{self.ora} {self.perc} {self.az} {self.kibe}"

    def osszperc(self):
        return self.ora * 60 + self.perc


f = open("ajto.txt")
lista = []
for i in f:
    i = i.strip().split()
    lista.append(Tarsalgo(*i))
print(f"2. feladat\nAz első belépő: {lista[0].az} ")
ki = [i.az for i in lista if i.kibe == "ki"]
print(f"Az utolsó kilépő: {ki[-1]} ")
f = open("athaladas.txt", "w")
szotar = {}
for i in lista:
    szotar[i.az] = szotar.get(i.az, 0) + 1
for index, db in sorted(szotar.items()):
    f.write(f"{index} {db}\n")
print("4. feladat\nA végén a társalgóban voltak:", end=" ")
for index, db in sorted(szotar.items()):
    if db % 2 == 1:
        print(index, end=" ")
db = 0
masz = 0
ora_perc = None
for i in lista:
    if i.kibe == "ki":
        db -= 1
    else:
        db += 1
    if db > masz:
        masz = db
        ora_perc = f"{i.ora}:{i.perc}"
print(f"\n5. feladat\nPéldául {ora_perc}-kor voltak a legtöbben a társalgóban. ")
print("6. feladat")
az = int(input("Adja meg a személy azonosítóját! 22 "))
print("7. feladat")
for i in lista:
    if i.az == az and i.kibe == "be":
        print(f"{i.ora}:{i.perc}-", end="")
    elif i.az == az and i.kibe == "ki":
        print(f"{i.ora}:{i.perc}")
print("8. feladat")
kollega = [i for i in lista if i.az == az]
szum = 0
bent_van = False
kint_van = False
bent_ido = None
kint_ido = None
for i in kollega:
    if i.kibe == "be":
        bent_ido = i.osszperc()
        bent_van = True
    else:
        kint_ido = i.osszperc()
        kint_van = True
    if bent_van and kint_van:
        szum += kint_ido - bent_ido
        kint_van = False
        bent_van = False
if len(kollega) % 2 != 0:
    szum += 15 * 60 - (kollega[-1].ora * 60 + kollega[-1].perc)
    print(f"A(z) {az}. személy összesen {szum} percet volt bent, a megfigyelés végén a társalgóban volt. ")
else:
    print(f"A(z) {az}. személy összesen {szum} percet volt bent, a megfigyelés végén nem volt a társalgóban. ")
