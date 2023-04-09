#Kirjoita ohjelma, joka kysyy käyttäjän nimeä ja tämän jälkeen
#tulostaa nimen kahteen kertaan peräkkäisille riveille.

nimi = input("Anna nimesi:")
print(nimi)
print(nimi)

print("\n")

#Kirjoita ohjelma,joka kysyy käyttäjän nimeä ja tämän jälkeen
#tulostaa nimen kaksi kertaa samalle riville siten,
#että rivin alussa lopussa sekä nimien välissä on huutomerkki.

nimi = input("Anna nimesi:")
print("!" + nimi + "!" + nimi + "!")

print("\n")

#Kirjoita ohjelma, joka kysyy käyttäjän nimeä ja osoitetta.
#Ohjelma tulostaa syötetyt tiedot.

nimi = input("Etunimi:")
nimi2 = input("Sukunimi:")
osoite = input("Katuosoite:")
info = input("Postinumero ja kaupunki:")
print(nimi + " " + nimi2)
print(osoite)
print(info)