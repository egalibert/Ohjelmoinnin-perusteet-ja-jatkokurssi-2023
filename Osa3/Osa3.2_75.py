# Tee ohjelma, joka kysyy käyttäjältä merkkijonoa ja yksittäistä merkkiä. 
# Ohjelma tulostaa merkkijonosta löytyvän ensimmäisen kolmen merkin
# pituisen osajonon, jonka alkukirjain on käyttäjän syöttämä merkki.
# Voit olettaa, että merkkijono on vähintään kolmen merkin pituinen

sana = input("Sana:")
merkki = input("Merkki:")
kohta = sana.find(merkki)
if (kohta >= 0):
	print(f"{sana[kohta]}{sana[kohta + 1]}{sana[kohta + 2]}")

# two excresices left