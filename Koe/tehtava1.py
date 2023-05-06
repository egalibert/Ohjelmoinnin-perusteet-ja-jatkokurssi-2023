# Kirjoita ohjelma, joka kysyy käyttäjältä merkkijonoja yksi kerrallaan. 
# Kun käyttäjä syöttää tyhjän merkkijonon, ohjelma tulostaa syötettyjen 
# merkkijonojen määrän sekä pisimmän merkkijonon pituuden ja yleisimmän merkin.

# Tee tehtävän 1 ratkaisu tänne

total = 0
pisin = 0
yleisin = ""
all = ""
tulos = 0

while (True):
	merkkijono = input("Anna merkkijono:")
	if (merkkijono == " "):
		for letter in all:
			if (all.count(letter) > tulos):
				tulos = all.count(letter)
				yleisin = letter
		break
	total += 1
	if (pisin < len(merkkijono)):
		pisin = len(merkkijono)
	all += merkkijono
	

print(f"Merkkijonoja yhteensä: {total}")
print(f"Pisimmän merkkijonon pituus: {pisin}")
print(f"Merkkijonojen yleisin merkki: {yleisin}")