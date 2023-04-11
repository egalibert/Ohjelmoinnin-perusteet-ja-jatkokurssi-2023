# Tee funktio seitseman_veljesta jonka kutsuminen
# tulostaa seitsemän veljeksen nimet aakkosjärjestyksessä:

def seitseman_veljesta():
	print("Aapo")
	print("Eero")
	print("Juhani")
	print("Lauri")
	print("Simeoni")
	print("Timo")
	print("Tuomas")

if __name__ == "__main__":
	seitseman_veljesta()

# Täydennä koodipohjassa oleva funktio ensimmainen siten, 
# että se tulostaa parametrinaan saamansa merkkijonon ensimmäisen merkin.

# def ensimmainen(merkkijono):
#      # kirjoita koodia tähän

# # kokeillaan funktiota:
# if __name__ == "__main__":
#     ensimmainen('python')
#     ensimmainen('yhtälö')
#     ensimmainen('tieto')
#     ensimmainen('huominen')
#     ensimmainen('omena')
#     ensimmainen('nukkumaanmenoaika')

def ensimmainen(merkkijono):
	print(f"{merkkijono[0]}")

if __name__ == "__main__":
	ensimmainen('python')
	ensimmainen('yhtälö')
	ensimmainen('tieto')
	ensimmainen('huominen')
	ensimmainen('omena')
	ensimmainen('nukkumaanmenoaika')

# Tee funktio keskiarvo, joka saa parametrina kolme kokonaislukua. 
# Funktio tulostaa parametriensa keskiarvon.

def keskiarvo(x, y, i):
	tulos = (x + y + i) / 3
	print(f"{tulos}")

if __name__ == "__main__":
	keskiarvo(1, 2, 3)

# Tee funktio tulosta_monesti(merkkijono, kertaa), 
# joka saa parametriksi merkkijonon sekä kokonaisluvun, 
# joka kertoo, montako kertaa funktion tulee tulostaa 
# parametrina saamansa merkkijono:

def tulosta_monesti(jono, luku):
	while (luku > 0):
		print(f"{jono}")
		luku -= 1
if __name__ == "__main__":
	tulosta_monesti("python", 5)

# Tee funktio risunelio(pituus) joka saa parametriksi kokonaisluvun, 
# joka kertoo kuinka suuri risuneliö funktion pitää tulostaa:

def risunelio(i):
	y = i
	while (i > 0):
		print(f"{y * '#'}")
		i -= 1

if __name__ == "__main__":
	risunelio(5)

# Tee funktio shakkilauta, joka tulostaa shakkilaudan numeroista
# 0 ja 1 alla olevien esimerkkien mukaisesti.

def shakkilauta(i):
	y = i
	index = i
	tulos = ""
	tulos1 = ""
	while (index > 0):
		if (index % 2 == 1):
			tulos += "1"
		else:
			tulos += "0"
		index -= 1
	index = i
	while (index > 0):
		if (index % 2 == 1):
			tulos1 += "0"
		else:
			tulos1 += "1"
		index -= 1
	while (y > 0):
		if (y % 2 == 1):
			print(f"{tulos}")
		elif (y % 2 == 0):
			print(f"{tulos1}")
		y -= 1
			
if __name__ == "__main__":
	shakkilauta(3)

# Tee funktio nelio, joka tulostaa 
# sananeliön alla olevien esimerkkien mukaisesti.

#KESKEN

# def nelio(jono, i):
	
# if __name__ == "__main__":
# 	nelio("ab", 3)