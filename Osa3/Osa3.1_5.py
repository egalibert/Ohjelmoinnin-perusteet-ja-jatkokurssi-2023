# Tee edellisestä ohjelmasta hieman kehittyneempi versio, 
# joka tulostaa lopputuloksen lisäksi myös sen miten kyseinen summa lasketaan:

luku = int(input("Mihin asti:"))
num = 1
summa = 0
summa1 = "Laskettiin"
while (summa < luku):
    summa += num
    summa1 += f" {num}"
    if (summa < luku):
        summa1 += " +"
    num += 1
print(f"{summa1} = {summa}")

##############

a = 2       
while a < 6:
   print(a) 
   a = a + 2