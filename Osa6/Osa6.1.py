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
	
koepisteet = {}

# with open("koepisteet1.csv")as tiedosto:
with open(input("Koepisteet:")) as tiedosto:
	for rivi in tiedosto:
		tulos = 0
		i = 1
		osat = rivi.split(';')
		if osat[0] == "opnro":
			continue
		while (i < len(osat)):
			tulos += int(osat[i])
			i += 1
		koepisteet[osat[0]] = tulos

	# print(koepisteet)

def laske_pisteet(t_pisteet, k_pisteet):
	i = (t_pisteet / 40 * 100) // 10
	l_tulos = i + k_pisteet
	# print (l_tulos)
	if (l_tulos <= 14):
		return 0
	elif (l_tulos <= 17):
		return (1)
	elif (l_tulos <= 20):
		return (2)
	elif (l_tulos <= 23):
		return (3)
	elif (l_tulos <= 27):
		return (4)
	else:
		return (5)

for opnro, nimi in nimet.items():
	if opnro in kurssit:
		kurssi = (kurssit[opnro])
		koe_tulos = (koepisteet[opnro])
		l_tulos = laske_pisteet(kurssi, koe_tulos)
		print(nimi.rstrip("\n"), l_tulos)
	else:
		print(nimi.rstrip("\n"))



# Tee ohjelma, joka pyytää käyttäjää kirjoittamaan
# rivin englanninkielistä tekstiä. Ohjelma suorittaa tekstille 
# oikeinkirjoitustarkistuksen ja tulostaa saman tekstin siten, 
# että kaikki väärin kirjoitetut sanat on ympäröity tähdillä. 
# Seuraavassa kaksi käyttöesimerkkiä:

with open('wordlist.txt') as f:
	wordlist = f.read().split()
text = input('Write text: ')
words = text.split()
for i, word in enumerate(words):
	word = word.lower()
	if word not in wordlist:
		words[i] = '*' + word + '*'

output = ' '.join(words)

print(output)


# Tässä tehtävässä muotoillaan edellisen tehtävän tulostus parempaan muotoon
# Koepisteet osa3



# Tässä tehtävässä tehdään ohjelma, 
# joka tarjoaa käyttäjälle mahdollisuuden reseptien hakuun reseptin nimen, 
# valmistusajan tai raaka-aineen nimen perusteella. 
# Ohjelma lukee reseptit käyttäjän antamasta tiedostosta.

def muunna_listaksi(tiedosto):
	with open(tiedosto, "r") as file:
		teksti = file.read()
	rivit = teksti.split("\n")

	reseptit = []
	uusi_resepti = []
	for rivi in rivit:
		if (rivi != ""):
			uusi_resepti.append(rivi)
		if (rivi == ""):
			reseptit.append(uusi_resepti)
			uusi_resepti = []
	return(reseptit)

def hae_raakaaine(tiedosto: str, aine: str):
	reseptit = []
	reseptit = muunna_listaksi(tiedosto)
	uusi_lista = []
	valmis_lista = []

	for resepti in reseptit:
		for olio in resepti:
			if (aine.lower() in olio.lower()):
				uusi_lista.append(resepti)
	
	# print(uusi_lista)
	for resepti in uusi_lista:
		valmis_lista += ([f"{resepti[0]}, valmistusaika {resepti[1]} min"])
	return(valmis_lista)

def hae_aika(tiedosto: str, aika: int):
	reseptit = []
	reseptit = muunna_listaksi(tiedosto)
	uusi_lista  = []
	valmis_lista = []
	for resepti in reseptit:
		if (int(resepti[1]) <= aika):
			uusi_lista.append(resepti)
	for resepti in uusi_lista:
		valmis_lista += ([f"{resepti[0]}, valmistusaika {resepti[1]} min"])
	# print(uusi_lista)
	return(valmis_lista)


def hae_nimi(tiedosto: str, sana: str):
	reseptit = []
	reseptit = muunna_listaksi(tiedosto)
	valitut = []
	for resepti in reseptit:
		for olio in resepti:
			if (sana.lower() in olio.lower()):
				if (olio == resepti[0]):
					valitut.append(resepti[0])
	return(valitut)


def main():
	
		# loydetyt = hae_nimi("reseptit1.txt", "pullat")
		# loydetyt = hae_aika("reseptit1.txt", 30)
		loydetyt = hae_raakaaine("reseptit1.txt", "maito")

		for resepti in loydetyt:
			print(resepti)

if __name__ == "__main__":
	main()