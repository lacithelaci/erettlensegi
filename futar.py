class Futar:
    def __init__(self, napszam, fuvarszam, km):
        self.napszam = int(napszam)
        self.fuvarszam = int(fuvarszam)
        self.km = int(km)

    def __repr__(self):
        return f"{self.napszam} {self.fuvarszam} {self.km}"


lista = []
f = open("tavok.txt")
for i in f:
    i = i.strip().split()
    lista.append(Futar(*i))
print("2. feladat")
for i in sorted(lista, key=lambda i: (i.napszam, i.fuvarszam)):
    print(f"A hét legelső útja kilométerben", i.km)
    break
km = 0
for i in sorted(lista, key=lambda i: (i.napszam, i.fuvarszam)):
    km = i.km
print(f"3. feladat\na hét utolsó útja kilométerben", km)
minden_nap = set(i for i in range(1, 8))
dolgozott = set(i.napszam for i in lista)

print(f"4. feladat\nA futár ezeken a napokon nem dolgozott:", end=" ")
print(*minden_nap.difference(dolgozott))
print(f"5. feladat")
szotar = {}
for i in lista:
    szotar[i.napszam] = szotar.get(i.napszam, 0) + 1
legtobb = max(szotar.values())
for index, i in szotar.items():
    if i == legtobb:
        print(f"a hét {index}. napján volt a legtöbb fuvar")
print("6. feladat")
szum = 0
for y in minden_nap:
    for i in lista:
        if i.napszam == y:
            szum += i.km
    print(f"{y}. nap {szum} km")
    szum = 0
def penz(km):
    if km<=2:
        return 500
    elif km<=5:
        return 700
    elif km<=10:
        return 900
    elif km<=20:
        return 1400
    else:
        return 2000
print("7. feladat\nkérek egy km-t")
print(f"{penz(int(input()))} Ft")
f=open("dijazas.txt","w",encoding="utf-8")
osszeg=0
for i in sorted(lista, key=lambda i: (i.napszam, i.fuvarszam)):
    f.write(f"{i.napszam}. nap {i.fuvarszam}. út: {penz(i.km)} Ft\n")
    osszeg+=penz(i.km)
print(f"9. feladat\na futár {osszeg} forintot kap a heti munkájáért! ")
