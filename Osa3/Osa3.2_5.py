# Tee ohjelma, joka piirtää käyttäjän määräämän levyisen risuaitaviivan.

leveys = int(input("Leveys:"))
print(f"{'#' * leveys}")

# Laajenna edellistä niin, että käyttäjä 
# syöttää myös piirrettävien rivien määrän

leveys = int(input("Leveys:"))
pituus = int(input("Korkeus:"))
while (pituus > 0):
	print(f"{'#' * leveys}")
	pituus -= 1

# Tee ohjelma, joka pyytää käyttäjältä merkkijonoja ja 
# tulostaa kunkin merkkijonon oheisen esimerkin mukaisesti alleviivattuna. 
# Ohjelman suoritus päättyy, kun käyttäjä syöttää tyhjän merkkijonon, 
# eli merkkijonon jonka pituus on 0.

while (True):
	mjono = input("Anna merkkijono:")
	pituus = len(mjono)
	if (pituus > 0):
		print(f"{mjono}")
		print(f"{'-' * pituus}")
	else:
		break

# Tee ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa sen niin, 
# että tulostetuksi tulee tasan 20 merkkiä. Jos merkkijono on lyhyempi, 
# alkuun tulee tarvittava määrä tähtiä *.

sana = input("Sana:")
lenght = len(sana)
tulos = ""
tulos += (20 - lenght) * '*'
tulos += sana
print(f"{tulos}")
# print(f"{len(tulos)}")

# Tee ohjelma, joka kysyy käyttäjältä sanaa ja tulostaa sanan tähtiraameihin, 
# joissa sana on keskellä. Raamien leveys on 30 merkkiä, 
# ja voit olettaa, että sana mahtuu raameihin.

# Huom! Jos sanan pituus on pariton, voit tulostaa sanan 
# kumpaan tahansa mahdollisista keskikohdista.

sana = input("Sana:")
leveys = 30
raamit = '*' * leveys

if len(sana) % 2 == 0:
	keskikohta = leveys // 2
else:
	keskikohta = leveys // 2 + 1

tulos = f"{raamit}\n*{sana.center(leveys -2 )} * \n{raamit}"
print(tulos)

# Tee ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa sitten
# kaikki sen ensimmäisestä merkistä alkavat osajonot pituusjärjestyksessä.

jono = input("Anna merkkijono:")
pituus = len(jono)
index = 1

while (index <= pituus):
	print(f"{jono[0:index]}")
	index += 1

# Tee ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa sitten 
# kaikki sen viimeiseen merkkiin päättyvät osajonot pituusjärjestyksessä.

jono = input("Anna merkkijono:")
pituus = len(jono)
index = pituus

while (index > 0):
	print(f"{jono[0:index]}")
	index -= 1

# Tee ohjelma, joka kysyy käyttäjältä merkkijonon ja 
# tulostaa sitten tiedon löytyvätkö vokaalit a, e ja o merkkijonosta.

# Voit olettaa, että merkkijono on syötetty kokonaan pienillä kirjaimilla.
#  Katso mallia esimerkkitulostuksesta.

jono = input("Anna merkkijono:")
if ('a' in jono):
	print("a löytyy")
else:
	print("a ei löydy")
if ('e' in jono):
	print("e löytyy")
else:
	print("e ei löydy")
if ('o' in jono):
	print("o löytyy")
else:
	print("o ei löydy")