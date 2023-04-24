# Tee ohjelma, joka kysyy nimeä ja luo "omistuskirjoituksen" 
# käyttäjän haluamaan tiedostoon. Seuraavassa ohjelman esimerkkisuoritus:

kuka = input("Kenelle teos omistetaan:")
minne = input("Mihin kirjoitetaan:")

with open(minne, "w") as tiedosto:
	tiedosto.write(f"Hei {kuka}, toivomme \
viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")


# Tee ohjelma, joka mallintaa yksinkertaista päiväkirjaa. 
# Ohjelman tulee tallentaa päiväkirjamerkinnät tiedostoon paivakirja.txt. 
# Kun ohjelma käynnistetään, se lukee merkinnät tiedostosta.

while (True):
	teksti = ""
	komento = ""
	print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
	komento = input("Valinta:")
	if (komento == "1"):
		teksti = input("Anna merkintä:")
		with open("paivakirja.txt", "a")as tiedosto:
			tiedosto.write(f"{teksti}\n")
			print("Päiväkirja tallennettu")
	elif (komento == "2"):
		print("Merkinnät")
		with open('paivakirja.txt', 'r') as tiedosto:
			sisalto = tiedosto.read()
		print(sisalto)
	if (komento == "0"):
		print("Heippa!")
		break


# Kirjoita funktio suodata_laskut(), joka
# Lukee tiedoston laskut.csv sisällön ja
# kirjoittaa tiedostoon oikeat.csv ne rivit, 
# joilla laskutoimituksen lopputulos on oikein sekä
# kirjoittaa tiedostoon vaarat.csv ne rivit, 
# joilla laskutoimituksen lopputulos on väärin.
# Edellisestä esimerkistä tiedostoon oikeat.csv olisi siis kirjoitettu rivit

def tarkista_tulos(lasku):
	operandit = lasku.split('+') if '+' in lasku else lasku.split('-')
	if '+' in lasku:
		tulos = int(operandit[0]) + int(operandit[1])
	else:
		tulos = int(operandit[0]) - int(operandit[1])
	return tulos

def suodata_laskut():
	oikeat_file = open('oikeat.csv', 'w')
	vaarat_file = open('vaarat.csv', 'w')
	with open("laskut.csv", "r") as tiedosto:
		for rivi in tiedosto:
			nimi, lasku, tulos = rivi.strip().split(';')
			oikea_vastaus = tarkista_tulos(lasku)
		
			if int(tulos) == oikea_vastaus:
				oikeat_file.write(rivi)
			else:
				vaarat_file.write(rivi)

if __name__ == "__main__":
	suodata_laskut()


# Kirjoita funktio tallenna_henkilo(henkilo: tuple) 
# joka saa parametrikseen henkilöä kuvaavan tuplen. 
# Tuplessa on seuraavat tiedot tässä järjestyksessä:

def tallenna_henkilo(henkilo: tuple):
	with open("henkilot.csv", "w") as tiedosto:
		tiedosto.write(f"{henkilo[0]};{henkilo[1]};{henkilo[2]}")

if __name__ == "__main__":
	tuple = ("Kimmo Kimmonen", 37, 175.5)
	tallenna_henkilo(tuple)


# Tehtäväsi on kirjoittaa funktio hae_sanat(hakusana: str), 
# joka palauttaa listana annetun hakusanan mukaiset sanat tiedostosta.

# Hakusanassa voi käyttää pienten kirjainten lisäksi seuraavia erikoismerkkejä:

# Piste . tarkoittaa, että mikä tahansa merkki käy (esim ca. 
# vastaa vaikkapa sanoja cat ja car, p.ng sanoja ping ja pong 
# ja .a.e sanoja sane, care tai late.
# Asteriski * tarkoittaa, että sanan alku- tai loppuosaksi 
# käy mikä tahansa jono, esim. ca* vastaa vaikkapa sanoja 
# california, cat, caring tai catapult. Vastaavasti hakusana *ane vastaa 
# vaikkapa sanoja crane, insane tai aeroplane. Voit olettaa, 
# että asteriski on aina joko hakusanan alussa tai lopussa, 
# ja että hakusanassa esiintyy korkeintaan yksi asteriski.
# Jos hakusanassa ei ole erikoismerkkejä, haetaan vain 
# täsmälleen hakusanaa vastaava sana.

def tarkista_piste(hakusana :str):
	hakusanat = []

	with open("sanat.txt", "r") as tiedosto:
		tiedoston_sisalto = tiedosto.read()
		sanat = tiedoston_sisalto.split()
	for sana in sanat:
		if len(sana) != len(hakusana):
			continue
		osuma = True
		for i in range(len(hakusana)):
			if hakusana[i] == ".":
				continue
			if sana[i] != hakusana[i]:
				osuma = False
				break
		if osuma:
			hakusanat.append(sana)
	
	return (hakusanat)

def hae_sanat(hakusana :str):
	index = 0
	tulos = []
	star = 0
	piste = 0

	if ('*' in hakusana):
		if (hakusana[0] == '*'):
			star = 1
			sana = hakusana[:0] + hakusana[1:]
			
		elif(hakusana[len(hakusana) - 1] == '*'):
			star = 2
			sana = hakusana[:(len(hakusana) - 1)] + hakusana[(len(hakusana)):]
		else:
			sana = hakusana
	elif ('.' in hakusana):
		tulos = tarkista_piste(hakusana)

	with open("sanat.txt", "r") as tiedosto:
		teksti = tiedosto.read()
		sanat = teksti.split()
		# print(sanat, len(sanat))
		while (index < len(sanat)):
			if (star == 1):
				if (sanat[index].endswith(sana)):
					tulos.append(sanat[index])
					index += 1
				else:
					index += 1
			elif (star == 2):
				if (sanat[index].startswith(sana)):
					tulos.append(sanat[index])
					index += 1 
				else:
					index += 1
			elif (star == 0 and piste == 0):
				if (sanat[index] == hakusana):
					tulos.append(sanat[index])
					index += 1
				else:
					index += 1
	return (tulos)
	

if __name__ == "__main__":
	print(hae_sanat("*vokes"))
	print(hae_sanat("beac*"))
	print(hae_sanat("ca."))


# Tee sanakirjaa mallintava ohjelma, johon voi syöttää 
# uusia sanoja tai josta voi hakea syötettyjä sanoja.

# Ohjelman tulee toimia näin:

# Esimerkkitulostus
# 1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu
# Valinta: 1
# Anna sana suomeksi: auto
# Anna sana englanniksi: car
# Sanapari lisätty

sanakirja = {}

with open("sanakirja.txt", "w") as tiedosto:
	while (True):
		print("1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu")
		valinta = input("Valinta:")
		if (valinta == '1'):
			suomi = input("Anna sana suomeksi:")
			englanti = input("Anna sana englanniksi:")
			sanakirja[suomi] = englanti
			sanakirja[englanti] = suomi
			tiedosto.write(f"{suomi} - {englanti}")
			print("Sanapari lisätty")

		elif (valinta == '2'):
			sana = input("Anna sana:")
			if (sana in sanakirja or sana in tiedosto):
				print(f"{suomi} - {englanti}")

		elif (valinta == '3'):
			print("Moi!")
			break