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