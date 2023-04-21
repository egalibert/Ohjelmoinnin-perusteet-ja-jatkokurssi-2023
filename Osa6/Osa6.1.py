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


# Ohjelma käsittelee kahta CSV-muotoista tiedostoa. 
# Toisessa on tieto opiskelijoista:

# opnro;etunimi;sukunimi
# 12345678;pekka;peloton
# 12345687;jaana;javanainen
# 12345699;liisa;virtanen

# ja toisessa opiskelijoiden viikoittaisesta tehtävien lukumäärästä:

# opnro;v1;v2;v3;v4;v5;v6;v7
# 12345678;4;1;1;4;5;2;4
# 12345687;3;5;3;1;5;4;6
# 12345699;10;2;2;7;10;2;2

# Molempien CSV-tiedostojen ensimmäinen rivi on otsikkorivi, 
# joka kertoo kunkin kentän sisällön.

# Tee ohjelma, joka kysyy tiedostojen nimet ja tämän j
# älkeen tulostaa kunkin opiskelijan tehtävien yhteenlasketun määrän. 
# Ohjelma toimii seuraavasti, kun tiedostojen sisältö on yllä oleva:


nimet = {}

with open(input("Opiskelijatiedot:")) as tiedosto:
# with open("opiskelijat1.csv") as tiedosto:
	for rivi in tiedosto:
		osat = rivi.split(';')
		if osat[0] == "opnro":
			continue
		nimet[osat[0]] = f"{osat[1]} {osat[2]}"

kurssit = {}

with open(input("Tehtävätiedot:")) as tiedosto:
# with open("tehtavat1.csv")as tiedosto:
	for rivi in tiedosto:
		tulos = 0
		i = 1
		osat = rivi.split(';')
		if osat[0] == "opnro":
			continue
		while (i < len(osat)):
			tulos += int(osat[i])
			i += 1
		kurssit[osat[0]] = tulos

for opnro, nimi in nimet.items():
    if opnro in kurssit:
        kurssi = kurssit[opnro]
        print(nimi.rstrip("\n"), kurssi)
    else:
        print(nimi.rstrip("\n"))


# Edellinen tehtävä laajenee vielä siten, 
# että myös opiskelijan koepisteet luetaan CSV-tiedostosta.