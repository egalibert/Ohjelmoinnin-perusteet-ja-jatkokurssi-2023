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



# Ohjelmassa kirjoitetaan käyttäjän määrittelemään tiedostoon "ruutuaikoja", eli käyttäjän television, tietokoneen ja mobiililaitteen ääressä tiettyinä päivinä viettämää aikaa.

# Ohjelma toimii seuraavasti:

# Esimerkkitulostus
# Tiedosto: kesakuun_loppu.txt
# Aloituspäivä: 24.6.2020
# Montako päivää: 5
# Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite):
# Ruutuaika 24.06.2020: 60 120 0
# Ruutuaika 25.06.2020: 0 0 0
# Ruutuaika 26.06.2020: 180 0 0
# Ruutuaika 27.06.2020: 25 240 15
# Ruutuaika 28.06.2020: 45 90 5
# Tiedot tallennettu tiedostoon kesakuun_loppu.txt
# Kunkin päivän riville on siis annettu välilyönnillä eroteltuna kolme minuuttimäärää.

# Ohjelma tallentaa tilaston ruutuajoista tiedostoon kesakuun_loppu.txt, joka näyttää yllä olevalla syötteellä seuraavalta:

# Esimerkkidata
# Ajanjakso: 24.06.2020-28.06.2020
# Yht. minuutteja: 780
# Keskim. minuutteja: 156.0
# 24.06.2020: 60/120/0
# 25.06.2020: 0/0/0
# 26.06.2020: 180/0/0
# 27.06.2020: 25/240/15
# 28.06.2020: 45/90/5

# filename = input("Anna tiedoston nimi: ")
# start_date = input("Anna aloituspäivämäärä (pp.kk.vvvv): ")
# num_days = int(input("Anna päivien määrä: "))

filename = "vappu.txt"
start_date = "1.5.2020"
num_days = 1

with open(filename, "w") as file:
	file.write("Aloituspäivä: " + start_date + "\n")
	file.write("Montako päivää: " + str(num_days) + "\n")
	for i in range(num_days):
		print("Ruutuaika", start_date + ":", end=" ")
		tv, computer, mobile = input().split()
		file.write(start_date + ": " + tv + "/" + computer + "/" + mobile + "\n")

	with open(filename, "r") as file:
		lines = file.readlines()
		# start_date = datetime(start_date)
		end_date = datetime(start_date) + datetime(num_days)
		total_time = 0
		tv_time, computer_time, mobile_time = 0, 0, 0
		for line in lines[2:]:
			day, times = line.strip().split(": ")
			tv, computer, mobile = map(int, times.split("/"))
			total_time += tv + computer + mobile
			tv_time += tv
			computer_time += computer
			mobile_time += mobile
			print(day + ":", times)
	print("Ajanjakso:", start_date + "-" + end_date)
	print("Yht. minuutteja:", total_time)
	print("Keskim. minuutteja:", total_time / num_days)