# Kirjoita ohjelma, joka kysyy käyttäjältä merkkijonon ja määrän 
# ja tulostaa sitten annettua merkkijonoa annetun määrän. 
# Tulostuksen tulee tapahtua yhdelle riville yhteen pötköön.

jono = input("Anna merkkijono:")
count = int(input("Anna määrä:"))
print(f"{jono * count}")

# Kirjoita ohjelma, joka kysyy käyttäjältä kaksi merkkijonoa ja 
# tulostaa jonoista pidemmän (ts. sen, jossa on enemmän merkkejä). 
# Jos jonot ovat yhtä pitkiä tulostetaan viesti "Jonot ovat yhtä pitkät"

jono1 = input("Anna jono 1:")
jono2 = input("Anna jono 2:")
len1 = len(jono1)
len2 = len(jono2)
if (len1 > len2):
	print(f"{jono1} on pidempi")
elif (len2 > len1):
	print(f"{jono2} on pidempi")
else:
	print("Jonot ovat yhtä pitkät")

# Kirjoita ohjelma, joka kysyy käyttäjältä merkkijonon ja 
# tulostaa sitten merkkijonon merkit allekkain 
# käänteisessä järjestyksessä lopusta alkuun.

jono = input("Anna merkkijono:")
index = len(jono)
while (index > 0):
	print(f"{jono[index - 1]}")
	index -= 1

# Tee ohjelma, joka kysyy käyttäjältä sanan ja kertoo, 
# ovatko sen toinen ja toiseksi viimeinen merkki samoja.

sana = input("Anna sana:")
len = len(sana)
if (sana[1] == sana[-2]):
	print(f"Toinen ja toiseksi viimeinen kirjain on {sana[1]}")
else:
	print("Toinen ja toiseksi viimeinen kirjain eroavat")

# Sanalaatikko

sana = input("Sana: ")

leveys = 30
sanan_pituus = len(sana)
keskikohta = leveys // 2
sanan_keskipiste = sanan_pituus // 2
vasen_sivu = (keskikohta - len(sana) // 2) - 1
if (len(sana) % 2 == 0):
	oikea_sivu = vasen_sivu 
else:
	oikea_sivu = vasen_sivu - 1


# print(vasen_sivu, oikea_sivu)

print("*" * leveys)
print("*" + " " * vasen_sivu + sana + " " * oikea_sivu + "*")
print("*" * leveys)