class Reklam:
    def __init__(self, nap, reklamtipus, mennyiseg):
        self.nap = int(nap)
        self.reklamtipus = reklamtipus
        self.mennyiseg = int(mennyiseg)

    def __repr__(self):
        return f"{self.nap} {self.mennyiseg} {self.reklamtipus}"


f = open("rendel.txt")
lista = []
for i in f:
    i = i.split()
    lista.append(Reklam(*i))
print(f"2. feladat\nA rendelések száma: {len(lista)}\n3. feladat")
nap = int(input("Kérem, adjon meg egy napot: "))
azon_a_napon = [i for i in lista if i.nap == nap]
print(f"A rendelések száma az adott napon: {len(azon_a_napon)}\n4. feladat: ")
reklamtalan = set(i.nap for i in lista if i.reklamtipus == "NR")
print(f"{30 - len(reklamtalan)} nap nem volt a reklámban nem érintett városból rendelés\n5. feladat")
for i in sorted(lista, key=lambda i: i.mennyiseg, reverse=True):
    print(f"A legnagyobb darabszám: {i.mennyiseg}, a rendelés napja: {i.nap} ")
    break


def osszes(reklamtipus, nap):
    db = 0
    for i in lista:
        if i.nap == nap and i.reklamtipus == reklamtipus:
            db += i.mennyiseg
    return db


rendezett = [i for i in lista if i.nap == 21]
szotar = {}
for i in rendezett:
    szotar[i.reklamtipus] = szotar.get(i.reklamtipus, 0) + i.mennyiseg
print("A rendelt termékek darabszáma a 21. napon", end=" ")
for index, i in szotar.items():
    print(f"{index}: {i}", end=" ")
print(f"\n8.feladat\nNapok\t1..10\t11..20\t21..30 ")
halmaz = set(i.reklamtipus for i in lista)
for y in halmaz:
    elsotiz = []
    masodiktiz = []
    harmadiktiz = []
    for i in lista:
        if i.reklamtipus == y:
            if i.nap <= 10:
                elsotiz.append(i.mennyiseg)
            elif i.nap <= 20:
                masodiktiz.append(i.mennyiseg)
            else:
                harmadiktiz.append(i.mennyiseg)
    print(f"{y}\t\t{len(elsotiz)}\t\t{len(masodiktiz)}\t\t{len(harmadiktiz)}")
