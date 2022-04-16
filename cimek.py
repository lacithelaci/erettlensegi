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
