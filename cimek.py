lista=[]
o=open("ip.txt")
for i in o:
    i=i.strip()
    lista.append(i)
print(f"2. feladat:\nAz állományban {len(lista)} darab adatsor van. ")
print("3. feladat")
lista2=sorted(lista,key=lambda i:i)
utso=""
for i in lista2:
        utso=i
        break
print(f"A legalacsonyabb tárolt IP-cím:")
print(utso)
print("4. feladat")
def fuggveny(a):
    megoldas="Helyi egyedi cím"
    if a[0:9]=="2001:0db8":
        megoldas = "Dokumentációs cím"
    if a[0:7]=="2001:0e":
        megoldas="Globális egyedi cím"
    return megoldas
szotar={}
for i in lista:
    szotar[fuggveny(i)]=szotar.get(fuggveny(i),0)+1
for i,xd in szotar.items():
    print(f"{i}:{xd}")
def nullak(a):
    db=0
    for i in a:
        if i=="0":
            db+=1
    return db
f=open("sok.txt","w")
for index,i in enumerate(lista):
    if nullak(i)>=18:
        f.write(f"{index+1} {i} \n")
print("6. feladat")
def nullak_nelkul(a):
    a=a.strip().split(":")
    ures=""
    for i in a:
        if i=="0000":
            ures+="0"
            ures+=":"
        else:
            ures+=i
            ures+=":"
    return ures
def eltuntetheto(a):
    a = a.strip().split(":")
    ures=""
    semmi=""
    for i in a:
        if len(i)>1:
            if i[0].__contains__("0") or i[0:1].__contains__("00") or i[0:2].__contains__("000"):
                semmi=i.replace("0","")
            else:
                semmi=i
        else:
            semmi=i
        ures+=semmi
        ures+=":"

    return ures[0:-1]
a=eltuntetheto(nullak_nelkul("fcef:b0e7:7d20:0000:0000:0000:3b95:0565"))
print(a)
print('7. feladat')
