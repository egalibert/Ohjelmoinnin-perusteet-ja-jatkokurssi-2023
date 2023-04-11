# Tee funktio viiva, joka saa kaksi parametria (leveys, merkkijono). 
# Funktio tulostaa ensimmäisen parametrin määrittämän pituisen viivan käyttäen 
# toisena parametrina olevan merkkijonon ensimmäistä merkkiä. 
# Jos parametrina oleva merkkijono on tyhjä, 
# tulostuu viiva tähtinä.

def viiva(i, merkki):
    if (merkki == ""):
        print(f"{i * '*'}")
    else:
        print(f"{i * merkki[0]}")

if __name__ == "__main__":
    viiva(5, "x")

# Tee funktio risulaatikko, joka piirtää risuaitamerkkiä käyttäen 
# parametrinsa korkuisen, kymmenen merkkiä leveän risulaatikon.

# Funktion tulee kutsua edellisen tehtävän funktiota viiva 
# kaiken tulostuksen tekemiseen! Kopioi edellisen tehtävän funktion koodi 
# tämän tehtävän funktion koodin yläpuolelle. Älä muuta funktiota mitenkaan!

def viiva(i, merkki):
    if (merkki == ""):
        print(f"{i * '*'}")
    else:
        print(f"{i * merkki[0]}")

def risulaatikko(korkeus):
    while (korkeus > 0):
        viiva(10, "#")
        korkeus -= 1

if __name__ == "__main__":
    risulaatikko(5)

# Tee funktio risunelio, joka piirtää risuaitamerkkiä käyttäen
# parametrinsa kokoisen risuneliön.

# Funktion tulee kutsua edellisen tehtävän funktiota viiva 
# kaiken tulostuksen tekemiseen! Kopioi edellisen tehtävän funktion koodi 
# tämän tehtävän funktion koodin yläpuolelle. Älä muuta funktiota mitenkaan!

def viiva(i, merkki):
    if (merkki == ""):
        print(f"{i * '*'}")
    else:
        print(f"{i * merkki[0]}")

def risunelio(koko):
    i = koko
    while (koko > 0):
        viiva(i, "#")
        koko -= 1

if __name__ == "__main__":
    risunelio(5)

# Tee funktio nelio, joka saa kaksi parametria. 
# Funktio tulostaa neliön jonka korkeuden ja leveyden kertoo 
# ensimmäinen parametri. Toinen parametri määrittelee mitä merkkiä käyttäen 
# neliö piirretään.

# Funktion tulee kutsua edellisen tehtävän funktiota viiva
# kaiken tulostuksen tekemiseen! Kopioi edellisen tehtävän funktion 
# koodi tämän tehtävän funktion koodin yläpuolelle. 
# Älä muuta funktiota mitenkaan!

def viiva(i, merkki):
    if (merkki == ""):
        print(f"{i * '*'}")
    else:
        print(f"{i * merkki[0]}")

def nelio(koko, merkki):
    i = koko
    while (koko > 0):
        viiva(i, merkki)
        koko -= 1

if __name__ == "__main__":
    nelio(5, "x")

# Tee funktio kolmio, joka piirtää risuaitamerkkiä käyttäen 
# parametrinsa korkuisen ja levyisen, risuaitakolmion.

def viiva(i, merkki):
    if (merkki == ""):
        print(f"{i * '*'}")
    else:
        print(f"{i * merkki[0]}")

def kolmio(koko):
    i = 1
    while (koko > 0):
        viiva(i, "#")
        koko -= 1
        i += 1

if __name__ == "__main__":
    kolmio(5)

# Tee funktio kuvio, joka saa neljä parametria. 
# Funktio tulostaa kuvion, jonka yläosana on kahden ensimmäisen parametrin 
# määrittelemä kolmio ja alaosana ensimmäisen ja kahden jälkimmäisen 
# parametrin määrittelemä suorakulmio.

def viiva(i, merkki):
    if (merkki == ""):
        print(f"{i * '*'}")
    else:
        print(f"{i * merkki[0]}")

def kuvio(i, kuvio1, y, kuvio2):
    index = 1
    while (i > 0):
        viiva(index, kuvio1)
        i -= 1
        index += 1
    index -= 1
    while (y > 0):
        viiva(index, kuvio2)
        y -= 1

if __name__ == "__main__":
    kuvio(5, "x", 2, "o")

# Tee funktio joulukuusi, joka saa yhden parametrin. 
# Funktio tulostaa tekstin joulukuusi! ja parametrinsa kokoisen joulukuusen.

def joulukuusi(koko):
    print("joulukuusi!")
    for i in range(1, koko+1):
        print(" "*(koko-i) + "*"*(2*i-1))
    print(" "*(koko-1) + "*")

if __name__ == "__main__":
    joulukuusi(5)

# Tee funktio  luvuista_suurin, joka saa parametriksi kolme kokonaislukua. 
# Funktio palauttaa return-lausetta käyttäen luvuista suurimman.


def luvuista_suurin(i, x, y):
    if (i >= x and i >= y):
        return i
    elif(x >= i and x >= y):
        return x
    elif (y >= x and y >= i):
        return y

if __name__ == "__main__":
    suurin = luvuista_suurin(5, 4, 8)
    print(suurin)

# Tee funktio samat, joka saa parametriksi merkkijonon ja 
# kaksi merkkijonon indeksejä kuvaavaa kokonaislukua. 
# Funktio palauttaa return-lausetta käyttäen tiedon (True tai False) siitä,
# ovatko merkkijonon parametreina olevien indeksien
# osoittamissa paikoissa olevat merkit samat. 
# Jos jompikumpi indekseistä ei osu merkkijonon sisälle, palauttaa metodi False.

def samat(merkkijono, x, y):
    pituus = len(merkkijono)
    if (pituus <= x or pituus <= y):
        return False
    if (merkkijono[x] == merkkijono[y]):
        return True
    else:
        return False

if __name__ == "__main__":
    print(samat("abc", 0, 3))

# Tee kolme funktiota: eka_sana, toka_sana ja vika_sana.
# Jokainen funktioista saa parametrikseen lauseen (eli merkkijonon).

# Funktiot palauttavat nimensä mukaisesti lauseen ensimmäisen, 
# toisen tai viimeisen sanan.

# Voit olettaa jokaisessa tapauksessa, että merkkijono koostuu vähintään 
# kahdesta sanasta, ja että sanojen välillä on aina täsmälleen yksi välilyönti, 
# ja että merkkijonon alussa ja lopussa ei ole välilyöntejä.

def eka_sana(merkkijono):
    index = 0
    sana = ""
    while (merkkijono[index] != " "):
        sana += merkkijono[index]
        index += 1
    return (sana)

def toka_sana(merkkijono):
    index = 0
    sana = ""
    pituus = len(merkkijono)
    while (merkkijono[index] != " "):
        index += 1
    index += 1
    while (merkkijono[index] != " "):
        sana += merkkijono[index]
        index += 1
        if (index == pituus):
            return (sana)
    return (sana)

def vika_sana(merkkijono):
    sana = ""
    pituus = len(merkkijono)
    index = pituus
    while (merkkijono[index - 1] != " "):
        index -= 1
    while (index < pituus):
        sana += merkkijono[index]
        index += 1
    return (sana)


if __name__ == "__main__":
    lause = "eka toka"
    print(eka_sana(lause))
    print(toka_sana(lause))
    print(vika_sana(lause))