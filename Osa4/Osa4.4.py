# Tee ohjelma, joka pyytää käyttäjää syöttämään merkkijonon 
# ja tulostaa sitten merkkijonon kirjaimet yksitellen allekkain.

# Jokaisen kirjaimen jälkeen tulostetaan lisäksi tähti (*) omalle rivilleen.

sana = input("Anna merkkijono:")
for merkki in sana:
	print(merkki)
	print('*')


# Tee ohjelma, joka lukee käyttäjältä positiivisen kokonaisluvun N. 
# Ohjelma tulostaa sen jälkeen luvut väliltä -N...N nollaa lukuunottamatta. 
# Jokainen luku tulostetaan omalle rivilleen.

luku = int(input("Anna luku:"))
for i in range((luku * -1), luku + 1):
	if (i != 0):
		print(i)


# Tee funktio lista_tahtina, joka saa parametriksi listan kokonaislukuja. 
# Funktio tulostaa joukon tähtirivejä siten, että listalla olevat luvut 
# kertovat kunkin rivin tähtimäärän.

def lista_tahtina(lista):
	for i in lista:
		print(f"{i * '*'}")

if __name__ == "__main__":
	lista_tahtina([3, 7, 1, 1, 2])

# Tee funktio anagrammi joka saa parametriksi kaksi merkkijonoa. 
# Funktio palauttaa True, jos merkkijonot ovat anagrammeja eli ne 
# muodostuvat täsmälleen samoista kirjaimista.


def anagrammi(lista1, lista2):
	if (sorted(lista1) == sorted(lista2)):
		return (True)
	else:
		return (False)

if __name__ == "__main__":
	print(anagrammi("talo", 'tola'))


# Tee funktio palindromi, joka saa parametriksi merkkijonon ja palauttaa True, 
# jos merkkijono on palindromi 
# (eli samansisältöinen luettuna alusta loppuun tai lopusta alkuun).

# Tee myös funktiota hyödyntävä pääohjelma, 
# joka kyselee käyttäjältä sanoja niin kauan, 
# kunnes käyttäjä syöttää palindromin:


def palindromi(sana):
	if (sana == sana[::-1]):
		return True
	else:
		return False

while (True):
	word = input("Anna palindromi:")
	if (palindromi(word) == True):
		print(f"{word} on palindromi!")
		break
	else:
		print("ei ollut palindromi")


# Tee funktio positiivisten_summa, 
# joka saa parametriksi kokonaislukuja sisältävän listan.

# Funktio palauttaa listan positiivisten lukujen summan.

def positiivisten_summa(lista):
	pos_num = [i for i in lista if i > 0]
	summa = sum(pos_num)
	return (summa)

if __name__ == "__main__":
	lista = [1, -2, 3, -4, 5]
	vastaus = positiivisten_summa(lista)
	print("vastaus", vastaus)


# Tee funktio parilliset, 
# joka saa parametriksi kokonaislukuja sisältävän listan.

# Funktio palauttaa uuden listan, jolla on parametrina 
# olevan listan sisältämät parilliset luvut.

def parilliset(lista):
	new_lista = []
	for i in lista:
		if (i % 2 == 0):
			new_lista.append(i)
	return (new_lista)

if __name__ == "__main__":
	lista = [1, 2, 3, 4, 5]
	uusi_lista = parilliset(lista)
	print("alkuperäinen", lista)
	print("uusi", uusi_lista)


# Tee funktio summa, joka saa parametriksi kaksi 
# kokonaislukuja sisältävää listaa. Molemmissa listoissa on sama määrä alkioita.

# Funktio palauttaa uuden listan, 
# jonka alkiot muodostuvat parametreina olevien listojen alkioiden summista.

def summa(lista, lista1):
	uusi_lista = []
	index = 0
	while (index < len(lista)):
		uusi_lista.append(lista[index] + lista1[index])
		index += 1
	return uusi_lista


if __name__ == "__main__":
	a = [1, 2, 3]
	b = [7, 8, 9]
	print(summa(a, b))


# Tee funktio uniikit, joka saa parametriksi kokonaislukuja sisältävän listan.

# Funktio palauttaa uuden listan, joka sisältää parametrina annetun 
# listan luvut suuruusjärjestyksessä siten, 
# että jokainen luku on listalla vain kerran.

def uniikit(lista):
	new_lista = []
	for i in lista:
		if (i not in new_lista):
			new_lista.append(i)
	return sorted(new_lista)

if __name__ == "__main__":
	lista = [3, 2, 2, 1, 3, 3, 1]
	print(uniikit(lista))


# Tee funktio pisimman_pituus, joka saa parametriksi listan merkkijonoja. 
# Funktio palauttaa tiedon mikä on listan pisimmän merkkijonon pituus.

def pisimman_pituus(lista):
	paras = 1
	for sana in lista:
		if (len(sana) > paras):
			paras = len(sana)
	return paras

if __name__ == "__main__":
	lista = ["eka", "toka", "kolmas", "seitsemäs"]

	tulos = pisimman_pituus(lista)
	print(tulos)


# Tee funktio lyhin, joka saa parametriksi listan merkkijonoja. 
# Funktio palauttaa listan lyhimmän merkkijonon. 
# Jos samanpituisia on useita (testeissä näin ei ole), 
# voi funktio palauttaa niistä minkä vaan. 
# Funktio voi olettaa että listalla ei ole 
# tyhjiä eli nollan pituisia merkkijonoja.

def lyhin(lista):
	paras = 10
	paras_sana = ""
	for sana in lista:
		if (len(sana) < paras):
			paras = len(sana)
			paras_sana = sana
	return paras_sana

if __name__ == "__main__":
	lista = ["eka", "toka", "kolmas", "seitsemäs"]

	tulos = lyhin(lista)
	print(tulos)


# Tee funktio pisimmat, joka saa parametriksi listan merkkijonoja. 
# Funktio palauttaa listan, joka sisältää parametrina annetun 
# listan pisimmän merkkijonon. Jos pisimpiä merkkijonoja on useampia, 
# funktio palauttaa ne kaikki listassa.

# Merkkijonojen järjestyksen tuloslistassa tulee noudattaa merkkijonojen 
# järjestystä alkuperäisessä listassa.

def pisimman_pituus(lista):
	paras = 1
	for sana in lista:
		if (len(sana) > paras):
			paras = len(sana)
	return paras


if __name__ == "__main__":
	lista = ["eka", "toka", "kolmas", "seitsemäs"]

	tulos = pisimman_pituus(lista)
	print(tulos)