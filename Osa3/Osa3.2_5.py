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
pituus = len(sana)
keskikohta = 0
vasen_laita = "*"
oikea_laita = "*"

print(f"{30 * '*'}")
keskikohta = (30 - pituus) // 2
print(vasen_laita + (30 - keskikohta) * " " + )