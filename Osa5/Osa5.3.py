# Tee funktio kertaa_kymmenen(alku: int, loppu: int), 
# joka muodostaa ja palauttaa uuden sanakirjan. 
# Sanakirjassa on avaimina luvut väliltä alku..loppu.

def kertaa_kymmenen(x , y):
	sanakirja = {}
	while (x <= y):
		sanakirja[x] = x * 10
		x += 1
	return (sanakirja)

if __name__ == "__main__":
	d = kertaa_kymmenen(3, 6)
	print(d)


# Tee funktio kertomat(n: int), joka palauttaa lukujen 1..n kertomat 
# sanakirjassa siten, että luku on avain ja luvun kertoma arvo, 
# johon avain viittaa.

def kertomat(n: int):
    kertomat = {}

    for i in range(1, n+1):
        kertoma = 1
        for j in range(1, i+1):
            kertoma *= j
        kertomat[i] = kertoma
    
    return kertomat

if __name__ == "__main__":
	k = kertomat(5)
	print(k[1])
	print(k[3])
	print(k[5])



# Tee funktio histogrammi, joka saa parametrina merkkijonon 
# ja tulostaa merkkijonon eri kirjainten lukumäärää kuvaavan histogrammin, 
# jossa kirjaimen jokaista esiintymää kohti tulostuu 
# yksi tähti kirjaimen riville.

def histogrammi(sana):
	kirjaimet = {}
	for kirjain in sana:
		if kirjain in kirjaimet:
			kirjaimet[kirjain] += 1
		else:
			kirjaimet[kirjain] = 1
	
	for kirjain, lkm in kirjaimet.items():
		print(kirjain + " " + "*" * lkm)

if __name__ == "__main__":
	histogrammi("abba")


# Tee puhelinluettelo, joka toimii seuraavasti:

# Esimerkkitulostus
# komento (1 hae, 2 lisää, 3 lopeta): 2
# nimi: pekka
# numero: 040-5466745
# ok!

luettelo = {}

while (True):
	komento = int(input("komento (1 hae, 2 lisää, 3 lopeta):"))
	if (komento == 2):
		nimi = input("nimi:")
		p_num = input("numero:")
		luettelo[nimi] = p_num
		print("ok!")
	elif (komento == 1):
		nimi = input("nimi:")
		if (nimi in luettelo):
			print(luettelo[nimi])
		else:
			print("ei numeroa")
	else:
		print("lopetetaan...")
		break


# Tee puhelinluettelosta paranneltu versio, 
# missä jokaisella henkilöllä voi olla useampia puhelinnumeroita. 
# Ohjelma toimii kuten edellisessä tehtävässä, 
# mutta nyt se listaa jokaisen numeron:

luettelo = {}

while (True):
	komento = int(input("komento (1 hae, 2 lisää, 3 lopeta):"))
	if (komento == 1):
		nimi = input("nimi:")
		if (nimi in luettelo):
			numerot = luettelo[nimi]
			for p_num in numerot:
				print(p_num)
		else:
			print("ei numeroa")
	elif (komento == 2):
		nimi = input("nimi:")
		p_num = input("numero:")
		if (nimi in luettelo):
			luettelo[nimi].append(p_num)
		else:
			luettelo[nimi] = [p_num]
		print("ok!")
	else:
		print("lopetetaan...")
		break



# Kirjoita funktio kaanna(sanakirja: dict), 
# joka saa parametrikseen sanakirjan ja kääntää sen niin, 
# että arvoista tulee avaimia ja päinvastoin.

def kaanna(sanakirja):
    kaannetty = {}
    for avain, arvo in sanakirja.items():
        kaannetty[arvo] = avain
    sanakirja.clear()
    sanakirja.update(kaannetty)

if __name__ == "__main__":
	s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
	kaanna(s)
	print(s)



# Kirjoita funktio lukukirja(), joka palauttaa uuden sanakirjan. 
# Palautettu rakenne sisältää avaimina luvut nollasta 99:ään. 
# Sanakirjan arvoina ovat luvut kirjaimin kirjoitettuna. Katso esimerkkiä alla:

def lukukirja():
	ykkoset = ['', 'yksi', 'kaksi', 'kolme', 'neljä', 'viisi',
				'kuusi', 'seitsemän', 'kahdeksan', 'yhdeksän']
	kymmenet = ['', '', 'kaksikymmentä', 'kolmekymmentä', 'neljäkymmentä',
				'viisikymmentä', 'kuusikymmentä','seitsemänkymmentä', 
				'kahdeksankymmentä', 'yhdeksänkymmentä']
	erikoistapaukset = {
		0: 'nolla',
		10: 'kymmenen',
		11: 'yksitoista',
		12: 'kaksitoista',
		13: 'kolmetoista',
		14: 'neljätoista',
		15: 'viisitoista',
		16: 'kuusitoista',
		17: 'seitsemäntoista',
		18: 'kahdeksantoista',
		19: 'yhdeksäntoista',
	}
	sanakirja = {}
	for i in range(100):
		if i in erikoistapaukset:
			sanakirja[i] = erikoistapaukset[i]
		else:
			sanakirja[i] = kymmenet[i // 10] + ykkoset[i % 10]
	return sanakirja


if __name__ == "__main__":
	luvut = lukukirja()
	print(luvut[2])
	print(luvut[11])
	print(luvut[45])
	print(luvut[99])
	print(luvut[0])


# Kirjoita funktio lisaa_elokuva(rekisteri: 
# list, nimi: str, ohjaaja: str, vuosi: int, pituus: int), 
# joka lisää yhden elokuvaolion elokuvarekisteriin.

def lisaa_elokuva(rekisteri, nimi_a, ohjaaja_a, vuosi_a, pituus_a):
	i = len(rekisteri)
	elokuva = {}
	elokuva["nimi"] = nimi_a 
	elokuva["ohjaaja"] = ohjaaja_a
	elokuva["vuosi"] = vuosi_a
	elokuva["pituus"] = pituus_a
	rekisteri.append(elokuva)
	

if __name__ == "__main__":
	rekisteri = []
	lisaa_elokuva(rekisteri, "Pythonin viemää", "Pekka Python", 2017, 116)
	lisaa_elokuva(rekisteri, "Python lentokoneessa", "Renny Pytholin", 2001, 94)
	print(rekisteri)


# Kirjoita funktio etsi_elokuvat(rekisteri: list, hakusana: str), 
# joka käsittelee edellisessä tehtävässä luotua elokuvarekisteriä. 
# Funktio muodostaa uuden listan, jolle kopioidaan rekisteristä ne elokuvat, 
# joiden nimestä löytyy hakusana. Pienet ja isot kirjaimet 
# eivät merkitse haussa, joten hakusanalla paj pitää löytyä sekä elokuva
# Tappajahai että elokuva Pajatoiminnan historia.

