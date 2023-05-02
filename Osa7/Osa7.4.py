# Toteuta funktio tulosta_henkilot(tiedosto: str), 
# joka lukee esimerkin tavalla muodostetun JSON-tiedoston 
# (jonka sisältönä voi olla mielivaltainen määrä henkilöitä) 
# ja tulostaa ne seuraavassa muodossa:

import json

def tulosta_henkilot(tiedosto: str):
	with open(tiedosto) as f:
		data = json.load(f)

	for person in data:
		harrastukset = ", ".join(person["harrastukset"])
		print(f"{person['nimi']} {person['ika']} vuotta ({harrastukset})")

if __name__ == "__main__":
	tulosta_henkilot("tiedosto1.json")






# Tehtäväsi on etsiä ne opiskelijat, jotka ovat käyttäneet tenttiin 
# yli 3 tuntia aikaa, eli opiskelijat, joiden jonkin tehtävän palautus on 
# tehty yli 3 tuntia tentin aloitusajasta. 
# Palautuksia voi siis olla useampi. Voit olettaa, 
# että kaikki ajat ovat saman vuorokauden puolella.

import csv
from datetime import datetime, timedelta

def huijarit():
	aloitusajat = {}
	with open('tentin_aloitus.csv') as file:
		for line in file:
			opiskelija, aika = line.strip().split(';')
			tunnit, minuutit = map(int, aika.split(':'))
			aloitusajat[opiskelija] = tunnit * 60 + minuutit
	huijarit = []
	with open('palautus.csv') as file:
		for line in file:
			opiskelija, _, _, aika = line.strip().split(';')
			tunnit, minuutit = map(int, aika.split(':'))
			palautusaika = tunnit * 60 + minuutit
			if palautusaika - aloitusajat[opiskelija] > 180:
				if opiskelija not in huijarit:
					huijarit.append(opiskelija)
	return huijarit



# Käytössäsi on edellisessä tehtävässä määritellyt datatiedostot. 
# Kirjoita funktio viralliset_pisteet(), 
# joka palauttaa sanakirjassa (dict) opiskelijoiden koepisteet 
# seuraavien sääntöjen mukaan:

# Jos samaan tehtävänumeroon on tehty useita palautuksia, 
# korkeimman pistemäärän palautus otetaan huomioon
# Jos tehtäväpalautus on tehty yli 3 tuntia tentin aloittamisen jälkeen, 
# palautusta ei huomioida ollenkaan
# Tehtävät on numeroitu 1–8 ja jokaisesta tehtävästä voi saada 0–6 pistettä.

# Palautetussa sanakirjassa tunnus on avain ja tehtävien yhteispistemäärä arvo.

# Vinkki: sisäkkäiset sanakirjat (dict)
#  ovat mainio työkalua tallennettaessa eri opiskelijoiden pisteitä ja aikoja.


from datetime import datetime, timedelta

def viralliset_pisteet():
	
	with open("tentin_aloitus.csv", "r") as tiedosto:
		aloitukset = {}
		for rivi in tiedosto:
			opiskelija, aika = rivi.strip().split(";")
			aloitukset[opiskelija] = datetime.strptime(aika, "%H:%M")

	pisteet = {}
	with open("palautus.csv", "r") as tiedosto:
		for rivi in tiedosto:
			fields = rivi.strip().split(";")
			if len(fields) != 4:
				print(f"Invalid input: {rivi}")
				continue
			opiskelija, tehtava, pisteet_str, aika = fields
			try:
				pisteet_luku = int(pisteet_str)
				palautus_aika = datetime.strptime(aika, "%H:%M")
			except ValueError:
				print(f"Invalid input: {rivi}")
				continue
			if opiskelija not in aloitukset:
				print(f"Start time not found for student {opiskelija}")
				continue
			tentti_aika = palautus_aika - aloitukset[opiskelija]
			if tentti_aika > timedelta(hours=3):
				print(f"Cheating detected: {opiskelija}")
				continue
			if opiskelija not in pisteet:
				pisteet[opiskelija] = {}
			if tehtava not in pisteet[opiskelija] or pisteet_luku > pisteet[opiskelija][tehtava]:
				pisteet[opiskelija][tehtava] = pisteet_luku

	yhteispisteet = {}
	for opiskelija in pisteet:
		yhteispisteet[opiskelija] = sum(pisteet[opiskelija].values())

	return yhteispisteet


