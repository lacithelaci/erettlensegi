class Radio:
    def __init__(self, nap, az, uzenet):
        self.nap = int(nap)
        self.az = int(az)
        self.uzenet = uzenet

    def __repr__(self):
        return f"{self.nap} {self.az} {self.uzenet}"


lista = []
f = open("veetel.txt")
for sor in f:
    sor = sor.strip().split()
    sor2 = f.readline().strip()
    lista.append(Radio(*sor, sor2))
print(f"2. feladat:\nAz első üzenet rögzítője: {lista[0].az}\nAz utolsó üzenet rögzítője: {lista[-1].az} ")
print("3. feladat")
hossz = None
for adatok in lista:
    hossz = adatok.uzenet.split("farkas")
    if len(hossz) > 1:
        print(f"{adatok.az}. nap {adatok.nap}. rádióamatőr ")
print("4. feladat")
napok = set(nap for nap in range(1, 12))
db = 0
lista2 = []
for nap in sorted(napok):
    db = 0
    for adatok in lista:
        if adatok.nap == nap:
            db += 1
    lista2.append(db)
    print(f"{nap}. nap: {db} rádióamatőr ")
f = open(f"adaas.txt", "w")
minden_nap = set(nap.nap for nap in lista)
napi_adatok = set()
betu = None
szoveg = ""
for nap in minden_nap:
    betu = "#"
    szoveg = ""
    for adatok in lista:
        if nap == adatok.nap:
            napi_adatok.add(adatok.uzenet)
    for karakter in range(0, 90):
        betu = "#"
        for szoveg_betui in napi_adatok:
            if szoveg_betui[karakter] != "#":
                betu = szoveg_betui[karakter]
        szoveg += betu
    f.write(f"{szoveg}\n")
    napi_adatok = set()


def szame(szo):
    valasz = True
    for i in range(0, len(szo)):
        if szo[i] < '0' or szo[i] > '9':
            valasz = False
    return valasz


print("7. feladat")
nap_sorszama = int(input("Adja meg a nap sorszámát! 2 "))
radios_az = int(input("Adja meg a rádióamatőr sorszámát! 15 "))
radios_adata = ""
for adatok in lista:
    if adatok.az == radios_az and adatok.nap == nap_sorszama:
        radios_adata = adatok.uzenet
osszeg = 0
megallapithato=True
if radios_adata != "":
    for index, betu in enumerate(radios_adata):
        if szame(betu):
            osszeg+=int(betu)
        if szame(betu):
            if radios_adata[index+1]=="#":
                megallapithato=False
if radios_adata!="":
    if megallapithato != True or osszeg==0:
        print("Nincs információ")
    else:
        print(f"A megfigyelt egyedek száma: {osszeg} ")
else:
    print("Nincs ilyen feljegyzés")
