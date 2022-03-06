f=open("penztar.txt")
lista=[]
kosar={}
for i in f:
    if i.strip()=="F":
        lista.append(kosar)
        kosar={}
    else:
        if i.strip() not in kosar:
            kosar[i.strip()]=1
        else:
            kosar[i.strip()]+=1
print(f"2. feladat\nA fizetések száma: {len(lista)} ")
print(f"3. feladat\nAz első vásárló {len(lista[0])} darab árucikket vásárolt.")
print("4. feladat")
sorszam=int(input("Adja meg egy vásárlás sorszámát!"))
termek=input("Adja meg egy árucikk nevét!")
dbszam=int(input("Adja meg a vásárolt darabszámot!"))
print("5. feladat")
eloszor=0
utolso=0
db=0
volte=True
for index,i in enumerate(lista):
    for xd in i:
        if termek==xd:
            db+=1
            eloszor=index
        if volte:
            if termek == xd:
                utolso=index
                volte=False
print(f"Az első vásárlás sorszáma: {utolso+1}")
print(f"Az utolsó vásárlás sorszáma: {eloszor+1} ")
print(f"{db} vásárlás során vettek belőle. ")
print("6. feladat")
def darab(a):
    alap=500
    alap2=500
    alap3=500
    if a==2:
        alap2=450
    elif a>2:
        alap3=400
        alap2=450
    else:
        alap=500
    if a==1:
        return alap
    if a==2:
        return alap+alap2
    if a>=3:
        return alap+alap2+(alap3*(a-2))
print(f"{dbszam} darab vételekor fizetendő: {darab(dbszam)} ")
print("7. feladat")
for index,i in enumerate(lista):
    for xd,xd2 in i.items():
        if index+1==sorszam:
            print(f"{xd} {xd2}")
i2=0
szamlalo=0
asd=open("összeg.txt","w")
for index,i in enumerate(lista):
    if i2==index:
        for xd,xd2 in i.items():
            szamlalo+=darab(xd2)
        asd.write(f"{i2+1}: {szamlalo} \n")
        i2+=1
    szamlalo=0