#Tee ohjelma, joka kysyy käyttäjältä kokonaisluvun ja
#tulostaa merkkijonon "Orwell" jos luku on täsmälleen 1984.
#Muussa tapauksessa ohjelma ei tulosta mitään.

luku = int(input("Anna luku:"))
if (luku ==  1984):
	print("Orwell")

#Kirjoita ohjelma, joka lukee käyttäjältä kokonaisluvun. 
#Mikäli luku on pienempi kuin 0, ohjelma tulostaa luvun kerrottuna luvulla -1. 
#Muulloin ohjelma tulostaa käyttäjän syöttämän luvun. 
#Alla on muutamia esimerkkejä ohjelman odotetusta toiminnasta.

luku = int(input("Anna luku:"))
if (luku < 0):
	luku *= -1
print(f"Luvun itseisarvo on {luku}")

# Kirjoita ohjelma, joka kysyy ensin käyttäjän nimen. 
# Jos nimi on mikä tahansa muu kuin "Jerry", ohjelma kysyy keittoannosten
# lukumäärän ja kertoo sitten kokonaishinnan. Yksi annos maksaa 5,90.

nimi = input("Mikä on nimesi:")
if (nimi != "Jerry"):
	annos = int(input("Kuinka monta anoosta keittoa:"))
	kokonaishinta = annos * 5.90
	print(f"Kokonaishinta on {kokonaishinta}")
print("Seuraava!")

#Tee ohjelma, joka lukee käyttäjältä kokonaisluvun 
# ja kertoo sitten sen suuruusluokan oheisten esimerkkisuoritusten mukaisesti:

luku = int(input("Anna luku:"))
if (luku < 1000):
	print("Luku on pienempi kuin 1000")
if (luku < 100):
	print("Luku on pienempi kuin 100")
if (luku < 10):
	print("Luku on pienempi kuin 10")
print("Kiitos!")

#Tee ohjelma, joka kysyy käyttäjältä ensin kaksi lukua ja sen jälkeen komennon. 
# Jos komento on joko summa, tulo tai erotus, 
# ohjelma laskee syötteille kyseisen operaation tuloksen. 
# Muussa tapauksessa ohjelma ei tulosta mitään.

luku1 = int(input("Luku 1:"))
luku2 = int(input("Luku 2:"))
komento = input("Komento:")
if (komento == "summa"):
	print(f"{luku1} + {luku2} = {luku1 + luku2}")
if (komento == "erotus"):
	print(f"{luku1} - {luku2} = {luku1 - luku2}")
if (komento == "tulo"):
	print(f"{luku1} * {luku2} = {luku1 * luku2}")

#Tee ohjelma, joka kysyy käyttäjältä lämpötilan fahrenheit-asteina, 
# ja tulostaa sitten lämpötilan celsius-asteina. 
# Jos lämpötila celsius-asteina on pienempi kuin 0, 
# ohjelma tulostaa lisäksi viestin "Paleltaa!".

tila = int(input("Anna lämpötila (F):"))
celsius = tila - 32 // 1.8
print(f"{tila} fahrenheit-astetta on {celsius} celsius-astetta")
if (celsius < 0):
	print("Paleltaa!")

#Tee ohjelma, joka kysyy tuntipalkkaa, 
# työskenneltyjen tuntien määrää ja viikonpäivää.
# Ohjelma tulostaa palkan, joka on tuntipalkka kertaa tuntien määrä 
# muina päivinä paitsi sunnuntaisin, jolloin tuntipalkka on kaksinkertainen.

t_palkka = float(input("Tuntipalkka:"))
t_tunnit = int(input("Työtunnit:"))
paiva = input("Viikonpäivä:")
if (paiva == "sunnuntai"):
	t_palkka *= 2
print(f"Palkka {t_palkka * t_tunnit} euroa")

#Ohjelmassa lasketaan bonuskortin saldoon vuoden lopussa lisättävä
# bonuspistemäärä seuraavan kaavan mukaisesti:

pisteet = int(input("Kuinka paljon pisteitä? "))
bonuspisteet = pisteet
if pisteet < 100:
	bonuspisteet *= 1.1
	print("Sait 10 % bonusta")

if pisteet >= 100:
	bonuspisteet *= 1.15
	print("Sait 15 % bonusta")

print("Pisteitä on nyt", bonuspisteet)
