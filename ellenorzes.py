class Ellenorzes:
    def __init__(self, rendszam, kora, kperc, kms, kezred, vora, vperc, vms, vezred):
        self.rendszam = rendszam
        self.kora = int(kora)
        self.kperc = int(kperc)
        self.kms = int(kms)
        self.kezred = int(kezred)
        self.vora = int(vora)
        self.vperc = int(vperc)
        self.vms = int(vms)
        self.vezred = int(vezred)

    def __repr__(self):
        
        return f"{self.rendszam} {self.kora} {self.kperc} {self.kms} {self.kezred} {self.vora} {self.vperc} {self.vms} {self.vezred}"

    def atlagkm(self):
        
        
        return int(10 / (((self.vora * 3600 + self.vperc * 60 + self.vms + self.vezred / 1000) - (
                self.kora * 3600 + self.kperc * 60 + self.kms + self.kezred / 1000)) / 3600))

    def vegms(self):
        
        return self.vora * 3600 + self.vperc * 60 + self.vms + self.vezred / 1000

    def kezdms(self):
        
        return self.kora * 3600 + self.kperc * 60 + self.kms + self.kezred / 1000

    def bunti(self):
        
        if self.atlagkm() <= 121:
            return f"30000 Ft"
        
        elif self.atlagkm() <= 136:
            return f"45000 Ft"
        
        elif self.atlagkm() <= 151:
            return f"60000 Ft"
        
        else:
            return f"200000 Ft"


f = open("meresek.txt")
lista = []
for i in f:
    
    lista.append(Ellenorzes(*i.strip().split()))
    
print(f"2. feladat\nA mérés során {len(lista)} jármű adatait rögzítették.\n3. feladat")

kilenc_elott = [i for i in lista if i.vora < 9]
print(f"9 óra előtt {len(kilenc_elott)} jármű haladt el a végponti mérőnél.\n4. feladat\nAdjon meg egy óra és perc értéket! 8 20 ")

ora = int(input())
perc = int(input())

megadott_idopont = [i for i in lista if i.kperc == perc and i.kora == ora]
print(f"a. A kezdeti méréspontnál elhaladt járművek száma:", len(megadott_idopont))

megadott_idopont2 = [i for i in lista if i.kperc <= perc <= i.vperc and i.kora <= ora <= i.vora]
print(f"b. A forgalomsűrűség: {len(megadott_idopont2) / 10}")

print(f"5. feladat")

adatai = None
km_orak = [i.atlagkm() for i in lista]

for i in lista:
    
    if i.atlagkm() == max(km_orak):
        adatai = i
        print(f"rendszáma: {i.rendszam}\nátlagsebessége: {i.atlagkm()} km/h ")
        break
        
lehagyottak = [i for i in lista if i.kezdms() < adatai.kezdms() and adatai.vegms() < i.vegms()]
print(f"által lehagyott járművek száma: {len(lehagyottak)}\n6. feladat")

kilencven_felett = [i for i in lista if i.atlagkm() >= 90]
print(f"A járművek {len(kilencven_felett) / len(lista) * 100:.2f}%-a volt gyorshajtó. ")

f=open("buntetes.txt","w")
megbuntetett=[i for i in lista if i.atlagkm()>104]

for i in megbuntetett:
    f.write(f"{i.rendszam};{i.atlagkm()} km/h;{i.bunti()}\n")
