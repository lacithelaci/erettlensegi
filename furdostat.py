class Furdo:
    def __init__(self, vendegaz, furdoaz, kibe, ora, perc, ms):
        self.vendegaz = int(vendegaz)
        self.furdoaz = int(furdoaz)
        self.kibe = int(kibe)
        self.ora = int(ora)
        self.perc = int(perc)
        self.ms = int(ms)

    def __repr__(self):
        return f"{self.vendegaz} {self.furdoaz} {self.kibe} {self.ora} {self.perc} {self.ms}"

    def msbe(self):
        return self.ora * 3600 + self.perc * 60 + self.ms


def vissza(ms):
    perc = ms // 60
    ora = perc // 60
    perc = perc - ora * 60
    msbe = ms - (perc * 60 + (ora * 60 * 60))
    return f"{ora}:{perc}:{msbe}"


f = open("furdoadat.txt")
lista = []
for i in f:
    i = i.strip().split()
    lista.append(Furdo(*i))
kilepes = [i for i in lista if i.kibe == 1 and i.furdoaz == 0]
print(
    f"2. feladat\nAz első vendég {kilepes[0].ora}:{kilepes[0].perc}:{kilepes[0].ms}-kor lépett ki az öltözőből.\nAz utolsó vendég {kilepes[-1].ora}:{kilepes[-1].perc}:{kilepes[-1].ms}-kor lépett ki az öltözőből. ")
print(f"3. feladat")
szotar = {}
for i in lista:
    if i.furdoaz != 0 and i.kibe == 0:
        szotar[i.vendegaz] = szotar.get(i.vendegaz, 0) + 1
egyreszleges = [i for i in szotar.values() if i == 1]
print(f"A fürdőben {len(egyreszleges)} vendég járt csak egy részlegen. ")
print(f"4. feladat")
halmaz = set(i.vendegaz for i in lista)
bejott = False
kijott = False
beido = None
kiido = None
masz = 0
kulonbseg = 0
vendegaz = None
for y in halmaz:
    bejott = False
    kijott = False
    beido = None
    kiido = None
    for i in lista:
        if y == i.vendegaz:
            if i.furdoaz == 0 and i.kibe == 0:
                beido = i.msbe()
                bejott = True
            if i.furdoaz == 0 and i.kibe == 1:
                kiido = i.msbe()
                kijott = True
            if bejott and kijott:
                kulonbseg = beido - kiido
                bejott = False
                kijott = False

            if masz < kulonbseg:
                masz = kulonbseg
                vendegaz = y
print(f"{vendegaz}. vendég {vissza(masz)}")
hat_kilenc = {}
kilenc_tizenhat = {}
tizenhat_plusz = {}
for i in lista:
    if i.ora < 9 and i.furdoaz == 0 and i.kibe == 1:
        hat_kilenc[i.vendegaz] = hat_kilenc.get(i.vendegaz, 0) + 1
    elif i.ora < 16 and i.furdoaz == 0 and i.kibe == 1:
        kilenc_tizenhat[i.vendegaz] = kilenc_tizenhat.get(i.vendegaz, 0) + 1
    elif i.ora < 20 and i.furdoaz == 0 and i.kibe == 1:
        tizenhat_plusz[i.vendegaz] = tizenhat_plusz.get(i.vendegaz, 0) + 1
print(
    f"5. feladat\n6-9 óra között {len(hat_kilenc)} vendég\n9-16 óra között {len(kilenc_tizenhat)} vendég\n16-20 óra között {len(tizenhat_plusz)} vendég ")
halmaz = set(i.vendegaz for i in lista)
bejott = False
kijott = False
beido = None
kiido = None
masz = 0
kulonbseg = 0
vendegaz = None
f = open("szauna.txt", "w")
for y in halmaz:
    bejott = False
    kijott = False
    beido = None
    kiido = None
    szum = 0
    for i in lista:
        if y == i.vendegaz:
            if i.furdoaz == 3 and i.kibe == 0:
                beido = i.msbe()
                bejott = True
            if i.furdoaz == 3 and i.kibe == 1:
                kiido = i.msbe()
                kijott = True
            if bejott and kijott:
                kulonbseg = beido - kiido
                bejott = False
                kijott = False
                szum += kulonbseg
    f.write(f"{y} {vissza(-szum)}\n")
szotar = {}
reszlegek = set(i.furdoaz for i in lista)
seged = []
for y in reszlegek:
    seged = []
    for i in lista:
        if i.furdoaz == y:
            if i.vendegaz not in seged:
                seged.append(i.vendegaz)
                szotar[i.furdoaz] = szotar.get(i.furdoaz, 0) + 1


def reszlegek(a):
    szotar = {1: "Uszoda", 2: "Szaunák", 3: "Gyógyvizes medencék", 4: "Strand"}
    for index, i in szotar.items():
        if index == a:
            return i


for index, i in szotar.items():
    if index != 0:
        print(f"{reszlegek(index)}: {i} ")
