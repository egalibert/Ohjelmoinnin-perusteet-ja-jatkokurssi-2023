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