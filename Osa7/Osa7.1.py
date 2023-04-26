# Tee funktio hypotenuusa(kateetti1: float, kateetti2: float), 
# joka saa parametrikseen suorakulmaisen kolmion kateettien pituudet. 
# Funktio palauttaa kolmion hypotenuusan pituuden.


from math import *

def hypotenuusa(a, b):
	c = sqrt((a ** 2) + (b ** 2))
	return (c)

if __name__ == "__main__":
	print(hypotenuusa(3,4)) # 5.0
	print(hypotenuusa(5,12)) # 13.0
	print(hypotenuusa(1,1)) # 1.4142135623730951
	

# Tutustu näihin vakioihin ja kirjoita niitä käyttäen funktio 
# jaa_merkkeihin(merkkijono: str), joka saa parametrikseen merkkijonon.
# Funktio palauttaa tuplen, jossa parametrina saadun merkkijonon 
# merkit on jaettu kolmeen eri merkkijonoon:

from string import *

def jaa_merkkeihin(merkkijono: str):
	merkkijono1 = ""
	merkkijono2 = ""
	merkkijono3 = ""

	osat = ()

	for letter in merkkijono:
		if letter in ascii_letters:
			merkkijono1 += letter
		elif letter in punctuation:
			merkkijono2 += letter
		else:
			merkkijono3 += letter	
		# print(letter)
	osat = merkkijono1, merkkijono2, merkkijono3
	return(osat)

if __name__ == "__main__":
	osat = jaa_merkkeihin("Tämä on testi!!! Toimiiko, mitä?")
	print(osat[0])
	print(osat[1])
	print(osat[2])


# Tutustu Pythonin moduuliin fractions ja toteuta sen avulla funktio
# jaa_palasiksi(maara: int), joka saa parametrikseen palasten määrän. 
# Funktio jakaa luvun 1 parametrin mukaisesti yhtä suuriin murtolukupalasiin 
# ja palauttaa nämä palaset listassa.

from fractions import *

def jaa_palasiksi(maara: int):
	palat = [Fraction(1, maara) for i in range(maara)]
	return palat

if __name__ == "__main__":
	for p in jaa_palasiksi(3):
		print(p)

	print()

	print(jaa_palasiksi(5))