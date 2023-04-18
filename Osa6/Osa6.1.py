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