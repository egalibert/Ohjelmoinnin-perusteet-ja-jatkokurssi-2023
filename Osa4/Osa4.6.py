# Kirjoita funktio kaikki_vaarinpain, joka saa parametrikseen 
# listan merkkijonoja. Funktio luo ja palauttaa uuden listan, 
# jossa kaikki alkuperäisellä listalla olevat merkkijonot on käännetty. 
# Myös listan alkioiden järjestys muutetaan käänteiseksi.

def kaikki_vaarinpain(lista):
	return [x[::-1] for x in lista][::-1]

if __name__ == "__main__":
	lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
	lista2 = kaikki_vaarinpain(lista)
	print(lista2)


# Kirjoita funktio eniten_kirjainta, joka saa parametrikseen merkkijonon. 
# Funktio palauttaa kirjaimen, jota esiintyy eniten merkkijonossa. 
# Jos yhtä yleisiä kirjaimia on monta, 
# funktion tulee palauttaa niistä ensimmäisenä merkkijonossa esiintyvä.

def eniten_kirjainta(jono):
	paras = 1
	tulos = 0
	kirjain = ""
	for i in jono:
		tulos = jono.count(i)
		if (tulos > paras):
			paras = tulos
			kirjain = i
	return (kirjain)

if __name__ == "__main__":
	mjono = "abcbdbe"
	print(eniten_kirjainta(mjono))

	toinen_jono = "esimerkkimerkkijonokki"
	print(eniten_kirjainta(toinen_jono))


# Kirjoita funktio ilman_vokaaleja, 
# joka saa parametrikseen merkkijonon. 
# Funktio palauttaa uuden merkkijonon, 
# jossa alkuperäisen merkkijonon vokaalit on poistettu.

# Voit olettaa, että merkkijono koostuu pelkästään 
# pienistä suomen kielen kirjaimista a...ö.

def ilman_vokaaleja(jono):
	new_jono = ""
	for i in jono:
		if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or \
			i == 'y' or i == 'ä' or i == 'ö' or i == 'å'):
			continue
		else:
			new_jono += i
	return new_jono


if __name__ == "__main__":
	mjono = "tämä on esimerkki"
	print(ilman_vokaaleja(mjono))


# Kirjoita metodia hyödyntäen funktio poista_isot, 
# joka saa parametrikseen listan merkkijonoja.
# Funktio palauttaa uuden listan, jolla on sen parametrina olevasta 
# listasta ne merkkijonot, jotka eivät koostu kokonaan isoista kirjaimista.

def poista_isot(lista):
	uusi_lista = []
	for i in lista:
		if (i.isupper() == True):
			continue
		else:
			uusi_lista.append(i)
	return uusi_lista

if __name__ == "__main__":
	lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
	karsittu_lista = poista_isot(lista)
	print(karsittu_lista)


# Määritellään, että listan alkiot ovat naapureita, jos niiden erotus on 1. 
# Naapureita olisivat siis esim alkiot 1 ja 2 tai alkiot 56 ja 55.

# Kirjoita funktio pisin_naapurijono, joka etsii listasta pisimmän peräkkäisiä 
# naapureita sisältävän osalistan ja palauttaa sen pituuden.

def pisin_naapurijono(lista):
	i = 0
	paras = 0
	pituus = len(lista)
	while (i < pituus - 1):
		tulos = 1
		while (lista[i] - lista[i + 1] == 1 or lista[i + 1] - lista[i] == 1):
			print(f"{lista[i]} ja {lista[i + 1]}")
			tulos += 1
			i += 1
			print(i, pituus)
			if (i + 1 == pituus):
				break
		if (tulos > paras):
			paras = tulos
		i += 1
	return (paras)


if __name__ == "__main__":
	lista = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25, 30]
	print(pisin_naapurijono(lista))


# Tässä tehtävässä toteutetaan ohjelma kurssin arvosanatilastojen tulostamiseen.

# Ohjelmalle syötetään rivejä, jotka sisältävät yhden opiskelijan 
# koepistemäärän sekä tehtyjen harjoitustehtävien määrän. 
# Ohjelma tulostaa niiden perusteella arvosanoihin liittyviä tilastoja.

def jakauma(lista):
	index = 5
	while (index >= 0):
		print(f"	{index}: {lista.count(index) * '*'} ")
		index -= 1


def laske_prosentti(lista):
	index = 0
	for i in lista:
		if (i > 0):
			index += 1
	return ((index / len(lista)) * 100)


def laske_arvosana(pisteet):
	if (pisteet < 15):
		return 0
	elif (pisteet < 18):
		return 1
	elif (pisteet < 21):
		return 2
	elif (pisteet < 24):
		return 3
	elif (pisteet < 28):
		return 4
	else:
		return 5

def laske_h_pisteet(pisteet):
	pisteet = pisteet // 10
	return (pisteet)

def main():
	keskiarvo = []
	arvosanat = []
	while (True):
		syote = (input("Koepisteet ja harjoitusten määrä:"))
		if (syote == ""):
			print("Tilasto:")
			print(f"Pisteiden keskiarvo: {round(sum(keskiarvo) / len(keskiarvo), 1)}")
			print(f"Hyväksymisprosentti: {round(lapaisy_pro, 1)}")
			print(f"Arvosanajakauma:")
			jakauma(arvosanat)
			break
		syote = syote.split()
		koe = int(syote[0])
		harjoitus = int(syote[1])

		h_pisteet = laske_h_pisteet(harjoitus)
		tulos = h_pisteet + koe
		keskiarvo.append(tulos)

		if (koe < 10):
			arvosanat.append(0)
		else:
			arvosanat.append(laske_arvosana(tulos))

		lapaisy_pro = laske_prosentti(arvosanat)

main()