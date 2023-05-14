class Jelentes:
    def __init__(self, telepules, ido, szelirany, homerseklet):
        self.telepules = telepules
        self.ido = ido
        self.szelirany = szelirany
        self.homerseklet = int(homerseklet)

    def __repr__(self):
        return f"{self.telepules} {self.ido} {self.szelirany} {self.homerseklet}"


lista = []
f = open("tavirathu13.txt")
for i in f:
    i = i.strip().split()
    lista.append(Jelentes(*i))
print(f"2. feladat ")
telepules = input(f"Adja meg egy település kódját! Település: SM ")
telepules = [i for i in lista if i.telepules == telepules]
print(f"Az utolsó mérési adat a megadott településről {telepules[-1].ido[0:2]}:{telepules[-1].ido[2:]}-kor érkezett. ")
print(f"3. feladat")
homerseklet = [i.homerseklet for i in lista]
legnagyobb = max(homerseklet)
legkisebb = min(homerseklet)
for i in lista:
    if i.homerseklet == legkisebb:
        print(
            f"A legalacsonyabb hőmérséklet: {i.telepules} {telepules[-1].ido[0:2]}:{telepules[-1].ido[2:]} {i.homerseklet} fok. ")
        break
for i in lista:
    if i.homerseklet == legnagyobb:
        print(
            f"A legmagasabb hőmérséklet: {i.telepules} {telepules[-1].ido[0:2]}:{telepules[-1].ido[2:]} {i.homerseklet} fok. ")
        break
print(f"4. feladat")
db = 0
for i in lista:
    if i.szelirany == "00000":
        db += 1
        print(f"{i.telepules} {i.ido[0:2]}:{i.ido[2:]}")
if db == 0:
    print(f"Nem volt szélcsend a mérések idején.")
print("5. feladat")
telepulesaz = set(i.telepules for i in lista)
oras_halmaz = set()
ertekek = []
for y in sorted(telepulesaz):
    oras_halmaz = set()
    ertekek = []
    for i in lista:
        if i.telepules == y:
            if int(i.ido[0:2]) in [1, 7, 13, 19]:
                oras_halmaz.add(int(i.ido[0:2]))
            ertekek.append(i.homerseklet)
    if len(oras_halmaz) == 4:
        print(
            f"{y} Középhőmérséklet: {round(sum(ertekek) / len(ertekek))}; Hőmérséklet-ingadozás: {max(ertekek) - min(ertekek)} ")
    else:
        print(f"{y} NA; Hőmérséklet-ingadozás: {max(ertekek) - min(ertekek)} ")
print(f"6. feladat\nA fájlok elkészültek. ")
kettoskereszt = "#"
for y in telepulesaz:
    f = open(f"{y}.txt", "w")
    f.write(f"{y}\n")
    for i in lista:
        if i.telepules == y:
            f.write(f"{i.ido[0:2]}:{i.ido[2:]} {kettoskereszt * int(i.szelirany[3:])}\n")
