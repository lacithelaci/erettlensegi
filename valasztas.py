class Valasztas:
    def __init__(self, kerulet, szavazat, vnev, knev, part):
        self.kerulet = int(kerulet)
        self.szavazat = int(szavazat)
        self.vnev = vnev
        self.knev = knev
        self.part = part

    def __repr__(self):
        return f"{self.kerulet} {self.szavazat} {self.knev} {self.vnev} {self.part}"

    def teljes_partnev(self):
        if self.part == "GYEP":
            return f"Gyümölcsevők Pártja"
        if self.part == "HEP":
            return f"Húsevők Pártja"
        if self.part == "TISZ":
            return f"Tejivók Szövetsége"
        if self.part == "ZEP":
            return f"Zöldségevők Pártja"
        if self.part == "-":
            return f"Független jelöltek"

    def fuggetlen(self):
        if self.part == "-":
            return f"független"
        else:
            return self.part

    def teljes_nev(self):
        return f"{self.vnev} {self.knev}"


f = open("szavazatok.txt")
lista = []
for i in f:
    i = i.strip().split()
    lista.append(Valasztas(*i))
print(f"2. feladat\nA helyhatósági választáson {len(lista)} képviselőjelölt indult.\n3. feladat")
szavazatok = None
vnev = input("Kérem a képviselő vezetéknevét")
knev = input("Kérem a képviselő keresztnevét")
for kepviselok in lista:
    if kepviselok.knev == knev and kepviselok.vnev == vnev:
        szavazatok = kepviselok.szavazat
        break
if szavazatok == None:
    print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")
else:
    print(szavazatok)
print("4. feladat")
szavazat = [i.szavazat for i in lista]
print(
    f"A választáson {sum(szavazat)} állampolgár, a jogosultak {round(sum(szavazat) / 12345 * 100, 2)}%-a vett részt.\n5. feladat")
partszavazatok = {}
for kepviselok in lista:
    partszavazatok[kepviselok.teljes_partnev()] = partszavazatok.get(kepviselok.teljes_partnev(),
                                                                     0) + kepviselok.szavazat
for part, szavazatok in partszavazatok.items():
    print(f"{part}= {((szavazatok / sum(szavazat)) * 100):.2f}% ")
print("6. feladat")
for kepviselok in lista:
    if kepviselok.szavazat == max(szavazat):
        print(f"{kepviselok.vnev} {kepviselok.knev} {kepviselok.fuggetlen()}")
f = open("kepviselok.txt", "w",encoding="utf-8")
# 7. feladat
keruletek = []
for kepviselok in lista:
    if kepviselok.kerulet not in keruletek:
        keruletek.append(kepviselok.kerulet)
maximum = 0
neve = None
part = None
for kerulet in sorted(keruletek):
    maximum = 0
    neve = None
    part = None

    for kepviselok in lista:
        if kerulet == kepviselok.kerulet:
            if kepviselok.szavazat > maximum:
                maximum = kepviselok.szavazat
                neve = kepviselok.teljes_nev()
                part = kepviselok.fuggetlen()
    f.write(f"{kerulet} {neve} {part}\n")


