# Kirjoita funktio suurin, joka lukee tiedoston 
# ja palauttaa suurimman tiedostosta löytyvän luvun.

def suurin():
	with open("luvut.txt") as tiedosto:
		alku = True
		for luku in tiedosto:
			if alku or int(luku) > suurin:
				suurin = int(luku)
				alku = False
		return suurin

if __name__ == "__main__":
	suurin()


# Kirjoita funktio lue_hedelmat, joka lukee hedelmätiedoston 
# ja muodostaa siitä sanakirjan, jossa hedelmän nimi on avain ja hinta arvo.
# Hinnan tulee olla float-arvona sanakirjassa.

def lue_hedelmat():
	with open("hedelmat.csv") as tiedosto:
		sanakirja = {}
		for rivi in tiedosto:
			rivi = rivi.replace("\n", "")
			osat = rivi.split(";")
			sanakirja[osat[0]] = float(osat[1])
	return (sanakirja)

def main():
	lue_hedelmat()

if __name__ == "__main__":
	main()


# Kirjoita funktiot summa ja maksimi, jotka lukevat ja palauttavat
# nimensä mukaisesti matriisin kaikkien alkioiden summan ja suurimman alkion.

# Kirjoita lisäksi funktio rivisummat, 
# joka palauttaa listassa kaikkien matriisin rivien summat. 
# Esimerkiksi matriisille

def rivisummat():
	numerot = avaa_file()
	rivi_sum = 0
	uusi_lista = []
	for i in numerot:
		index = 0
		while (index < len(i)):
			rivi_sum += int(i[index])
			index += 1
		uusi_lista.append(rivi_sum)
		rivi_sum = 0
	return (uusi_lista)


def maksimi():
	numerot = avaa_file()
	maksimi = 1
	for i in numerot:
		for numero in i:
			if (int(numero) > maksimi):
				maksimi = int(numero)
	return (maksimi)

def summa():
	numerot = avaa_file()
	tulos = 0
	for i in numerot:
		for numero in i:
			tulos += int(numero)
	return (tulos)

def avaa_file():
	numerot = []
	with open("matriisi.txt") as tiedosto:
		for rivi in tiedosto:
			rivi = rivi.replace("\n", "")
			for numero in rivi:
				numero = rivi.split(",")
			numerot.append(numero)
	return (numerot)

def main():

	s_tulos = summa()
	m_tulos = maksimi()
	r_tulos = []
	r_tulos = rivisummat()
	print(f"{s_tulos}\n{m_tulos}\n{r_tulos}")


if __name__ == "__main__":
	main()


