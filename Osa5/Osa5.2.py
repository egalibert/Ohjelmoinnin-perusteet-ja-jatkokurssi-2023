# Tee funktio tuplaa_alkiot(luvut: list), 
# joka saa parametrikseen lukuja sisältävän listan.

# Funktio palauttaa uuden listan, jossa alkuperäisen 
# listan alkiot on kerrottu kahdella. 
# Funkto ei saa muuttaa alkuperäistä listaa.

def tuplaa_alkiot(lista):
	for i in lista:
		lista[i] *= 2

if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)

# Tee funktio poista_pienin(luvut: list), 
# joka saa parametrikseen lukuja sisältävän listan.

# Funktio etsii ja poistaa listasta pienimmän alkion. 
# Voit olettaa, että pienin alkio esiintyy listassa vain kerran.

# Funktio ei siis palauta mitään, 
# vaan muokkaa parametrinaan saamaansa listaa!

def poista_pienin(lista):
	pienin = 10
	for i in lista:
		if (i < pienin):
			pienin = i
	lista.remove(pienin)

if __name__ == "__main__":
    luvut = [2, 4, 6, 1, 3, 5]
    poista_pienin(luvut)
    print(luvut)


# Tässä tehtävässä toteutetaan vielä kaksi funktiota 
# sudokua varten: tulosta ja lisays.

# Funktio tulosta saa parametriksi sudokuruudukkoa esittävän kaksiulotteisen 
# listan ja tulostaa sen alla olevan esimerkkitulostuksen mukaisessa muodossa.

# Funktio lisays(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int) 
# saa parametriksi sudokuruudukkoa esittävän kaksiulotteisen listan, 
# rivi- ja sarakenumerot sekä luvun väliltä 1–9. 
# Funktio lisää luvun parametrien ilmoittamaan kohtaan sudokuruudukkoa.

def lisays(lauta, rivi, sarake, i):
	lauta[rivi][sarake] = i


def tulosta(lauta):
	for rivi_index in range(0, len(lauta)):
		teksti = ""
		if rivi_index % 3 == 0 and rivi_index != 0:
			print()
		for sarake_index in range(0, len(lauta[rivi_index])):
			arvo = lauta[rivi_index][sarake_index]
			if sarake_index % 3 == 0 and sarake_index != 0:
				teksti += " "
			teksti += (str(arvo) if arvo != 0 else '_') + " "
			
		print(teksti)


if __name__ == "__main__":
	sudoku  = [
		[9, 0, 0, 0, 8, 0, 3, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0]
	]

	tulosta(sudoku)
	lisays(sudoku, 0, 0, 2)
	lisays(sudoku, 1, 2, 7)
	lisays(sudoku, 5, 7, 3)
	print()
	print("Kolme numeroa lisätty:")
	print()
	tulosta(sudoku)



# Funktio kopioi_ja_lisaa(sudoku: list, rivi_nro: int,
# sarake_nro: int, luku:int) saa parametreikseen sudokuruudukkoa
# esittävän kaksiulotteisen listan, rivinumeron, sarakenumeron 
# sekä luvun väliltä 1–9. Funktio palauttaa parametrina saadusta 
# sudokuruudukosta kopion, johon on lisätty parametrina saatu 
# luku parametrina saatuun sijaintiin sijoitettuna. 
# Funktio ei saa muuttaa parametrina annettua sudokuruudukkoa.

def kopioi_ja_lisaa(sudoku, rivi, sarake, i):
	uusi_sudoku = [rivi[:]for rivi in sudoku]
	uusi_sudoku[rivi][sarake] = i
	return uusi_sudoku

def tulosta(lauta):
	for rivi_index in range(0, len(lauta)):
		teksti = ""
		if rivi_index % 3 == 0 and rivi_index != 0:
			print()
		for sarake_index in range(0, len(lauta[rivi_index])):
			arvo = lauta[rivi_index][sarake_index]
			if sarake_index % 3 == 0 and sarake_index != 0:
				teksti += " "
			teksti += (str(arvo) if arvo != 0 else '_') + " "
			
		print(teksti)

if __name__ == "__main__":
	sudoku  = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0]
	]

	kopio = kopioi_ja_lisaa(sudoku, 0, 0, 2)
	print("Alkuperäinen:")
	tulosta(sudoku)
	print()
	print("Kopio:")
	tulosta(kopio)



# Ristinollaa pelataan 3 x 3 -kokoisella ruudukolla, 
# johon pelaajat merkitsevät vuorotellen ristin tai nollan. 
# Pelin voittaa se pelaaja, 
# joka saa ensimmäisenä kolme merkkiä pystyyn, 
# vaakaan tai kulmittain. Peli päättyy tasapeliin, 
# jos kumpikaan pelaaja ei saa kolmen sarjaa.

# Kirjoita funktio pelaa_siirto(lauta: list, x: int, y: int, nappula:
# str), jossa sijoitetaan annettu pelinappula annettuihin 
# koordinaatteihin pelilaudalla. 
# Koordinaattien arvot ovat väliltä 0..2.

def pelaa_siirto(lauta, x, y ,nappula):
	if (x <= 2 and x >= 0 and y <= 2 and y >= 0):
		if (lauta[y][x] == ""):
			lauta[y][x] = nappula
			return (True)
		else:
			return (False)
	else:
		return (False)

if __name__ == "__main__":
	lauta = [["", "X", ""],
			 ["", "", ""], 
			 ["O", "", ""]]
	print(pelaa_siirto(lauta, 3, 0, "X"))
	print(lauta)


# Kirjoita funktio transponoi(matriisi: list), 
# joka saa parametrikseen kaksiulotteisen kokonaislukuja 
# sisältävän taulukon eli matriisin. 
# Funktio transponoi matriisin eli muuntaa rivit sarakkeiksi ja päinvastoin.

# Voit olettaa, että matriisissa on yhtä monta riviä kuin sarakettakin 
# (eli matriisi on neliömatriisi).

def transponoi(matriisi):
    for i in range(len(matriisi)):
        for j in range(i, len(matriisi)):
            matriisi[i][j], matriisi[j][i] = matriisi[j][i], matriisi[i][j]


