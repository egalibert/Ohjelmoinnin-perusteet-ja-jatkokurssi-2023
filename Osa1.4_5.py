#Tee ohjelma, joka arvioi käyttäjän keskimääräisiä ruokailukustannuksia.

#Ohjelma kysyy, kuinka monta kertaa viikossa käyttäjä käy Unicafessa ja
#Unicafe-lounaan hinnan sekä viikon muiden ruokaostosten hinnan.

#Näiden tietojen perusteella ohjelma laskee käyttäjän keskimääräiset ruokamenot
#sekä viikossa että yhtenä päivänä.

kerta = int(input("Montako kertaa viikossa syöt Unicafessa?"))
l_hinta = float(input("Unicafe-lounaan hinta?"))
r_hinta = float(input("Paljonko käytät viikossa ruokaostoksiin?"))

viikko_h = kerta * l_hinta + r_hinta
päivä_h = viikko_h / 7
print("Kustannukset keskimäärin:")
print(f"Päivässä {päivä_h} euroa")
print(f"Viikossa {viikko_h} euroa")

#Tee ohjelma, joka kysyy kurssin opiskelijoiden määrän
#ja ryhmän koon ja ilmoittaa, montako ryhmää opiskelijoista muodostuu.
#Jos jako ei mene tasan, yhdessä ryhmässä voi olla vähemmän opiskelijoita,
#mutta kaikissa muissa on oltava haluttu määrä.

monta = int(input("Montako opiskelijaa?"))
ryhmä = int(input("Mikä on ryhmän koko?"))
optimi = monta // ryhmä
jakoj = monta % ryhmä
if (jakoj != 0):
	optimi += 1
print(f"Ryhmien määrä: {optimi}")
