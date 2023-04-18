# Tee funktio tee_tuple(x: int, y: int, z: int), 
# joka muodostaa ja palauttaa parametrinaan saamistaan 
# kokonaisluvuista tuplen seuraavien sääntöjen mukaaan:

# Tuplen ensimmäinen alkio on parametreista pienin
# Tuplen toinen alkio on parametreista suurin
# Tuplen kolmas alkio on parametrien summa

def tee_tuple (i, x, y):
	summa = i + x + y
	isoin = max(i, x, y)
	pienin = min(i, x, y)
	tuple = (pienin, isoin, summa)
	return (tuple)

if __name__ == "__main__":
    print(tee_tuple(5, 3, -1))


# Tee funktio vanhin(henkilot: list), 
# joka saa parametrikseen listan henkilöitä esittäviä tupleja. 
# Funktio etsii ja palauttaa vanhimman henkilön nimen.

# Henkilötuplessa on ensin henkilön nimi merkkijonona ja 
# toisena alkiona henkilön syntymävuosi.

def vanhin(henkilot):
	vanhin = 2030
	nimi = ""
	for henkilo in henkilot:
		if (henkilo[1] < vanhin):
			vanhin = henkilo[1]
			nimi = henkilo[0]
		print (henkilo[1])
	return (nimi)

if __name__ == "__main__":
	h1 = ("Arto", 1977)
	h2 = ("Einari", 1985)
	h3 = ("Maija", 1953)
	h4 = ("Essi", 1997)
	hlista = [h1, h2, h3, h4]

	print(vanhin(hlista))


# Kirjoita funktio vanhemmat(henkilot: list, vuosi: int), 
# joka palauttaa uuden listan, jolle on tallennettu kaikki 
# ennen annettua vuotta syntyneet henkilöiden nimet parametrina 
# saadulta henkilöiden listalta.

def vanhemmat(lista :list, vuosi :int):
	uusi_lista = []
	for henkilo in lista:
		if (henkilo[1] < vuosi):
			uusi_lista.append(henkilo[0])
	return (uusi_lista)

if __name__ == "__main__":
	h1 = ("Arto", 1977)
	h2 = ("Einari", 1985)
	h3 = ("Maija", 1953)
	h4 = ("Essi", 1997)
	hlista = [h1, h2, h3, h4]

	vanhemmat_henkilot = vanhemmat(hlista, 1979)
	print(vanhemmat_henkilot)


# Tässä tehtäväsarjassa toteutetaan yksinkertainen opiskelijarekisteri. 
# Ennen ohjelmoinnin aloittamista kannattanee hetki miettiä, 
# minkälaisen tietorakenteen tarvitset ohjelman 
# tallentamien tietojen organisointiin.