class Tesztverseny:
    def __init__(self, az, valasz):
        self.az = az
        self.valasz = valasz

    def __repr__(self):
        return f"{self.az} {self.valasz}"


print(f"1. feladat: Az adatok beolvasása")
f = open("valaszok.txt")
elso_sor = f.readline().strip()
lista = []

for i in f:
    lista.append(Tesztverseny(*i.strip().split()))
    
print(f"2. feladat: A vetélkedőn {len(lista)} versenyző indult. ")

print(f"3. feladat: A versenyző azonosítója = AB123 ")

az = input()
megegyezo_azonosito = [i.valasz for i in lista if i.az == az]

print(f"{megegyezo_azonosito[0]} (a versenyző válasza)\n4. feladat: ")


def megegyezo(helyes, bekert):
    seged_string = ""
    
    for i in range(0, len(helyes)):
        
        if helyes[i] == bekert[i]:
            seged_string += "+"
            
        else:
            seged_string += " "
            
    return seged_string


print(
    f"{elso_sor} (a helyes megoldás)\n{megegyezo(elso_sor, megegyezo_azonosito[0])} (a versenyző helyes válaszai)\n5. feladat: A feladat sorszáma = 10 ")

sorszam = int(input())
helyes = [i for i in lista if elso_sor[sorszam - 1] == i.valasz[sorszam - 1]]

print(
    f"A feladatra {len(helyes)} fő, a versenyzők {len(helyes) / len(lista) * 100:.2f}%-a adott helyes választ.\n6. feladat: A versenyzők pontszámának meghatározása ")


def pontok(helyes, bekert):
    osszeg = 0
    
    for i in range(0, len(helyes)):
        
        if helyes[i] == bekert[i]:
            if i <= 4:
                osszeg += 3
                
            elif i <= 9:
                osszeg += 4
                
            elif i <= 12:
                osszeg += 5
                
            else:
                osszeg += 6
                
    return osszeg


elso_harom = set()

for i in sorted(lista, key=lambda i: pontok(elso_sor, i.valasz), reverse=True):
    elso_harom.add(pontok(elso_sor, i.valasz))
    
    if len(elso_harom) == 3:
        break
        
print(f"7. feladat: A verseny legjobbjai: ")

for i in sorted(lista, key=lambda i: pontok(elso_sor, i.valasz), reverse=True):
    if pontok(elso_sor, i.valasz) == sorted(list(elso_harom))[2]:
        print(f"1. díj ({pontok(elso_sor, i.valasz)} pont): {i.az} ")
        
    elif pontok(elso_sor, i.valasz) == sorted(list(elso_harom))[1]:
        print(f"2. díj ({pontok(elso_sor, i.valasz)} pont): {i.az} ")
        
    elif pontok(elso_sor, i.valasz) == sorted(list(elso_harom))[0]:
        print(f"3. díj ({pontok(elso_sor, i.valasz)} pont): {i.az} ")


