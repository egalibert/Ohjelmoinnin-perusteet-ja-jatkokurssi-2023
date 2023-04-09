#Tee ohjelma, joka kysyy huomisen sääennusteen 
# ja suosittelee sen mukaista pukeutumista.

#Suositus vaihtelee sen mukaan, onko lämpötila yli 20 astetta, 
# yli 10 astetta vai yli 5 astetta. Myös sade vaikuttaa suositukseen.

print("Kerro huominen sääennuste:")
tila = int(input("Lämpötila:"))
sade = input("Sataako (kyllä/ei):")
print("Pue housut ja paita")
if (tila < 20):
	print("Ota myös pitkähihainen paita")
if (tila < 10):
	print("Pue päälle takki")
if (tila < 5):
	print("Kannattaa ottaa myös hanskat")
if (sade == "kyllä"):
	print("Muista sateenvarjo!")

#Kirjoita ohjelma, joka ratkaisee toisen asteen yhtälön ax²+bx+c. 
# Ohjelmalle annetaan arvot a, b ja c, ja sen tulee laskea juuret 
# (eli ratkaisut) kaavalla

from math import sqrt

a = float(input("Anna a:"))
b = float(input("Anna b:"))
c = float(input("Anna c:"))

diskriminantti = b ** 2  - 4 * a * c
if diskriminantti > 0:
	juuri1 = (-b +sqrt(diskriminantti))/(2*a)
	juuri2 = (-b - sqrt(diskriminantti))/(2*a)

	print("Juuri 1:", juuri1)
	print("Juuri 2:", juuri2)