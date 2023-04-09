# Kirjoita edellä olevaa toistolause-esimerkkiä mukaillen ohjelma, 
# joka tulostaa viestin "moi" ja kysyy käyttäjältä "Jatketaanko?" 
# kunnes käyttäjä syöttää merkkijonon "ei". 
# Tämän jälkeen tulostetaan merkkijono "ei sitten" ja suoritus päättyy.

while (True):
	print("moi")
	sana = input("Jatketaanko?")
	if (sana == "ei"):
		break
print("ei sitten")

# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja. 
# Mikäli luku on negatiivinen (eli pienempi kuin nolla), 
# käyttäjälle tulostetaan viesti "Epäkelpo luku" ja 
# käyttäjältä kysytään uutta lukua. 
# Jos taas luku on nolla, lukujen lukeminen lopetetaan 
# ja ohjelma poistuu toistolauseesta.

from math import sqrt

while (True):
	luku = int(input("Syötä luku:"))
	if (luku < 0):
		print("Epäkelpo luku")
	elif (luku == 0):
		break
	else:
		print(f"{sqrt(luku)}")
print("Lopetetaan...")

# Korjaa ohjelmassa oleva ongelma.

# luku = 5
# print("Lähtölaskenta!")
# while True:
#   print(luku)
#   luku = luku - 1
#   if luku > 0:
#     break

# print("Nyt!")

luku = 5
print("Lähtölaskenta!")
while True:
	print(luku)
	luku = luku - 1
	if luku == 0:
		break

print("Nyt!")

# Tee ohjelma, joka kysyy käyttäjältä salasanaa ja 
# tämän jälkeen pyytää toistamaan salasanan niin kauan, 
# kunnes käyttäjä syöttää ensimmäisenä annetun salasanan uudelleen.

salasana = input("Salasana:")
while (True):
	salasana1 = input("Toista salasana:")
	if (salasana != salasana1):
		print("Ei ollut sama!")
	else:
		break
print("Käyttäjätunnus luotu!")

