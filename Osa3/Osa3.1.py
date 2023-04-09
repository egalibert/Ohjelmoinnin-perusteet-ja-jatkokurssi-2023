# Kirjoita ohjelma, joka tulostaa silmukassa luvut 
# kahdesta kolmeenkymmeneen kahden luvun välein. 
# Jokainen luku tulostetaan omalle rivilleen.

num = 0

while (num < 30):
    num += 2
    print(f"{num}")

# Korjaa tehtäväpohjassa oleva ohjelma

# print("Valmiina?")
# luku = int(input("Anna luku: "))
# while luku = 0:
# print(luku)
# print("Nyt!")

print("Valmiina?")
luku = int(input("Anna luku: "))
while (luku > 0):
    print(f"{luku}")
    luku -= 1
print("Nyt!")

# Tee ohjelma, joka tulostaa kaikki käyttäjän 
# antamaa lukua pienemmät luvut alkaen luvusta yksi.

luku = int(input("Mihin asti:"))
num = 1

while (luku > num):
    print(f"{num}")
    num += 1

# Tee ohjelma, joka tulostaa ensin luvun 1 ja
# sen jälkeen kerta toisensa jälkeen aina kaksi kertaa suuremman luvun. 
# Ohjelma siis tulostaa luvun kaksi potensseja.

# Ohjelman suoritus päättyy, kun on tulostettu luku, 
# joka on korkeintaan käyttäjän syötteen suuruinen. 
# Yhtään käyttäjän syötettä suurempaa lukua ei siis tulosteta!

luku = int(input("Mihin asti:"))
num = 1

while (luku >= num):
    print(f"{num}")
    num *= 2

# Muuta edellistä ohjelmaa siten, että käyttäjä saa määrätä kertoimen 
# (edellisessä ohjelmassa kerroin oli aina 2), eli sen,
# minkä luvun potensseja ohjelma tulostaa.

luku = int(input("Mihin asti:"))
kerroin = int(input("Mikä kerroin:"))
num = 1
while (luku >= num):
    print(f"{num}")
    num *= kerroin

# Tee ohjelma, joka laskee peräkkäisten lukujen summaa 1 + 2 + 3 + ... 
# kunnes sen arvo on vähintään käyttäjän syöttämä luku.

luku = int(input("Mihin asti:"))
num = 1
summa = 0
while (summa < luku):
    summa += num
    num += 1
print(f"{summa}")

