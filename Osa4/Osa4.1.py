# Tee ohjelma, joka kysyy käyttäjältä, mikä editori on käytössä. 
# Ohjelma jatkaa, kunnes vastaus on Visual Studio Code.

# Seuraava käyttöesimerkki havainnollistaa ohjelman haluttua tulostusta:

while (True):
	sana = input("Editori:")
	sana = sana.lower()
	if (sana == "visual studio code"):
		print("loistava valinta!")
		break
	elif (sana == "word" or sana == "notepad"):
		print("surkea")
	else:
		print("ei ole hyvä")
