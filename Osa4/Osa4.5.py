# Kirjoita funktio muotoile, joka saa parametrikseen liukulukuja 
# sisältävän listan. Funktio muodostaa listan perusteella uuden 
# merkkijonoja sisältävän listan, jossa jokainen liukulukulistan alkio 
# esitetään pyöristettynä kahden desimaalin tarkkuuteen. 
# Listan alkioiden järjestyksen tulee säilyä.

def muotoile(lista):
	return [f"{x:.2f}" for x in lista]

if __name__ == "__main__":
	lista = [1.234, 0.3333, 0.11111, 3.446]
	lista2 = muotoile(lista)
	print(lista2)

