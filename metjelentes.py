class Idojaras:
    def __init__(self, telepules, ido, szelirany_erosseg, homerseklet):
        self.telepules = telepules
        self.ido = ido
        self.szelirany_szelerosseg = szelirany_erosseg
        self.homerseklet = int(homerseklet)

    def __repr__(self):
        return f"{self.telepules} {self.ido} {self.szelirany_szelerosseg} {self.homerseklet}"


f = open("tavirathu13.txt")
lista = []

for i in f:
    lista.append(Idojaras(*i.strip().split()))

print(f"2. feladat")
telepules_kodja = input("Adja meg egy település kódját! Település: SM ")
megegyezo = [i for i in lista if i.telepules == telepules_kodja]
print(
    f"Az utolsó mérési adat a megadott településről {megegyezo[-1].ido[0:2]}:{megegyezo[-1].ido[2:4]}-kor érkezett.\n3. feladat")

homersekletek = [i.homerseklet for i in lista]
for i in lista:
    if i.homerseklet == min(homersekletek):
        print(
            f"A legalacsonyabb hőmérséklet: {i.telepules} {i.ido[0:2]}:{i.ido[2:4]} {i.homerseklet} fok. ")
        break

for i in lista:
    if i.homerseklet == max(homersekletek):
        print(
            f"A legmagasabb hőmérséklet: {i.telepules} {i.ido[0:2]}:{i.ido[2:4]} {i.homerseklet} fok. ")
        break

print(f"4. feladat")
for i in lista:
    if i.szelirany_szelerosseg == "00000":
        print(f"{i.telepules} {i.ido[0:2]}:{i.ido[2:4]}")

print(f"5. feladat")
varos_kodok = set(i.telepules for i in lista)
for varos_kod in varos_kodok:

    homersekletek = []
    idopontok = set()
    maxminhomerseklet = []

    for i in lista:
        if varos_kod == i.telepules and int(i.ido[0:2]) in [1, 7, 13, 19]:
            idopontok.add(i.ido[0:2])
            homersekletek.append(i.homerseklet)

        if varos_kod == i.telepules:
            maxminhomerseklet.append(i.homerseklet)

    if len(idopontok) == 4:

        print(
            f"{varos_kod} Középhőmérséklet: {sum(homersekletek) / len(homersekletek):.0f}; Hőmérséklet-ingadozás: {max(maxminhomerseklet) - min(maxminhomerseklet)} ")
    else:

        print(f"{varos_kod} NA; Hőmérséklet-ingadozás: {max(maxminhomerseklet) - min(maxminhomerseklet)} ")
print(f"6. feladat\nA fájlok elkészültek. ")

for varos_kod in varos_kodok:
    f = open(f"{varos_kod}.txt", "w", encoding="utf-8")
    f.write(f"{varos_kod}\n")
    kettoskereszt = "#"

    for i in lista:
        if i.telepules == varos_kod:
            f.write(f"{i.ido[0:2]}:{i.ido[2:4]} {kettoskereszt * int(i.szelirany_szelerosseg[3:5])}\n")
