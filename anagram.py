print("1. feladat")
szoveg=input("Kérek egy szöveget)
betui=set()
for betu in szoveg:
    betui.add(betu)
print("Karakterszám:",len(betui))
print("Karakterek:",*betui)
lista=[]
f=open("szotar.txt")
for szo in f:
    szo=szo.strip()
    lista.append(szo)
def sorba(szo):
    szoveg=""
    for betu in sorted(szo):
        szoveg+=betu
    return szoveg
f=open("abc.txt","w")
for szo in lista:
    f.write(f"{sorba(szo)}\n")
print("4. feladat")
szo1=input("Kérek egy szöveget)
szo2=input("Kérek egy másik szöveget)
if sorba(szo1)==sorba(szo2):
    print("Anagramma")
else:
    print("Nem anagramma")
print("5. feladat")
anagrammak=[]
szo1=input("Kérek egy szöveget)
for szo in lista:
    if sorba(szo)==sorba(szo1):
        anagrammak.append(szo)
if len(anagrammak)==0:
    print("Nincs a szótárban anagramma")
else:
    print(*anagrammak)
print("6. feladat")
maxhossz=0
for szo in lista:
    if maxhossz<len(szo):
        maxhossz=len(szo)
leghosszabbak=[szo for szo in lista if len(szo)==maxhossz]
for szo in sorted(leghosszabbak,key=lambda szo:sorba(szo)):
    print(szo)
f=open("rendezve.txt","w")
elozo=""
jelenlegi=""
db=0
lista=sorted(lista,key=lambda szo:(len(szo),sorba(szo)))
for szo in sorted(lista,key=lambda szo:(len(szo),sorba(szo))):
    jelenlegi=szo
    if db!=0:
        if sorba(jelenlegi)==sorba(elozo):
            f.write(f"{elozo} ")
        else:
            f.write(f"{elozo}\n")
        if len(jelenlegi)!=len(elozo):
            f.write("\n")
    db+=1
    elozo=jelenlegi
if sorted(lista[-1])==sorted(lista[-2]):
    f.write(f"{lista[-1]}")
else:
    f.write(f"\n{lista[-1]}")
