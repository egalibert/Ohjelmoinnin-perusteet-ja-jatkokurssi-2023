# Tee moduuli merkkiapuri, joka sisältää seuraavat funktiot:

# Funktio vaihda_koko(merkkijono: str) saa parametrikseen merkkijonon. 
# Funktio luo ja palauttaa uuden merkkijonon, jossa alkuperäisen merkkijonon 
# pienet kirjaimet on muutettu isoiksi kirjaimiksi ja päinvastoin.

# Funktio puolita(merkkijono: str) palauttaa tuplessa 
# parametrinaan saamansa merkkijonon ensimmäisen ja toisen puolikkaan. 
# Jos merkkijonossa on pariton määrä kirjaimia, ensimmäinen puolikas on lyhyempi.

# Funktio poista_erikoismerkit(merkkijono: str) palauttaa merkkijonon, 
# josta on poistettu kaikki muut merkit paitsi aakkoset 
# [a...ö, A...Ö], numerot ja välilyönnit.

def vaihda_koko(merkkijono: str):
	new_string = ""
	for letter in merkkijono:
		if (letter.isupper() == True):
			new_string += letter.lower()
		elif (letter.islower() == True):
			new_string += letter.upper()
		else:
			new_string += letter
	return (new_string)

def puolita(merkkijono: str):
	new_string1 = ""
	new_string2 = ""
	pituus = len(merkkijono)
	pituus //= 2
	i = 0
	while (i < pituus):
		new_string1 += merkkijono[i]
		i += 1
	while (i < len(merkkijono)):
		new_string2 += merkkijono[i]
		i += 1

	return (new_string1, new_string2)

def poista_erikoismerkit(merkkijono: str):
	new_string = ""
	special_characters = "!@#$%^&*()-+?_=,<>/"
	for letter in merkkijono:
		if (letter.isalpha()):
			new_string += letter
		elif (letter == " " or letter.isdigit()):
			new_string += letter
		elif (letter == special_characters):
			continue
	return(new_string)

