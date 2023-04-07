# Seuraavassa ohjelmassa on useita syntaksivirheitä. Korjaa ohjelma siten, että syntaksi on kunnossa ja se toimii alla olevien esimerkkien mukaisesti.

#   luku = input("Anna luku: ")
#   if luku>100
#     print("Luku oli suurempi kuin sata")
#     luku - 100
#     print("Nyt luvun arvo on pienentynyt sadalla)
#      print("Arvo on nyt"+ luku)
#  print(luku + " taitaa olla onnenlukuni!")
#  print("Hyvää päivänjatkoa!)

luku = int(input("Anna luku: "))
if (luku > 100):
	print("Luku oli suurempi kuin sata")
	luku -= 100
	print("Nyt luvun arvo on pienentynyt sadalla")
	print(f"Arvo on nyt {luku}")
print(f"{luku} taitaa olla onnenlukuni!")
print("Hyvää päivänjatkoa!")

#Tee ohjelma, joka lukee käyttäjältä sanan ja 
# tulostaa sanan merkkien määrän, mikäli niitä on enemmän kuin yksi.

sana = input("Anna sana:")
pituus = len(sana)
if (pituus > 1):
	print(f"Sanassa {sana} on {pituus} kirjainta")
print("Kiitos!")

#Tee int-funktiota hyödyntäen ohjelma, 
# joka kysyy käyttäjältä desimaaliluvun ja 
# tulostaa erikseen luvun kokonaisosan ja desimaaliosan.

luku = float(input("Anna luku:"))
luku1 = int(luku)
luku2 = (luku - luku1)
print(f"Kokonaisosa {luku1}")
print(f"Desimaaliosa {luku2}")