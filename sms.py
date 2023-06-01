def szamokkal(szoveg):
    hozzafuzni = ""
    betuk = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    
    for betu in szoveg:
        db = 1
        
        for i in betuk:
            db += 1
            
            if betu in i:
                
                hozzafuzni += str(db)
    return hozzafuzni


print(f"1. feladat\nAdjon meg egy betűt: ")
betu = input()

print(f"Ez tartozik hozzá: {szamokkal(betu)}\n2. feladat\nkérek egy szót")

szo = input()
print(f"Ezzel a számsorral lehet ezt a telefonba bevinni:", szamokkal(szo))

lista = []
f = open("szavak.txt")

for i in f:
    i = i.strip()
    lista.append(i)

print(f"4. feladat\nA leghosszabb szó:", sorted(lista, key=lambda i: len(i))[-1])

print(f"5. feladat")
rovidek = [i for i in lista if len(i) <= 5]

print(f"{len(rovidek)} rövid szó található a fájlban!")
f = open("kodok.txt", "w", encoding="utf-8")

for i in lista:
    f.write(f"{szamokkal(i)}\n")
    
print(f"7. feladat\nAdjon meg egy számsort")
szamsor = input()
szamsoros = [i for i in lista if szamokkal(i) == szamsor]

print(f"Ezek tartoznak hozzá:", *szamsoros)
print(f"8. feladat")

szotar = {}

for i in lista:
    szotar[szamokkal(i)] = szotar.get(szamokkal(i), 0) + 1
    
db2 = 0

for index, db in szotar.items():
    for y in lista:
        
        if db > 1 and szamokkal(y) == index:
            db2 += 1
            print(f"{y} : {index}", end="; ")
            
        if db2 == 8:
            print("")
            db2 = 0
            
print("\n9. feladat")
van = False
kod = None
maximum = max(szotar.values())

for index, i in szotar.items():
    
    for y in lista:
        
        if index == szamokkal(y) and maximum == i:
            kod = szamokkal(y)
            break
            
idetartozo = [i for i in lista if szamokkal(i) == kod]
print(f"{kod}:", *idetartozo)
