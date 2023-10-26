lista = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]
print(f"2. feladat\nA tárgyak tömegének összege: {sum(lista)} kg\n3. feladat")
osszeg = 0
print(f"A dobozok tartalmának tömege (kg):", end=" ")
lista2 = []
for i in lista:
    if osszeg + i <= 20:
        osszeg += i

    else:
        print(osszeg, end=" ")
        osszeg = 0
        osszeg += i
        lista2.append(osszeg)
if osszeg != 0:
    lista2.append(osszeg)
    print(osszeg)
print(f"A szükséges dobozok száma: ", len(lista2))
