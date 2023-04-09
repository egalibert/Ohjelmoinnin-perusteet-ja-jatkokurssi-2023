# Tee sovellus, joka kysyy käyttäjältä PIN-koodia niin kauan, 
# kunnes käyttäjä antaa oikean PIN-koodin 4321. 
# Ohjelma kertoo yritysten lukumäärän:

test = 0
while (True):
	oikea = 4321
	pin = int(input("PIN-koodi:"))
	if (pin != oikea):
		print("Väärin")
		test += 1
	elif (pin == oikea):
		test += 1
		break
if (test == 1):
	print("Oikein, tarvitsit vain yhden yrityksen!")
else:
	print(f"Oikein, tarvitsit {test} yritystä")

# Tee ohjelma, joka kyselee käyttäjältä vuosilukua ja kertoo, 
# milloin on seuraava karkausvuosi.

# Jos käyttäjän syöttämä vuosi on karkausvuosi (kuten 2020), 
# ohjelma ei kerro tätä vuotta vaan sitä seuraavan karkausvuoden:

vuosi = int(input("Vuosi:"))

if vuosi % 4 == 0 and (vuosi % 100 != 0 or vuosi % 400 == 0):
	seuraava = vuosi + 4
else:
	vuosien_paassa = 4 - vuosi % 4
	if vuosien_paassa == 4:
		vuosien_paassa = 0
	seuraava = vuosi + vuosien_paassa
if (seuraava % 4 == 0 and seuraava % 100 == 0):
	if (seuraava % 400 != 0):
		seuraava += 4

print(f"Vuotta {vuosi} seuraava karkausvuosi on {seuraava}")

# Tee ohjelma, joka pyytää käyttäjää syöttämään sanoja. 
# Kun käyttäjä syöttää sanan loppu, 
# ohjelma tulostaa sanoista muodostuneen tarinan ja suoritus päättyy.

tarina = ""
edellinen = ""

while True:
	sana = input("Anna sana: ")
	if (sana == "loppu"):
		break
	if (edellinen == sana):
		break
	tarina += sana + " "
	edellinen = sana
print(f"{tarina}")

# Tee ohjelma, joka pyytää käyttäjää syöttämään kokonaislukuja. 
# Ohjelma pyytää lukuja niin kauan kunnes käyttäjä syöttää nollan.

print("Syötä kokonaislukuja, 0 lopettaa:")
count = 0
summa = 0
pos_count = 0
neg_count = 0

while(True):
	luku = int(input("Luku:"))
	if (luku != 0):
		count += 1
		summa += luku
		if (luku > 0):
			pos_count += 1
		else:
			neg_count += 1
	else:
		break
print(f"Lukuja yhteensä {count}")
print(f"Lukujen summa {summa}")
print(f"Lukujen keskiarvo {summa / count}")
print(f"Positiivisia {pos_count}")
print(f"Negatiivisia {neg_count}")