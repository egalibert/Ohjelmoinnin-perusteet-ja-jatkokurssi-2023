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

# Tee ohjelma, joka tulostaa luvut 1:stä käyttäjän antamaan lukuun. 
# Luvut on kuitenkin käännetty pareittain ympäri.

luku = int(input("Anna luku:"))
i = 1
toinen_luku = 2
while i <= luku:
	if (toinen_luku > luku):
		print(f"{i}")
	else:
		print(f"{toinen_luku}")
		print(f"{i}")
		toinen_luku += 2
	i += 2

# Tee ohjelma, joka kysyy käyttäjältä luvun ja 
# tulostaa sitten lukuja vuorotellen seuraavien esimerkkien mukaisesti.

luku = int(input("Anna luku:"))
i = 1
toinen_luku = luku
index = 0
printed = 0
while (True):
	if (printed != luku):
		print(f"{i + index}")
		printed += 1
	if (printed != luku):
		print(f"{toinen_luku - index}")
		printed += 1
	index += 1
	if (printed == luku):
		break

# Osajonojen haku

sana = input("Sana:")
merkki = input("Merkki:")

for i in range(len(sana) - 2):
    osajono = sana[i:i+3]
    if osajono[0] == merkki:
        print(osajono)

# Toinen esiintymä

sana = input("Sana:")
merkki = input("Merkki:")

jono = input("Anna merkkijono:")
merkki = input("Anna osajono:")

eka = jono.find(merkki)
toka = jono.find(merkki, eka + 1)

if toka == -1:
	print("Osajonoa ei löytynyt toista kertaa.")
else:
	print(f"Osajonon toinen esiintymä on kohdassa {toka}.")