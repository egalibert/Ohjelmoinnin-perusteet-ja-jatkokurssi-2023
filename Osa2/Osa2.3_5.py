# Vuosi on karkausvuosi, jos se on jaollinen 4:llä. 
# Kuitenkin jos vuosi on jaollinen 100:lla, se on karkausvuosi vain silloin, 
# kun se on jaollinen myös 400:lla.

# Tee ohjelma, joka lukee käyttäjältä vuosiluvun, 
# ja tarkistaa, onko vuosi karkausvuosi.

luku = int(input("Anna vuosi:"))
if (luku % 4 == 0 and luku % 100 == 0):
	if (luku % 400 == 0):
		print("Vuosi on karkausvuosi.")
	else:
		print("Vuosi ei ole karkausvuosi.")
elif (luku % 4 == 0 and luku % 100 != 0):
	print("Vuosi on karkausvuosi.")
else:
	print("Vuosi ei ole karkausvuosi.")

# Tee ohjelma, joka kysyy käyttäjältä kolme kirjainta. 
# Ohjelma tulostaa kirjaimista aakkosjärjestyksessä keskimmäisen.

# Voit olettaa, että kirjaimet ovat 
# joko kaikki isoja tai kaikki pieniä kirjaimia

kirjain1 = input("Anna 1. kirjain:")
kirjain2 = input("Anna 2. kirjain:")
kirjain3 = input("Anna 3. kirjain:")
if (kirjain1 > kirjain2 and kirjain1 > kirjain3):
	if (kirjain2 > kirjain3):
		print(f"Keskimmäinen kirjain on {kirjain2}")
	else:
		print(f"Keskimmäinen kirjain on {kirjain3}")
elif (kirjain2 > kirjain1 and kirjain2 > kirjain3):
	if (kirjain1 > kirjain3):
		print(f"Keskimmäinen kirjain on {kirjain1}")
	else:
		print(f"Keskimmäinen kirjain on {kirjain3}")
elif (kirjain3 > kirjain1 and kirjain3 > kirjain2):
	if (kirjain1 > kirjain2):
		print(f"Keskimmäinen kirjain on {kirjain1}")
	else:
		print(f"Keskimmäinen kirjain on {kirjain2}")

# Tee ohjelma, joka laskee lahjaveron lähimpien sukulaisten antamalle lahjalle. 
# Alla on muutama esimerkki ohjelman toiminnasta.

lahja = int(input("Lahjan suuruus?"))
vero = 0
if (lahja < 5000):
	print("Ei veroa!")
elif (lahja <= 25000):
	vero = 100 + (lahja - 5000) * 0.08
elif (lahja <= 55000):
	vero = 1700 + (lahja - 25000) * 0.1
elif (lahja <= 200000):
	vero = 4700 + (lahja - 55000) * 0.12
elif (lahja <= 1000000):
	vero = 22100 + (lahja - 200000) * 0.15
else:
	vero = 142100 + (lahja - 1000000) * 0.17
if (vero != 0):
	print(f"Vero: {vero} euroa")
