lista = []
f = open("ip.txt")

for i in f:
    
    i = i.strip()
    lista.append(i)
    
print(f"2. feladat:\nAz állományban {len(lista)} darab adatsor van.")

print(f"3. feladat:\nA legalacsonyabb tárolt IP-cím:", sorted(lista)[0])

print(f"4. feladat")


def ip_cim_fajtak(ipcim):
    
    if ipcim[0:9] == "2001:0db8":
        return f"Dokumentációs cím"
    
    elif ipcim[0:7] == "2001:0e":
        return f"Globális egyedi cím"
    
    else:
        return f"Helyi egyedi cím:"


szotar = {}

for i in lista:
    szotar[ip_cim_fajtak(i)] = szotar.get(ip_cim_fajtak(i), 0) + 1
    
for index, i in szotar.items():
    print(f"{index} : {i}")
    
f = open("sok.txt", "w", encoding="utf-8")
sorszam = 0

for i in lista:
    sorszam += 1
    
    if i.count("0") >= 18:
        f.write(f"{sorszam} {i}\n")
        
print(f"6. feladat\nKérek egy sorszámot: 10 ")
sorszam = int(input())

def rovidetes_1(sor):
    teljes = ""
    uj_alak = sor.replace("0000", "0")
    uj_alak = uj_alak.split(":")
    
    for i in uj_alak:
        
        if len(i) != 1:
            
            while i[0] == '0':
                i = i.replace('0', "", 1)
                
        teljes += i
        teljes += ":"
        
    return teljes[0:-1]


print(f"{lista[sorszam - 1]}\n{rovidetes_1(lista[sorszam - 1])}\n7. feladat")


def rovidetes_2(sor):
    uj_alak = sor.split(":")
    maximum = 0
    szamlalo = 0
    ujabb_alak=""
    
    for i in uj_alak:
        
        if i[0] == '0':
            szamlalo+=1
            
        else:
            szamlalo=0

        if maximum<szamlalo:
            maximum=szamlalo
            
        ujabb_alak+=i
        ujabb_alak+=":"
        
    ujabb_alak=ujabb_alak[0:-1]
    
    if maximum>1:
        return ujabb_alak.replace(":0"*maximum,":",1)
    
    else:
        return ujabb_alak
    
if rovidetes_1(lista[sorszam - 1])!=rovidetes_2(rovidetes_1(lista[sorszam - 1])):
    print(rovidetes_2(rovidetes_1(lista[sorszam - 1])))
    
else:
    print("Nem rövidíthető tovább.")
