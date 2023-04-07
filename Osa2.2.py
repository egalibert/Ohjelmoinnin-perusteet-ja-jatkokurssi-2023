#Tee ohjelma, joka kysyy käyttäjän ikää ja kertoo, 
# onko tämä täysi-ikäinen (eli 18-vuotias tai vanhempi).

ika = int(input("Kuinka vanha olet?"))
if (ika < 18):
	print("Et ole täysi-ikäinen!")
else:
	print("Olet täysi-ikäinen!")

#Tee ohjelma, joka kysyy käyttäjältä kaksi kokonaislukua 
# ja tulostaa niistä suuremman. 
# Jos luvut ovat yhtä suuret, ohjelma huomaa myös tämän.

ensi = int(input("Anna ensimmäinen luku:"))
toine = int(input("Anna toinen luku:"))
if (ensi > toine):
	print(f"Suurempi luku: {ensi}")
elif (toine > ensi):
	print(f"Suurempi luku: {toine}")
else:
	print("Luvut ovat yhtä suuret!")

# Tee ohjelma, joka kysyy kahden henkilön nimen 
# ja iän ja tulostaa vanhemman henkilön nimen.

print("Henkilö 1:")
nimi1 = input("Nimi:")
ika1 = int(input("Ikä:"))
print("Henkilö 2:")
nimi2 = input("Nimi:")
ika2 = int(input("Ikä:"))
if (ika1 > ika2):
	print(f"{nimi1} on vanhempi")
elif (ika2 > ika1):
	print(f"{nimi2} on vanhempi")
else:
	print(f"{nimi1} ja {nimi2} ovat yhtä vanhoja")

#Tee ohjelma, joka kysyy käyttäjältä kahta sanaa. 
# Ohjelma tulostaa sanoista sen, joka on aakkosjärjestyksessä jälkimmäinen.

sana1 = input("Anna 1. sana:")
sana2 = input("Anna 2. sana:")
if (sana1 > sana2):
	print(f"{sana1} on aakkosjärjestyksessä viimeinen.")
elif (sana2 > sana1):
	print(f"{sana2} on aakkosjärjestyksessä viimeinen.")
else:
	print("Annoit saman sanan kahdesti.")

a = int(input("luku:"))
if a < 4:
   print("eka")
elif a < 3:
   print("toka")
else:
   print("kolmas")