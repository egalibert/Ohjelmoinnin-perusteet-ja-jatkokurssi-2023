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