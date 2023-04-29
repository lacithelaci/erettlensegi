class Utazas:
    def __init__(self, megallo, felszall_datum, az, berlet_tipus, ervenyes):
        self.megallo = int(megallo)
        self.felszall_datum = felszall_datum
        self.az = int(az)
        self.berlet_tipus = berlet_tipus
        self.ervenyes = int(ervenyes)

    def __repr__(self):
        return f"{self.megallo} {self.felszall_datum} {self.az} {self.berlet_tipus} {self.ervenyes}"

    def ervenyese(self):
        if self.ervenyes < int(self.felszall_datum[0:8]) and len(str(self.ervenyes)) > 3 or self.ervenyes == 0:
            return False
        else:
            return True

    def ervenyes_szoveg(self):
        return str(self.ervenyes)


f = open("utasadat.txt")
lista = []
for i in f:
    i = i.strip().split()
    lista.append(Utazas(*i))
print(f"2. feladat\nA buszra {len(lista)} utas akart felszállni.\n3. feladat")
ervenytelen = [i.az for i in lista if
               (i.ervenyes < int(i.felszall_datum[0:8]) and len(str(i.ervenyes)) > 2) or i.ervenyes == 0]
print(f"A buszra {len(ervenytelen)} utas nem szállhatott fel.\n4. feladat")
szotar = {}
for i in sorted(lista, key=lambda i: i.megallo):
    szotar[i.megallo] = szotar.get(i.megallo, 0) + 1
legtobb_felszallt = max(szotar.values())
for index, i in szotar.items():
    if legtobb_felszallt == i:
        print(f"A legtöbb utas ({legtobb_felszallt} fő) a {index}. megállóban próbált felszállni. ")
        break
print("5. feladat")
ingyenes = [i.az for i in lista if i.berlet_tipus in ["NYP", "RVS", "GYK"] and i.ervenyese()]
kedvezmenyes = [i.az for i in lista if i.berlet_tipus in ["TAB", "NYB", ] and i.ervenyese()]
print(f"Ingyenesen utazók száma: {len(ingyenes)} fő\nA kedvezményesen utazók száma: {len(kedvezmenyes)} fő")


def napokszama(e1, h1, n1, e2, h2, n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365 * e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1 * 306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2 = 365 * e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2 * 306 + 5) // 10 + n2 - 1
    return d2 - d1


f = open("figyelmeztetes.txt", "w", encoding="utf-8")
for i in lista:
    if len(i.ervenyes_szoveg()) > 2:
        if 0 <= (napokszama(int(i.felszall_datum[0:4]), int(i.felszall_datum[4:6]), int(i.felszall_datum[6:8]),
                            int(i.ervenyes_szoveg()[0:4]), int(i.ervenyes_szoveg()[4:6]),
                            int(i.ervenyes_szoveg()[6:8]))) <= 3:
            f.write(f"{i.az} {i.ervenyes_szoveg()[0:4]}-{(i.ervenyes_szoveg()[4:6])}-{int(i.ervenyes_szoveg()[6:8])}\n")

