# Luo funktio pisteet(tilasto), joka saa parametrikseen merkkijonon.

# Parametrina annettu merkkijono on jääkiekkojoukkueen tilasto, joka on muodoltaa:
# [joukkue]:[voitot]-[tappiot]-[tasapelit]

# Esimerkiksi merkkijono: "Kumpulan Älynväläys:0-8-1" kuvaa joukkuetta nimeltään 
# Kumpulan Älynväläys, jolla on 0 voittoa, 8 tappioita ja 1 tasapeli.

# Funktio pisteet(tilasto) palauttaa joukkueen saamat pisteet kokonaislukuna. 
# Pisteet lasketaan niin että voitosta saa kolme pistettä, 
# tasapelistä yhden pisteen ja tappiosta ei yhtään.

# Tee tehtävän 3 ratkaisu tänne

def pisteet(tilasto :str):
	palautus = 0

	pisteet = tilasto.split(':')
	tulokset = pisteet[1].split('-')

	print(tulokset)
	if (tulokset[0].isdigit() == False or tulokset[1].isdigit() == False or tulokset[2].isdigit() == False):
		raise ValueError("Kaikki syötteet eivät olleet kokonaislukuja")
	else:
		palautus += int(tulokset[0]) * 3
		palautus += int(tulokset[1])

	return (palautus)

# def main():
# 	tilasto = "Heban haukat:5-6-1"
# 	tulos = (pisteet(tilasto))
# 	print(tulos)
# 	tilasto ="Brewsterit:3-12-10"
# 	tulos = (pisteet(tilasto))
# 	print(tulos)
# 	tilasto = "Virkavapailijat:0-0-0"
# 	tulos = (pisteet(tilasto))
# 	print(tulos)
# 	tilasto = "KBC:AAA-1-ll"
# 	tulos = (pisteet(tilasto))
# 	print(tulos)
# 	tilasto = "Navy jerries:7-xx-1"
# 	tulos = (pisteet(tilasto))
# 	print(tulos)
	# tilasto = "Loosisters:8-5-abb"
	# tulos = (pisteet(tilasto))
	# print(tulos)


# main()