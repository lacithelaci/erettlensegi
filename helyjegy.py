class Helyjegy:
    def __init__(self, sorszam, ules, honnan, hova):
        self.sorszam = int(sorszam)
        self.ules = int(ules)
        self.honnan = int(honnan)
        self.hova = int(hova)

    def __repr__(self):
        return f"{self.sorszam} {self.ules} {self.honnan} {self.hova}"


f = open("eladott.txt")
elso_sor = f.readline().split()
lista = []
db = 0

for i in f:

    db += 1
    lista.append(Helyjegy(db, *i.strip().split()))
print(
    f"2. feladat\nA legutolsó jegyvásárló ülésének sorszáma: {lista[-1].ules}\nAz általa beutazott távolság: {lista[-1].hova - lista[-1].honnan} km")
print(f"3. feladat\nŐk utazták végig a teljes utat:", end=" ")

for i in lista:

    if i.honnan == 0 and i.hova == int(elso_sor[1]):
        print(i.sorszam, end=" ")

print(f"\n4. feladat")


def fizetendo(ut_hossza, km_dij):

    if str(ut_hossza)[-1] != "0":
        ut_hossza = int(ut_hossza // 10) * 10 + 10

    ar = ut_hossza * km_dij
    if str(ar)[-1] != "0":

        if str(ar)[-1] in ["1", "2"]:
            ar = int(ar // 10) * 10

        elif str(ar)[-1] in ["3", "4", "5", "6", "7"]:
            ar = int(ar // 10) * 10 + 5

        else:
            ar = int(ar // 10) * 10 + 10

    return ar


arak = [fizetendo(i.hova - i.honnan, int(elso_sor[2])) for i in lista]
print(f"a jegyekből {sum(arak)} bevétele származott a társaságnak!\n5. feladat")

vegallomast_megelozo = [i.hova for i in lista if i.hova != int(elso_sor[1])]
fel = 0
le = 0

for i in lista:

    if i.honnan == max(vegallomast_megelozo):
        fel += 1

    elif i.hova == max(vegallomast_megelozo):
        le += 1

print(f"A busz végállomást megelőző utolsó megállásánál {fel} szállt fel és {le} le! ")
print("6. feladat")

halmaz = set()
for i in lista:
    halmaz.add(i.hova)
    halmaz.add(i.honnan)

print(f"{len(halmaz) - 2} helyen állt meg a busz a kiinduló állomás és a célállomás között! ")
tavolsag = int(input("7. feladat\nAdjon meg egy távolságot"))

f = open("kihol.txt", "w", encoding="utf-8")
ulesek = set(i.ules for i in lista)

for ules in ulesek:

    szabad_e = False
    utas = None

    for i in lista:

        if i.honnan <= tavolsag < i.hova and i.ules==ules:
            szabad_e = True
            utas = i.sorszam
    if szabad_e:

        f.write(f"{ules}. ülés: {utas}. utas\n")

    else:
        f.write(f"{ules}. ülés: üres\n")
