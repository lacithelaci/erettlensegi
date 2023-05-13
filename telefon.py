class Telefon:
    def __init__(self, kezdes_ora, kezdes_perc, kezdes_ms, vege_ora, vege_perc, vege_ms, hivoaz):
        self.kezdes_ora = int(kezdes_ora)
        self.kezdes_perc = int(kezdes_perc)
        self.kezdes_ms = int(kezdes_ms)
        self.vege_ora = int(vege_ora)
        self.vege_perc = int(vege_perc)
        self.vege_ms = int(vege_ms)
        self.hivoaz = hivoaz

    def __repr__(self):
        return f"{self.kezdes_ora} {self.kezdes_perc} {self.kezdes_ms} {self.vege_ora} {self.vege_perc} {self.vege_ms} {self.hivoaz}"


def mpbe(o, p, ms):
    return o * 3600 + p * 60 + ms


def vissza(ms):
    perc = ms // 60
    ora = perc // 60
    perc = perc - ora * 60
    msbe = ms - (perc * 60 + (ora * 60 * 60))
    return f"{ora} {perc} {msbe}"


f = open("hivas.txt")
lista = []
db = 0
for i in f:
    db += 1
    i = i.strip().split()
    lista.append(Telefon(*i, db))
hivasok = {}
for i in lista:
    hivasok[i.kezdes_ora] = hivasok.get(i.kezdes_ora, 0) + 1
print(f"3. feladat")
for index, i in hivasok.items():
    print(f"{index} ora {i} hivas")
print(f"4. feladat")
for i in sorted(lista,
                key=lambda i: mpbe(i.vege_ora, i.vege_perc, i.vege_ms) - mpbe(i.kezdes_ora, i.kezdes_perc, i.kezdes_ms),
                reverse=True):
    print(
        f"A leghosszabb ideig vonalban levo hivo {i.hivoaz}. sorban szerepel,a hivas hossza: {mpbe(i.vege_ora, i.vege_perc, i.vege_ms) - mpbe(i.kezdes_ora, i.kezdes_perc, i.kezdes_ms)} masodperc.")
    break
print("5. feladat\nAdjon meg egy idopontot! (ora perc masodperc) 10 11 12")
ora = int(input())
perc = int(input())
ms = int(input())
megadott_idopontig = [i for i in lista if mpbe(ora, perc, ms) >= mpbe(i.kezdes_ora, i.kezdes_perc, i.kezdes_ms)]
db = 0
if len(megadott_idopontig) > 0:
    for i in megadott_idopontig:
        if mpbe(ora, perc, ms) >= mpbe(i.kezdes_ora, i.kezdes_perc, i.kezdes_ms) and mpbe(ora, perc, ms) <= mpbe(
                i.vege_ora, i.vege_perc, i.vege_ms):
            db += 1
if len(megadott_idopontig) == 0:
    print(f"Nem volt beszélő.")
elif db - 1 == -1:
    print(f"Nem volt beszélő.")
else:
    print(f"A varakozok szama: {db - 1} a beszelo a {len(megadott_idopontig) - (db - 1)}. hivo.")
print("6. feladat")
ervenyes = [i for i in lista if
            mpbe(i.vege_ora, i.vege_perc, i.vege_ms) >= 8 * 3600 and mpbe(i.kezdes_ora, i.kezdes_perc,
                                                                          i.kezdes_ms) <= 12 * 3600]
elozo = 0
jelenlegi = 0
az = None
az_hivas_kezdete = None
ervenyes_hivas_mp = []
for i in ervenyes:
    jelenlegi = mpbe(i.vege_ora, i.vege_perc, i.vege_ms)
    if elozo < jelenlegi:
        az = i.hivoaz
        az_hivas_kezdete = mpbe(i.kezdes_ora, i.kezdes_perc, i.kezdes_ms)
        ervenyes_hivas_mp.append(mpbe(i.vege_ora, i.vege_perc, i.vege_ms))
    elozo = jelenlegi
print(
    f"Az utolso telefonalo adatai a(z) {az}. sorban vannak, {ervenyes_hivas_mp[-2] - az_hivas_kezdete} masodpercig vart.")
f = open("sikeres.txt", "w")
elozo = 0
jelenlegi = 0
nemvolt = False
for i in ervenyes:
    jelenlegi = mpbe(i.vege_ora, i.vege_perc, i.vege_ms)
    if elozo < jelenlegi:
        if mpbe(i.kezdes_ora, i.kezdes_perc, i.kezdes_ms) <= 8 * 3600 and nemvolt == False:
            f.write(f"{i.hivoaz} {8} {0} {0} {vissza(jelenlegi)}\n")
            nemvolt = True
        else:
            f.write(f"{i.hivoaz} {vissza(elozo)} {vissza(jelenlegi)}\n")
    elozo = jelenlegi
