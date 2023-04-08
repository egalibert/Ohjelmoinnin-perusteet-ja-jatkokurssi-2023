# Tee ohjelma, joka kysyy käyttäjän ikää. 
# Jos ikä ei ole uskottava (se on alle 5 tai mahdoton luku iälle), 
# antaa ohjelma siihen liittyvän kommentin

ika = int(input("Kerro ikäsi?"))
if (ika < 0):
	print("Taitaa olla virhe")
elif (ika > 0 and ika < 5):
	print("En usko, että osaat kirjoittaa...")
else:
	print(f"Ok, olet siis {ika}-vuotias")

# Tee ohjelma, joka kysyy käyttäjän nimeä. 
# Jos nimeksi syötetään Tupu, Hupu tai Lupu, 
# ohjelma tunnistaa käyttäjän Aku Ankan veljenpojaksi.
# Jos nimeksi annetaan Mortti tai Vertti, 
# ohjelma vastaavasti tunnistaa käyttäjän Mikki Hiiren veljenpojaksi.

nimi = input("Anna nimesi:") 
if (nimi == "Tupu" or nimi == "Hupu" or nimi == "Lupu"):
	print("Olet luultavasti Aku Ankan veljenpoika.")
elif (nimi == "Mortti" or nimi == "Vertti"):
	print("Olet luultavasti Mikki Hiiren veljenpoika.")
else:
	print("Et ole kenenkään tuntemani hahmon veljenpoika.")

# Alla oleva taulukko kuvaa erään kurssin arvosanan muodostumista. 
# Tee ohjelma, joka ilmoittaa kurssiarvosanan annetun taulukon mukaisesti.

# pistemäärä	arvosana
# < 0		mahdotonta!
# 0-49		hylätty
# 50-59		1
# 60-69		2
# 70-79		3
# 80-89		4
# 90-100	5
# > 100		mahdotonta!

grade = int(input("Anna pisteet [0-100]:"))
if (grade < 0 or grade > 100):
	print("Arvosana: mahdotonta!")
elif (grade >= 0 and grade <= 49):
	print("Arvosana: hylätty")
elif (grade >= 50 and grade <= 59):
	print("Arvosana: 1")
elif (grade >= 60 and grade <= 69):
	print("Arvosana: 2")
elif (grade >= 70 and grade <= 79):
	print("Arvosana: 3")
elif (grade >= 80 and grade <= 89):
	print("Arvosana: 4")
else:
	print("Arvosana: 5")

# Ohjelma kysyy käyttäjältä lukua. 
# Jos luku on jaollinen kolmella, tulostetaan Fizz. 
# Jos luku on jaollinen viidellä, tulostetaan Buzz. 
# Jos luku on jaollinen sekä kolmella, että viidellä, tulostetaan FizzBuzz

luku = int(input("Luku:"))
if (luku % 3 == 0 and luku % 5 != 0):
	print("Fizz")
elif (luku % 5 == 0 and luku % 3 != 0):
	print("Buzz")
elif (luku % 3 == 0 and luku % 5 == 0):
	print("FizzBuzz")

