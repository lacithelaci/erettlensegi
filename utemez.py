class Tabor:
    def __init__(self, kezdhonap, kezdnap, veghonap, vegnap, tanulok, program):
        self.kezdhonap = int(kezdhonap)
        self.kezdnap = int(kezdnap)
        self.veghonap = int(veghonap)
        self.vegnap = int(vegnap)
        self.tanulok = tanulok
        self.program = program

    def __repr__(self):
        return f"{self.kezdhonap} {self.kezdnap} {self.veghonap} {self.vegnap} {self.tanulok} {self.program}"

    def jelenkezok_szama(self):
        return len(self.tanulok)


f = open("taborok.txt")
lista = []
for i in f:
    i = i.strip().split("\t")
    lista.append(Tabor(*i))
print(
    f"2. feladat\nAz adatsorok száma: {len(lista)}\nAz először rögzített tábor témája: {lista[0].program}\nAz utoljára rögzített tábor témája: {lista[-1].program} ")
print("3. feladat")
zenei = [i for i in lista if i.program == "zenei"]
for i in zenei:
    print(f"Zenei tábor kezdődik {i.kezdhonap}. hó {i.kezdnap}. napján. ")
print(f"4. feladat\nLegnépszerűbbek:")
legtobb = [i.jelenkezok_szama() for i in lista]
masz = max(legtobb)
for i in lista:
    if i.jelenkezok_szama() == masz:
        print(f"{i.kezdhonap} {i.kezdnap} {i.program} ")
print(f"6. feladat")
ho = 8
nap = 1
db = 0
for i in lista:
    if i.kezdhonap * 31 + i.kezdnap <= ho * 31 + nap <= i.veghonap * 31 + i.vegnap:
        db += 1
print(f"Ekkor éppen {db} tábor tart. ")
print(f"7. feladat")
tanulo = input(f"Adja meg egy tanuló betűjelét: L ")
egytanulo = [i for i in lista if tanulo in i.tanulok]
f = open("egytanulo.txt", "w", encoding="utf-8")
for i in sorted(egytanulo, key=lambda i: (i.kezdhonap, i.kezdnap)):
    f.write(f"{i.kezdhonap}.{i.kezdnap}-{i.veghonap}.{i.vegnap}. {i.program}\n")
seged = []
for i in sorted(egytanulo, key=lambda i: (i.kezdhonap, i.kezdnap)):
    seged.append(i.kezdhonap * 31 + i.kezdnap)
    seged.append(i.veghonap * 31 + i.vegnap)

if sorted(seged) == seged:
    if len(set(seged)) == len(seged):
        print("Elmehet mindegyik táborba")
    else:
        print("Nem mehet elmindegyik táborba")
else:
    print(f"Nem mehet el mindegyik táborba. ")
