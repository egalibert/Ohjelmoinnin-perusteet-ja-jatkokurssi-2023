# Tee ohjelma, joka kysyy käyttäjältä positiivisen kokonaisluvun. 
# Ohjelma tulostaa esimerkkitulostuksen mukaisesti kertolaskuja lukuun asti:

luku = int(input("Anna luku:"))
i = 1
j = 1

while i <= luku:
	j = 1
	while j <= luku:
		tulo = i * j
		print(f"{i} x {j} = {tulo}")
		if j == luku:
			break
		j += 1
	i += 1

# Tee ohjelma, joka kysyy käyttäjältä lauseen. Ohjelma tulostaa 
# jokaisen sanan ensimmäisen kirjaimen ruudulle omille riveilleen.

lause = input("Anna lause:")
pituus = len(lause)
index = 0

print(f"{lause[0]}")
while (index < pituus - 1):
	if (lause[index] == ' '):
		print(f"{lause[index + 1]}")
	index += 1

# Tee ohjelma, joka kysyy käyttäjältä kokonaisluvun. 
# Jos käyttäjä syöttää negatiivisen luvun tai nollan, 
# ohjelman suoritus päättyy. Muuten ohjelma tulostaa luvun kertoman.

# Kertoma lasketaan kertomalla keskenään luku ja kaikki 
# sitä pienemmät positiiviset kokonaisluvut. 
# Esim. luvun 5 kertoma on 1 * 2 * 3 * 4 * 5 = 120.


while (True):
	luku = int(input("Anna luku:"))
	index = luku
	summa = 1
	if (luku <= 0):
		print("Kiitos ja moi!")
		break
	else:
		while (index > 0):
			summa *= index
			index -= 1
	print(f"Luvun {luku} kertoma on {summa}")
