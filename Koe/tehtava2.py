# A) Palauttaa listan tupleja parametrina annetun merkkijonon perusteella. 
# Listan tuplet ovat kaksipaikkaisia. 
# Merkkijonot ovat muotoa "jono1a;jono1b,jono2a;jono2b,jono3a; ...". 
# Tuplet erotellaan merkkijonosta pilkun perusteella ja tuplen osat puolipisteellä, 
# niin että puolipisteen vasemmanpuolinen merkkijono on tuplen vasemmanpuolinen alkio.

# B) Palauttaa sanakirjan parametrina annetun listan pohjalta. 
# Annettu lista koostuu kaksipaikkaisista tupleista, kuten a-kohdan funktion paluuarvo. 
# Sanakirja rakennetaan niin, että listan tuplet vastaavat avain-arvo-pareja,
# missä tuplen vasen alkio on avain ja oikea alkio on arvo.

# Tee tehtävän 2 ratkaisu tänne

def erottele(merkkijono: str):
	uusi_tuple = ()
	final = []
	osa1 = ""
	osa2 = ""
	i = 0
	while (i < len(merkkijono) - 1):
		osa1 = ""
		osa2 = ""
		uusi_tuple = ()
		while (merkkijono[i].isalpha() or merkkijono[i].isspace()):
			osa1 += merkkijono[i]
			i += 1
		i += 1
		while (merkkijono[i].isalpha() or merkkijono[i].isspace()):
			osa2 += merkkijono[i]
			i += 1
			if (i == len(merkkijono)):
				i -= 1
				break
		i += 1
		uusi_tuple = (osa1, osa2)
		final.append(uusi_tuple)
	return (final)

def sanakirjaksi(lista: list):
	sanakirja = {}
	for pari in lista:
		sanakirja[pari[0]] = pari[1]
	return (sanakirja)

# def main():
# 	lista1 = erottele('maa;suomi,kaupunki;helsinki,huone;keittio')
# 	lista2 = erottele('nimi;ella')
# 	lista3 = erottele('valmistaja;aston martin,kuski;vettel')

# 	print(lista1) # [('maa', 'suomi'), ('kaupunki', 'helsinki'), ('huone','keittio')]
# 	print(lista2) # [('nimi', 'ella')]
# 	print(lista3) # [('valmistaja', 'aston martin'), ('kuski', 'vettel')]

# def main():
# 	sanakirja1 = sanakirjaksi([('maa', 'suomi'), ('kaupunki', 'helsinki'), ('huone','keittio')])
# 	sanakirja2 = sanakirjaksi([('nimi', 'ella')])
# 	sanakirja3 = sanakirjaksi([('valmistaja', 'aston martin'), ('kuski', 'vettel')])

# 	print(sanakirja1) # {'maa': 'suomi', 'kaupunki': 'helsinki', 'huone': 'keittio'}
# 	print(sanakirja2) # {'nimi': 'ella'}
# 	print(sanakirja3) # {'valmistaja': 'aston martin'



# main()