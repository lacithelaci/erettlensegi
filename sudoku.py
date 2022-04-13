#Szemán László
def fuggveny(a,b):
    xd=3*((a - 1)//3)+((b - 1)//3)+1
    return xd
print("1. feladat")
file=input("Adja meg a bemeneti fájl nevét!")
sor=int(input("Adja meg egy sor számát! "))
oszlop=int(input("Adja meg egy oszlop számát! "))
f=open("konnyu.txt")
lista=[]
for i in range(9):
    xd=f.readline().strip().split()
    adatok=[int(laci) for laci in xd]
    lista.append(adatok)
lista2=[]
for i in f:
    i=[int(laci) for laci in i.strip().split()]
    lista2.append(i)
print("3. feladat")
a=None
for i in lista:
    a=lista[sor-1][oszlop-1]
    if a==0:
        a="Az adott helyet még nem töltötték ki"
print(f"Az adott helyen szereplő szám: {a} ")
print(f"A hely a(z) {fuggveny(sor,oszlop)} résztáblázathoz tartozik. ")
print("4. feladat")
szumha=0
for i in lista:
    for sor in i:
        if sor==0:
            szumha+=1
print(f"Az üres helyek aránya: {(szumha/81*100):.1f} %")
print("5. feladat")
print()
for i in lista2:
    szam = i[0]
    sor=i[1]-1
    oszlop=i[2]-1
    print("A kiválasztott sor:", i[1], "oszlop:", i[2], "a szám:", i[0])

    if lista[sor][oszlop]>0:
        print("A helyet már kitöltötték.")
        print()
    else:
        szerepel=0
        for xd in range(9):
            if lista[sor][xd] == szam:
                szerepel=1
        if szerepel==1:
            print("Az adott sorban már szerepel a szám")
            print()
        else:
            szerepel = 0
            for buvesz in range(9):
                if lista[buvesz][oszlop]==szam:
                    szerepel=1
            if szerepel==1:
                print("Az adott oszlopban már szerepel a szám.")
                print()
            else:
                szerepel=0
                for buvesz in range(3*(sor//3), 3*(sor//3)+3):
                    for xd in range(3*(oszlop//3), 3*(oszlop//3)+3):
                        if lista[buvesz][xd]==szam:
                            szerepel=1
                if szerepel==1:
                    print("A résztáblázatban már szerepel a szám.")
                    print()
                else:
                    print("A lépés megtehető.")
                    print()


