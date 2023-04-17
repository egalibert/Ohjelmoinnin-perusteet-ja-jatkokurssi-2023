# Tee funktio pisin(merkkijonot: list), joka saa 
# parametrikseen listan merkkijonoja. 
# Funktio etsii ja palauttaa listalta pisimmän merkkijonon. 
# Voit olettaa, että vain yksi jonoista on pisin.

def pisin(lista):
	paras = 1
	sana = ""
	for i in lista:
		if (len(i) > paras):
			paras = len(i)
			sana = i
	return (sana)

if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))


# Tee funktio laske_alkiot(matriisi: list, alkio: int), 
# joka saa parametrikseen kaksiulotteisen kokonaislukutaulukon. 
# Funktio laskee, kuinka monta annetun alkion mukaista arvoa taulukosta löytyy.

def laske_alkiot(lista, index):
	count = 0
	for rivi in lista:
		for alkio in rivi:
			if (alkio == index):
				count += 1
	return (count)

if __name__ == "__main__":
	m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
	print(laske_alkiot(m, 1))


# Kirjoita funktio kumpi_voitti(pelilauta: list), 
# joka saa parametrikseen kaksiulotteisen taulukon, 
# joka kuvaa pelilautaa. 
# Taulukko koostuu kokonaisluvuista seuraavasti:


def kumpi_voitti(lauta):
	p1 = 0
	p2 = 0
	for rivi in lauta:
		for alkio in rivi:
			if (alkio == 1):
				p1 += 1
			elif (alkio == 2):
				p2 += 1
			else:
				continue
	if (p1 > p2):
		return (1)
	elif (p2 > p1):
		return (2)
	else:
		return (0)

if __name__ == "__main__":
	m = [[1, 2, 1], [0, 1, 2], [1, 0, 0]]
	print((kumpi_voitti(m)))


# Tee funktio rivi_oikein(sudoku: list, rivi_nro: int), 
# joka saa parametriksi sudokuruudukkoa esittävän kaksiulotteisen taulukon
# ja rivin numeron kertovan kokonaisluvun (rivit on numeroitu nollasta alkaen).
# Metodi palauttaa tiedon, onko rivi oikein täytetty eli onko siinä kukin 
# luvuista 1–9 korkeintaan kerran.

def rivi_oikein(lista, rivi):
	index = 1
	count = 0
	while (index < 10):
		count = 0
		for alkio in lista[rivi]:
			if (alkio == index):
				count += 1
			if (count > 1):
				return (False)
		index += 1
	return (True)
		

if __name__ == "__main__":
	sudoku = [
	[9, 0, 0, 0, 8, 0, 3, 0, 0],
	[2, 0, 0, 2, 5, 0, 7, 0, 0],
	[0, 2, 0, 3, 0, 0, 0, 0, 4],
	[2, 9, 4, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 7, 3, 0, 5, 6, 0],
	[7, 0, 5, 0, 6, 0, 4, 0, 0],
	[0, 0, 7, 8, 0, 3, 9, 0, 0],
	[0, 0, 1, 0, 0, 0, 0, 0, 3],
	[3, 0, 0, 0, 0, 0, 0, 0, 2]
	]

	print(rivi_oikein(sudoku, 0))
	print(rivi_oikein(sudoku, 1))


# Tee funktio sarake_oikein(sudoku: list, sarake_nro: int), 
# joka saa parametriksi sudokuruudukkoa esittävän kaksiulotteisen taulukon 
# ja sarakkeen (eli pystyrivin) numeron kertovan kokonaisluvun. 
# Metodi palauttaa tiedon, onko sarake oikein täytetty eli onko 
# siinä kukin luvuista 1–9 korkeintaan kerran.

def sarake_oikein(lista, sarake):
	index = 1
	count = 0
	while (index < 10):
		count = 0
		for rivi in lista:
				if (rivi[sarake] == index):
					count += 1
				if (count > 1):
					return (False)
		index += 1
	return (True)

if __name__ == "__main__":
	sudoku = [
	[9, 0, 0, 0, 8, 0, 3, 0, 0],
	[2, 0, 0, 2, 5, 0, 7, 0, 0],
	[0, 2, 0, 3, 0, 0, 0, 0, 4],
	[2, 9, 4, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 7, 3, 0, 5, 6, 0],
	[7, 0, 5, 0, 6, 0, 4, 0, 0],
	[0, 0, 7, 8, 0, 3, 9, 0, 0],
	[0, 0, 1, 0, 0, 0, 0, 0, 3],
	[3, 0, 0, 0, 0, 0, 0, 0, 2]
	]

	print(sarake_oikein(sudoku, 0))
	print(sarake_oikein(sudoku, 1))


# Tee funktio nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int), 
# joka saa parametriksi sudokuruudukkoa esittävän kaksiulotteisen 
# taulukon sekä yhden ruudun paikan kertovat rivi- ja sarakenumerot.

def nelio_oikein(lauta, x, y):
	index = 1
	max_x = x + 2
	max_y = y + 2
	temp_x = x
	temp_y = y
	while (index < 10):
		count = 0
		temp_x = x
		while (temp_x <= max_x):
			temp_y = y
			while(temp_y <= max_y):
				if (lauta[temp_x][temp_y] == index):
					count += 1
				if (count > 1):
					return (False)
				temp_y += 1
			temp_x += 1
		index += 1
	return (True)



if __name__ == "__main__":
	sudoku = [
	[9, 0, 0, 0, 8, 0, 3, 0, 0],
	[2, 0, 0, 2, 5, 0, 7, 0, 0],
	[0, 2, 0, 3, 0, 0, 0, 0, 4],
	[2, 9, 4, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 7, 3, 0, 5, 6, 0],
	[7, 0, 5, 0, 6, 0, 4, 0, 0],
	[0, 0, 7, 8, 0, 3, 9, 0, 0],
	[0, 0, 1, 0, 0, 0, 0, 0, 3],
	[3, 0, 0, 0, 0, 0, 0, 0, 2]
	]

	print(nelio_oikein(sudoku, 0, 0))
	print(nelio_oikein(sudoku, 1, 2))


# Tee funktio sudoku_oikein(sudoku: list), joka saa parametriksi 
# sudokuruudukkoa esittävän kaksiulotteisen taulukon. 
# Funktio kertoo käyttäen edellisen kolmen tehtävän funktioita 
# (kopioi ne tämän tehtävän koodin joukkoon), onko parametrina saatu 
# ruudukko täytetty oikein, eli sen jokainen rivi, 
# jokainen sarake sekä kaikki erilliset 3x3-neliöt sisältävät 
# korkeintaan kertaalleen jokaisen luvuista 1–9.

def nelio_oikein(lauta, x, y):
	index = 1
	max_x = x + 2
	max_y = y + 2
	temp_x = x
	temp_y = y
	while (index < 10):
		count = 0
		temp_x = x
		while (temp_x <= max_x):
			temp_y = y
			while(temp_y <= max_y):
				if (lauta[temp_x][temp_y] == index):
					count += 1
				if (count > 1):
					return (False)
				temp_y += 1
			temp_x += 1
		index += 1
	return (True)

def sarake_oikein(lista, sarake):
	index = 1
	count = 0
	while (index < 10):
		count = 0
		for rivi in lista:
				if (rivi[sarake - 1] == index):
					count += 1
				if (count > 1):
					return (False)
		index += 1
	return (True)

def rivi_oikein(lista, rivi):
	index = 1
	count = 0
	while (index < 10):
		count = 0
		for alkio in lista[rivi - 1]:
			if (alkio == index):
				count += 1
			if (count > 1):
				return (False)
		index += 1
	return (True)

def sudoku_oikein(sudoku):
	count = 0
	total_count = 0
	index1 = 0
	index2 = 0
	while (index1 <= 9):
		if (rivi_oikein(sudoku, index1) == True):
			count += 1
		else:
			return (False)
		index1 += 1
	if (count == 10):
		total_count += 1
	print(total_count, count)
	count = 0
	while (index2 <= 9):
		if (sarake_oikein(sudoku, index2) == True):
			count += 1
		else:
			return (False)
		index2 += 1
	if (count == 10):
		total_count += 1
	index1 = 0
	index2 = 0
	count = 0
	while (index1 <= 6):
		index2 = 0
		while (index2 <= 6):
			if (nelio_oikein(sudoku, index1, index2) == True):
				count += 1
			else:
				return (False)
			index2 += 3
		index1 += 3
	if (count == 9):
		total_count += 1
	print(total_count)
	if (total_count == 3):
		return (True)
	else:
		return (False)
		
	# (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) ja (6, 6)


if __name__ == "__main__":
	sudoku1 = [
	[9, 0, 0, 0, 8, 0, 3, 0, 0],
	[2, 0, 0, 2, 5, 0, 7, 0, 0],
	[0, 2, 0, 3, 0, 0, 0, 0, 4],
	[2, 9, 4, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 7, 3, 0, 5, 6, 0],
	[7, 0, 5, 0, 6, 0, 4, 0, 0],
	[0, 0, 7, 8, 0, 3, 9, 0, 0],
	[0, 0, 1, 0, 0, 0, 0, 0, 3],
	[3, 0, 0, 0, 0, 0, 0, 0, 2]
	]

	print(sudoku_oikein(sudoku1))

	sudoku2 = [
	[2, 6, 7, 8, 3, 9, 5, 0, 4],
	[9, 0, 3, 5, 1, 0, 6, 0, 0],
	[0, 5, 1, 6, 0, 0, 8, 3, 9],
	[5, 1, 9, 0, 4, 6, 3, 2, 8],
	[8, 0, 2, 1, 0, 5, 7, 0, 6],
	[6, 7, 4, 3, 2, 0, 0, 0, 5],
	[0, 0, 0, 4, 5, 7, 2, 6, 3],
	[3, 2, 0, 0, 8, 0, 0, 5, 7],
	[7, 4, 5, 0, 0, 3, 9, 0, 1]
	]

	print(sudoku_oikein(sudoku2))

