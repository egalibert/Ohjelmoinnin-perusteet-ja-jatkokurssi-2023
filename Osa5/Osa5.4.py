# Tee funktio tee_tuple(x: int, y: int, z: int), 
# joka muodostaa ja palauttaa parametrinaan saamistaan 
# kokonaisluvuista tuplen seuraavien sääntöjen mukaaan:

# Tuplen ensimmäinen alkio on parametreista pienin
# Tuplen toinen alkio on parametreista suurin
# Tuplen kolmas alkio on parametrien summa

def tee_tuple (i, x, y):
	summa = i + x + y
	isoin = max(i, x, y)
	pienin = min(i, x, y)
	tuple = (pienin, isoin, summa)
	return (tuple)

if __name__ == "__main__":
    print(tee_tuple(5, 3, -1))


# Tee funktio vanhin(henkilot: list), 
# joka saa parametrikseen listan henkilöitä esittäviä tupleja. 
# Funktio etsii ja palauttaa vanhimman henkilön nimen.

# Henkilötuplessa on ensin henkilön nimi merkkijonona ja 
# toisena alkiona henkilön syntymävuosi.

def vanhin(henkilot):
	vanhin = 2030
	nimi = ""
	for henkilo in henkilot:
		if (henkilo[1] < vanhin):
			vanhin = henkilo[1]
			nimi = henkilo[0]
		print (henkilo[1])
	return (nimi)

if __name__ == "__main__":
	h1 = ("Arto", 1977)
	h2 = ("Einari", 1985)
	h3 = ("Maija", 1953)
	h4 = ("Essi", 1997)
	hlista = [h1, h2, h3, h4]

	print(vanhin(hlista))


# Kirjoita funktio vanhemmat(henkilot: list, vuosi: int), 
# joka palauttaa uuden listan, jolle on tallennettu kaikki 
# ennen annettua vuotta syntyneet henkilöiden nimet parametrina 
# saadulta henkilöiden listalta.

def vanhemmat(lista :list, vuosi :int):
	uusi_lista = []
	for henkilo in lista:
		if (henkilo[1] < vuosi):
			uusi_lista.append(henkilo[0])
	return (uusi_lista)

if __name__ == "__main__":
	h1 = ("Arto", 1977)
	h2 = ("Einari", 1985)
	h3 = ("Maija", 1953)
	h4 = ("Essi", 1997)
	hlista = [h1, h2, h3, h4]

	vanhemmat_henkilot = vanhemmat(hlista, 1979)
	print(vanhemmat_henkilot)


# Tässä tehtäväsarjassa toteutetaan yksinkertainen opiskelijarekisteri. 
# Ennen ohjelmoinnin aloittamista kannattanee hetki miettiä, 
# minkälaisen tietorakenteen tarvitset ohjelman 
# tallentamien tietojen organisointiin.

def lisaa_opiskelija(sanakirja, nimi):
	sanakirja[nimi] = {}
	return (sanakirja)

def tulosta(sanakirja, nimi):
	if nimi in sanakirja:
		print(f"{nimi}:")
		if 'suoritukset' in sanakirja[nimi]:
			suoritukset = sanakirja[nimi]['suoritukset']
			if (len(suoritukset) != 0):
				print(f" suorituksia {len(suoritukset)} kurssilta:")
			else:
				print(" ei suorituksia")
			for kurssi, arvosana in suoritukset:
				print(f"  {kurssi} {arvosana}")
			if (len(suoritukset) != 0):
				keskiarvo = sum([s[1] for s in suoritukset]) / len(suoritukset)
				print(f" keskiarvo {keskiarvo}")
		else:
			print(" ei suorituksia")
	else:
		print(f"ei löytynyt ketään nimellä {nimi}")

def lisaa_suoritus(sanakirja, nimi, suoritus):
	if nimi in sanakirja:
		if 'suoritukset' not in sanakirja[nimi]:
			sanakirja[nimi]['suoritukset'] = []
		kurssin_suoritukset = [s for s in sanakirja[nimi]['suoritukset'] if s[0] == suoritus[0]]
		if not kurssin_suoritukset and suoritus[1] != 0:
			sanakirja[nimi]['suoritukset'].append(suoritus)
		elif kurssin_suoritukset and suoritus[1] > kurssin_suoritukset[-1][1]:
			sanakirja[nimi]['suoritukset'].remove(kurssin_suoritukset[-1])
			sanakirja[nimi]['suoritukset'].append(suoritus)
	else:
		print(f"Opiskelijaa {nimi} ei löytynyt.")

def kooste(sanakirja):
	print(f"opiskelijoita {len(sanakirja)}")
	eniten_suorituksia = 0
	eniten_suorituksia_nimi = ""
	paras_keskiarvo = 0
	paras_keskiarvo_nimi = ""
    
	for nimi in sanakirja:
		suoritukset = sanakirja[nimi]["suoritukset"]
		kurssit = set()
		suoritukset_summa = 0
		for kurssi, arvosana in suoritukset:
			if arvosana > 0:
				kurssit.add(kurssi)
				suoritukset_summa += arvosana
		keskiarvo = suoritukset_summa / len(kurssit) if kurssit else 0
		
		if len(kurssit) > eniten_suorituksia:
			eniten_suorituksia = len(kurssit)
			eniten_suorituksia_nimi = nimi
		
		if keskiarvo > paras_keskiarvo:
			paras_keskiarvo = keskiarvo
			paras_keskiarvo_nimi = nimi
			
	print("eniten suorituksia", eniten_suorituksia, eniten_suorituksia_nimi)
	print("paras keskiarvo", paras_keskiarvo, paras_keskiarvo_nimi)



# Tee ohjelma, joka tulostaa kirjainruudukon oheisten esimerkkien mukaisesti. 
# Voit olettaa, että kerroksia on enintään 26.

def print_kuvio(kerrokset: int):
	lista = [[0 for i in range(0, kerrokset *2 - 1)] for j in range(0, kerrokset * 2 -1)]
	dim = kerrokset * 2 - 1
	for i in range(kerrokset):
		for j in range(dim - 2 * i):
			lista[i][j + i] = (kerrokset - i)
			lista[dim - i - 1][j + i] = (kerrokset - i)
			lista[j + i][i] = (kerrokset - i)
			lista[j + i][dim - i - 1] = (kerrokset - i)
	for rivi in lista:
		for kirjain in rivi:
			kirjaimet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
			print(''.join(kirjaimet[kirjain - 1]), end='')
		print()

def main():
	kerrokset = int(input("Kerrokset:"))
	(print_kuvio(kerrokset))


main()