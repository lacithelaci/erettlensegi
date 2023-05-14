import math


class Jel:
    def __init__(self, ora, perc, ms, x, y):
        self.ora = int(ora)
        self.perc = int(perc)
        self.ms = int(ms)
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"{self.ora} {self.perc} {self.ms} {self.x} {self.y}"

    def msbe(self):
        return self.ora * 3600 + self.perc * 60 + self.ms


def ora_perc_ms(ms):
    perc = ms // 60
    ora = perc // 60
    perc = perc - ora * 60
    ms = ms - (perc * 60 + ora * 3600)
    return f"{ora}:{perc}:{ms}"


def eltelt(a, b):
    return a - b


lista = []
f = open("jel.txt")
for i in f:
    i = i.strip().split()
    lista.append(Jel(*i))
print(f"2. feladat\nAdja meg a jel sorszámát! 3 ")
sorszam = 3
db = 0
for i in lista:
    db += 1
    if db == sorszam:
        print(f"x={i.x} y={i.y} ")
        break
print(f"4. feladat ")
print(
    f"Időtartam: {ora_perc_ms(eltelt(lista[-1].ora * 3600 + lista[-1].perc * 60 + lista[-1].ms, lista[0].ora * 3600 + lista[0].perc * 60 + lista[0].ms))}")
print(f"5. feladtat")
y = [i.y for i in lista]
x = [i.x for i in lista]
print(f"Bal alsó: {min(x)} {min(y)}, jobb felső: {max(x)} {max(y)}\n6. feladat")
szum = 0
for i in range(0, len(lista) - 1):
    szum += math.sqrt((lista[i].x - lista[i + 1].x) ** 2 + (lista[i].y - lista[i + 1].y) ** 2)
print(f"Elmozdulás: {round(szum, 3)} egység ")
f = open("kimaradt.txt", "w", encoding="utf-8")
koordinata_valtozas_x = 0
koordinata_valtozas_y = 0
idoelteres = 0
for i in range(0, len(lista) - 1):
    if abs(lista[i].x - lista[i + 1].x) > 10:
        koordinata_valtozas_x = abs(lista[i].x - lista[i + 1].x) // 11
    if abs(lista[i].y - lista[i + 1].y) > 10:
        koordinata_valtozas_y = abs(lista[i].y - lista[i + 1].y) // 11
    if lista[i + 1].msbe() - lista[i].msbe() > 5 * 60:
        idoelteres = (lista[i + 1].msbe() - lista[i].msbe()) // (5 * 60 + 1)
    if koordinata_valtozas_x != 0 or koordinata_valtozas_y != 0 or idoelteres != 0:
        if koordinata_valtozas_x > idoelteres or koordinata_valtozas_y > idoelteres:
            if koordinata_valtozas_x > koordinata_valtozas_y:
                f.write(
                    f"{lista[i + 1].ora} {lista[i + 1].perc} {lista[i + 1].ms} koordináta-eltérés {koordinata_valtozas_x}\n")
            else:
                f.write(
                    f"{lista[i + 1].ora} {lista[i + 1].perc} {lista[i + 1].ms} koordináta-eltérés {koordinata_valtozas_y}\n")
        else:
            f.write(f"{lista[i + 1].ora} {lista[i + 1].perc} {lista[i + 1].ms} időeltérés {idoelteres}\n")
        koordinata_valtozas_x = 0
        koordinata_valtozas_y = 0
        idoelteres = 0
