#Koodin pitäisi tuottaa täsmälleen seuraavanlainen tulostus:

#Esimerkkitulostus
#nimeni on Teppo Testaaja, olen 20-vuotias

#taitoihini kuuluvat
# - python (aloittelija)
# - java (veteraani)
# - ohjelmointi (puoliammattilainen)

#haen työtä, josta maksetaan palkkaa 2000-3000 euroa kuussa

nimi = "Teppo Testaaja"
ika = 20
taito1 = "python"
taso1 = "aloittelija"
taito2 = "java"
taso2 = "veteraani"
taito3 = "ohjelmointi"
taso3 = "puoliammattilainen"
ala = 2000
yla = 3000

print(f"nimeni on {nimi}, olen {ika}-vuotias\n")
print("taitoihini kuuluvat")
print(f"- {taito1} ({taso1})")
print(f"- {taito2} ({taso2})")
print(f"- {taito3} ({taso3})")
print(f"haen työtä, josta maksetaan palkkaa {ala}-{yla} euroa kuussa")

print("\n")

x = 27
y = 15
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")

print("\n")

#Korjaa ohjelma niin, että koko lasku tuloksineen tulostetaan yhdelle
# riville muuttamatta kuitenkaan print-komentojen määrää:

print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4)