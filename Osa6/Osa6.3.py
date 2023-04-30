# Tee funktio lue, joka kysyy käyttäjältä syötettä,
# kunnes se on parametrien määrittelemällä välillä oleva kokonaisluku. 
# Funktio palauttaa käyttäjän antaman syötteen.

# Funktio toimii seuraavasti:

def lue(teksti :str, min :int, max :int):
	while (True):
		luku = input(teksti)
		try:
			luku = int(luku)
			if (luku > min and luku < max):
				return luku
			else:
				print(f"Syötteen on oltava kokonaisluku väliltä {min}...{max}")
		except ValueError:
			print(f"Syötteen on oltava kokonaisluku väliltä {min}...{max}")


if __name__ == "__main__":
	luku = lue('Anna luku', 5, 10)
	print("syötit luvun:", luku)


# Kirjoita funktio uusi_henkilo(nimi: str, ika: int), 
# joka luo ja palauttaa uuden henkilö-tuplen. 
# Tuplessa ensimmäinen alkio on nimi ja jälkimmäinen ikä.

# Jos funktion parametrit ovat virheelliset, 
# sen tulee tuplen palauttamisen sijasta tuottaa ValueError-poikkeus.

# Virheellisiä parametreja tässä tapauksessa ovat:

# nimi on tyhjä merkkijono
# nimi ei koostu vähintään kahdesta sanasta
# nimen pituus on yli 40 merkkiä
# ikä on negatiivinen luku
# ikä on suurempi kuin 150

def uusi_henkilo(nimi: str, ika: int) -> tuple:
    if not nimi or len(nimi.split()) < 2 or len(nimi) > 40:
        raise ValueError("Nimi on virheellinen")
    if ika < 0 or ika > 150:
        raise ValueError("Ikä on virheellinen")
    return (nimi, ika)


# Tiedostoon lottonumerot.csv on tallennettu lottonumeroita 
# seuraavan esimerkin mukaisesti:

# Esimerkkidata
# viikko 1;5,7,11,13,23,24,30
# viikko 2;9,13,14,24,34,35,37
# ...jne...
# Aluksi pitäisi olla siis otsikko viikko x, 
# ja sen jälkeen seitsemän numeroa väliltä 1...39.

import csv

def poista_virheelliset_rivit(tiedostonimi):

	with open(tiedostonimi, 'r') as infile:
		reader = csv.reader(infile, delimiter=';')
		rows = [row for row in reader if len(row[1].split(',')) == 7] # Poistetaan rivit, jotka sisältävät enemmän kuin 7 numeroa

	with open(tiedostonimi, 'w', newline='') as outfile:
		writer = csv.writer(outfile, delimiter=';')
		for row in rows:
			writer.writerow(row)

def suodata_virheelliset():
	with open('lottonumerot.csv', 'r') as csvfile:
		with open('korjatut_numerot.csv', 'w', newline='') as outfile:
			writer = csv.writer(outfile, delimiter=';')
			writer.writerow(['viikko', 'numero1', 'numero2', 'numero3', 'numero4', 'numero5', 'numero6', 'numero7'])
			reader = csv.reader(csvfile, delimiter=';')
			for row in reader:
				if len(row) != 2:
					continue
				viikko, numerot_str = row
				numerot = numerot_str.split(',')
				if len(numerot) != 7:
					continue
				try:
					numerot = [int(n) for n in numerot]
				except ValueError:
					continue
				if not all(1 <= n <= 39 for n in numerot):
					continue
				if len(set(numerot)) != 7:
					continue
				writer.writerow([viikko] + numerot)
	poista_virheelliset_rivit("korjatut_numerot.csv")