# Tee funktio lottonumerot(maara: int, alaraja: int, ylaraja: int), 
# joka arpoo annetun määrän satunnaislukuja väliltä alaraja...ylaraja, 
# tallentaa ne listaan ja palauttaa listan. 
# Lukujen tulee olla palautetussa listassa suuruusjärjestyksessä.

def lottonumerot(maara: int, alaraja: int, ylaraja: int):
	from random import randint

	rivi = []
	while len(rivi) < maara:
		uusi = randint(alaraja, ylaraja)
		if uusi not in rivi:
			rivi.append(uusi)

	return(sorted(rivi))

if __name__ == "__main__":
	for numero in lottonumerot(7, 1, 40):
		print(numero)


import random
import string

def luo_salasana(pituus):
	kirjaimet = string.ascii_lowercase
	salasana = ''.join(random.choice(kirjaimet) for i in range(pituus))
	return salasana

# Tee funktio, jonka avulla on mahdollista luoda halutun pituisia 
# satunnaisista pienistä kirjaimista (väliltä a-z) muodostettuja salasanoja.

if __name__ == "__main__":
	for i in range(10):
		print(luo_salasana(8))


# Tee paranneltu versio edellisen tehtävän funktiosta.
#  Funktio saa nyt kolme parametria:

# jos toinen parametri on True, salasanassa on myös (yksi tai useampi) numero
# jos kolmas parametri on True, salasanassa on myös 
# (yksi tai useampi) erikoismerkki joukosta !?=+-()#

from random import *
from string import *
import string

def luo_hyva_salasana(pituus :int, onko_n :bool, onko_e :bool):
	kirjaimet = string.ascii_lowercase
	ssana = ""
	ssana += choice(kirjaimet)
	if (onko_n == True):
			ssana += choice(string.digits)
	if (onko_e == True):
			ssana += choice('!?=+-()#')
	while (len(ssana) < pituus):
		merkki = choice(kirjaimet)
		ssana += merkki

	return ssana

if __name__ == "__main__":
	for i in range(10):
		print(luo_hyva_salasana(5, False, False))


# Tehdään tässä tehtävässä muutamia funktioita, 
# joita on mahdollista käyttää nopanheittoon liittyvissä peleissä.

# Normaalin nopan sijaan tehtävässä käytetään ns. epätransitiivisia noppia, 
# joista on lisää tietoa esim. tässä artikkelissa tai tässä videossa.

from random import *

def heita(noppa: str):
	a_noppa = 3, 3, 3, 3, 3, 6
	b_noppa = 2, 2, 2, 5, 5, 5
	c_noppa = 1, 4, 4, 4, 4, 4

	if (noppa == "A"):
		return(choice(a_noppa))
	elif (noppa == "B"):
		return(choice(b_noppa))
	elif (noppa == "C"):
		return(choice(c_noppa))

def pelaa(noppa1: str, noppa2: str, kertaa: int):
	noppa1_voitot = 0
	noppa2_voitot = 0
	tasapelit = 0

	for i in range(kertaa):
		noppa1_tulos = heita(noppa1)
		noppa2_tulos = heita(noppa2)
		if noppa1_tulos > noppa2_tulos:
			noppa1_voitot += 1
		elif noppa2_tulos > noppa1_tulos:
			noppa2_voitot += 1
		else:
			tasapelit += 1
	return (noppa1_voitot, noppa2_voitot, tasapelit)

if __name__ == "__main__":
	tulos = pelaa("A", "C", 1000)
	print(tulos)
	tulos = pelaa("B", "B", 1000)
	print(tulos)


