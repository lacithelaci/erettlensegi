class Valasztas:
    def __init__(self,ker,szavazat,vnev,knev,part):
        self.ker = int(ker)
        self.szavazat = int(szavazat)
        self.knev = knev
        self.vnev = vnev
        self.part = part

    def __repr__(self):
        return f"{self.ker} {self.szavazat} {self.vnev} {self.knev} {self.part}"
    def nev(self):
        return f"{self.vnev} {self.knev}"
lista=[]
f=open("szavazatok.txt")
for i in f:
    i=i.strip().split()
    lista.append(Valasztas(*i))
print("2. feladat")
print(f"A helyhatósági választáson {len(lista)} képviselőjelölt indult. ")
print("3. feladat")
a="Ablak"
b="Antal"
c=""
Letezik=False
for i in lista:
    if i.knev==b and i.vnev==a:
        c=i.szavazat
        Letezik=True


if Letezik:
    print(f"{c} szavazatot kapott")
else:
    print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")
db=0
for i in lista:
    db+=i.szavazat

print(f"4. feladat\nA választáson {db} állampolgár, a jogosultak {((db/12345)*100):.2f}%-a vett részt. ")
szotar={}
asd=0
print("5. feladat")
for i in lista:
    szotar[i.part]=szotar.get(i.part,0)+i.szavazat
    asd+=i.szavazat
for xd,i in szotar.items():
    if xd=="-":
        xd="Független jelöltek"
    if xd=="GYEP":
        xd="Gyümölcsevők Pártja"
    if xd=="HEP":
        xd="Húsevők Pártja"
    if xd=="TISZ":
        xd="Tejivók Szövetsége "
    if xd=="ZEP":
        xd="Zöldségevők Pártja"
    print(f"{xd}= {((i/asd)*100):.2f}%")
print("6. feladat")
lista2=[i.szavazat for i in lista]
a=max(lista2)
lista3=[]
for i in lista:
    if a==i.szavazat:
        if i.part=="-":
            i.part="független"
        lista3.append(f"{i.vnev} {i.knev} {i.part}")
for i in lista3:
    print(i)
lista4=sorted(lista,key=lambda i:(i.ker,i.szavazat))
print("7. feladat")
nev=""
part=""
kepviselok=[]
ads="-"
for i in range(1,9):
    maxe=0
    maxi=0
    for xd in lista:
        if xd.part == ads:
            xd.part="független"
        if xd.szavazat>maxe and xd.ker==i:
            maxe=xd.szavazat
            nev=xd.nev()
            part=xd.part
    kepviselok.append(f"{nev} {part}")

xd=open("kepviselok.txt","w",encoding="UTF-8")
for i in kepviselok:
    xd.write(f"{i} \n")





