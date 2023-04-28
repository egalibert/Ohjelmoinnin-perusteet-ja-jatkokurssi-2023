# Tee ohjelma, joka kysyy käyttäjän syntymäajan 
# (erikseen päivä, kuukausi ja vuosi) ja tulostaa,
# kuinka monta päivää vanha käyttäjä oli 31.12.1999 
# seuraavan esimerkin mukaisesti:

from datetime import datetime

day = int(input("Päivä:"))
month = int(input("Kuukausi:"))
year = int(input("Vuosi:"))

target = datetime(1999, 12, 31)
annettu = datetime(year, month, day)
erotus = target-annettu

if (year <= 1999):
	print(f"Olit {erotus.days} päivää vanha, kun vuosituhat vaihtui.")
else:
	print(f"Et ollut syntynyt, kun vuosituhat vaihtui.")


# Tee funktio onko_validi(hetu: str), joka palauttaa True tai False sen mukaan, 
# onko annettu henkilötunnus oikea. Henkilötunnus on muotoa ppkkvvXyyyz, 
# jossa ppkkvv kertoo syntymäajan (päivä/kuukausi/vuosi), 
# X on syntymävuosisadasta riippuva välimerkki, 
# yyy henkilökohtainen yksilönumero ja z tarkistemerkki.

from datetime import datetime

def onko_validi(hetu: str):
	tarkastusmerkki = "0123456789ABCDEFHJKLMNPRSTUVWXY"
	paiva = ""
	vuosi = ""
	kuukausi = ""

	if (len(hetu) != 11):
		return (False)

	luku = hetu[7] + hetu[8] + hetu[9]

	if (hetu[6] == '-'):
		vuosi += "19"
	elif (hetu[6] == '+'):
		vuosi += "18"
	elif (hetu[6] == 'A'):
		vuosi += "20"
	else:
		return (False)

	paiva = hetu[0] + hetu[1]
	kuukausi = hetu[2] + hetu[3]
	vuosi += hetu[4] + hetu[5]

	print(paiva, kuukausi, vuosi)

	try:
		datetime(int(vuosi), int(kuukausi), int(paiva))
	except ValueError:
		print("Virhe syntymajassa")
		return False

	luku = int(hetu[:6] + hetu[7:10])
	jakojäännös = luku % 31
	tarkistemerkki = tarkastusmerkki[jakojäännös]
	
	if tarkistemerkki == hetu[len(hetu) -1]:
		return True
	else:
		return False


def main():
	hetu = "030103A493DD"
	print(onko_validi(hetu))

if __name__ == "__main__":
	main()


# Ohjelmassa kirjoitetaan käyttäjän määrittelemään tiedostoon "ruutuaikoja", 
# eli käyttäjän television, tietokoneen ja mobiililaitteen 
# ääressä tiettyinä päivinä viettämää aikaa.

