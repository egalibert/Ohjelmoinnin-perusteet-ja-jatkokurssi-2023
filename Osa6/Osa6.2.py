# Tee ohjelma, joka kysyy nimeä ja luo "omistuskirjoituksen" 
# käyttäjän haluamaan tiedostoon. Seuraavassa ohjelman esimerkkisuoritus:

kuka = input("Kenelle teos omistetaan:")
minne = input("Mihin kirjoitetaan:")

with open(minne, "w") as tiedosto:
	tiedosto.write(f"Hei {kuka}, toivomme \
viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")