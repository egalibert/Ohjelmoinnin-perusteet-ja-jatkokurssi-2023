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


