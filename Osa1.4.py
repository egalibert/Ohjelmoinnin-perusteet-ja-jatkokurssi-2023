#Tee ohjelma, joka kysyy käyttäjältä lukua. 
#Ohjelma tulostaa luvun kerrottuna viidellä.

#Ohjelman tulee toimia seuraavasti:

#Esimerkkitulostus
#Anna luku: 3
#Kun kerrotaan 3 luvulla 5, saadaan 15

luku = int(input("Anna luku:"))
print(f"kun kerrotaan {luku} luvulla 5, saadaan {luku * 5}")

#Tee ohjelma, joka kysyy käyttäjältä tämän nimen ja syntymävuoden.
#Ohjelma tulostaa sitten viestin seuraavan esimerkin mukaisesti:

#Esimerkkitulostus
#Anna nimi: Keijo Keksitty
#Anna syntymävuosi: 1990
#Moi Keijo Keksitty, olet 30 vuotta vanha vuoden 2020 lopussa

nimi = input("Anna nimi:")
vuosi = int(input("Anna synytymävuosi:"))
print(f"Moi {nimi}, olet {2020 - vuosi} vuotta vanha vuoden 2020 lopussa")

#Tee ohjelma, joka kysyy käyttäjältä vuorokausien lukumäärän.
#Tämän jälkeen ohjelma tulostaa sekuntien määrän annetuissa vuorokausissa.

luku = int(input("Kuinka monen vuorokauden sekunnit tulostetaan?"))
print(f"{60 * 60 * 24 * luku}")

#Oheinen ohjelma kysyy käyttäjältä kolme lukua ja 
#Tulostaa näiden tulon (eli luvut kerrottuna toisillaan).
#Ohjelmassa on kuitenkin virhe tai virheitä, joiden takia se ei toimi.
#Korjaa ohjelma sellaiseksi, että se toimii oikein.

luku1 = int(input("Anna luku 1: "))
luku2 = int(input("Anna luku 2: "))
luku3 = int(input("Anna luku 3: "))

tulo = luku1 * luku2 * luku3

print(f"Tulo on {tulo}")

#  Tee ohjelma joka kysyy käyttäjältä kaksi lukua.
#  Ohjelma tulostaa lukujen summan ja tulon.

luku1 = int(input("Luku 1:"))
luku2 = int(input("Luku 2:"))
print(f"Lukujen summa {luku1 + luku2}")
print(f"Lukujen tulo {luku1 * luku2}")

#  Tee ohjelma, joka lukee käyttäjältä neljä lukua ja 
#  tulostaa niiden summan ja keskiarvon

num1 = int(input("Luku 1:"))
num2 = int(input("Luku 2:"))
num3 = int(input("Luku 3:"))
num4 = int(input("Luku 4:"))
summa = num1 + num2 + num3 + num4
ka = summa / 4
print(f"Lukujen summa on {summa} ja keskiarvo {ka}")