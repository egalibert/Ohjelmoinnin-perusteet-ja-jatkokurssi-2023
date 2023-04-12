# Tee ohjelma, joka alustaa listan jossa on arvot [1, 2, 3, 4, 5]. 
# Tämän jälkeen ohjelma kysyy käyttäjältä alkion indeksin ja uuden arvon, 
# vaihtaa kyseisen alkion arvon ja tulostaa listan uudelleen. 
# Ohjelman suoritus päättyy, jos käyttäjä antaa alkion indeksiksi -1.

lista = [1, 2, 3, 4, 5]
while (True):
	index = int(input("Anna indeksi:"))
	if (index == -1):
		break
	arvo = int (input("Anna arvo:"))
	lista[index] = arvo
	print(lista)

# Tee ohjelma, joka kysyy käyttäjältä ensin lukujen määrän. 
# Sen jälkeen ohjelma pyytää käyttäjää syöttämään annetun määrän lukuja 
# yksitellen ja lisää ne listaan samassa järjestyksessä.

# Lopuksi lista tulostetaan.

count = int(input("Kuinka monta lukua:"))
lista = []
index = 1
while (index <= count):
	luku = int(input(f"Anna luku {index}:"))
	lista.append(luku)
	index += 1
print(f"{lista}")

# Tee ohjelma, joka pyytää käyttäjää valitsemaan alkion lisäyksen tai poiston. 
# Sekä lisäys että poisto tehdään listan loppuun. 
# Lisättävän alkion arvo on aina yhtä suurempi kuin listan viimeinen alkio 
# (tai 1, jos listassa ei ole alkioita).

# Joka operaation välissä lista tulostetaan.

lista = []
index = 1
while (True):
	print(f"Lista on nyt {lista}")
	if (index == 0):
		index = 1
	valinta = input("(l)isää, (p)oista vai e(x)it:")
	if (valinta == 'x'):
		print("Moi!")
		break
	elif (valinta == 'l'):
		lista.append(index)
		index += 1
	elif (valinta == 'p'):
		pituus = len(lista)
		lista.pop(pituus - 1)
		index -= 1

# Tee ohjelma, joka kyselee käyttäjältä sanoja. 
# Kun käyttäjä syöttää jonkin sanan kahdesti, 
# ohjelma tulostaa eri sanojen määrän ja lopettaa toimintansa.

lista = []
while (True):
	sana = input("sana:")
	if (sana not in lista):
		lista.append(sana)
	else:
		break
print(f"Annoit {len(lista)} eri sanaa")

# Tee ohjelma, joka kysyy käyttäjältä lukuja ja lisää niitä listaan. 
# Lista tulostetaan jokaisen luvun lisäyksen jälkeen kahdella eri tavalla:

# alkiot lisäysjärjestyksessä ja
# järjestettynä pienimmästä suurimpaan alkioon
# Ohjelman suoritus päättyy, kun käyttäjä syöttää luvun 0.

lista = []
while (True):
	luku = int(input("Anna luku:"))
	if (luku == 0):
		print("Moi!")
		break
	lista.append(luku)
	print(f"Lista: {lista}")
	print(f"Järjestettynä: {sorted(lista)}")

# Tee funktio pituus, joka palauttaa parametrinaan saamansa listan pituuden.

def pituus(lista):
    return (len(lista))

if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = pituus(lista) 
    print(tulos)

# Tee funktio keskiarvo, joka palauttaa parametrinaan saamansa 
# kokonaislukuja sisältävän listan alkioiden keskiarvon.

def keskiarvo(lista):
    return(sum(lista) / len(lista))

if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = keskiarvo(lista) 
    print(tulos)

# Tee funktio vaihteluvali, joka palauttaa parametrinaan saamansa 
# kokonaislukuja sisältävän listan vaihteluvälin 
# (eli suurimman ja pienimmän alkion erotuksen).

def vaihteluvali(lista):
    return(max(lista) - min(lista))

if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = vaihteluvali(lista) 
    print(tulos)

