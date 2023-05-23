tajszam = input(f"Kérem a TAJ-számot: 012345672 ")
utolso = tajszam[-1]
print(f"Az ellenőrzőszámjegy: ",utolso)
osszeg = 0
for i in range(0, 8):
    if i % 2 == 0:
        osszeg += int(tajszam[i]) * 3
    else:
        osszeg += int(tajszam[i]) * 7
print(f"A szorzatok összege: {osszeg}")
if osszeg % 10 == int(utolso):
    print("Helyes a szám!")
else:
    print("Hibás a szám")
