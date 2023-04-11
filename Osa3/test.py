# sana = input("Sana:")
# leveys = 30
# raamit = '*' * leveys
# keskikohta = leveys // 2
# sanan_keskipiste = len(sana) // 2

# #tulos = f"{raamit}\n*{sana.center(leveys -2 )} * \n{raamit}"
# #print(tulos)
# print(f"{raamit}")
# print("*" + " " * (keskikohta - sanan_keskipiste) + sana + " " * (keskikohta - sanan_keskipiste) + "*")
# print(f"{raamit}")


# Pyydetään käyttäjältä sana
# sana = input("Sana: ")

# # Lasketaan raamien leveys ja sanan keskikohta
# leveys = 30
# sanan_pituus = len(sana)
# keskikohta = leveys // 2
# sanan_keskipiste = sanan_pituus // 2
# vasen_sivu = keskikohta - sanan_pituus
# oikea_sivu = leveys - vasen_sivu - sanan_pituus -2

# # Tulostetaan tähtiraamit ja sana keskellä
# print("*" * leveys)
# print("*" + " " * vasen_sivu + sana + " " * oikea_sivu + "*")
# print("*" * leveys)

# def shakkilauta(i):
# 	y = i
# 	index = i
# 	tulos = ""
# 	tulos1 = ""
# 	while (index > 0):
# 		if (index % 2 == 1):
# 			tulos += "1"
# 		else:
# 			tulos += "0"
# 		index -= 1
# 	index = i
# 	while (index > 0):
# 		if (index % 2 == 1):
# 			tulos1 += "0"
# 		else:
# 			tulos1 += "1"
# 		index -= 1
# 	while (y > 0):
# 		if (y % 2 == 1):
# 			print(f"{tulos}")
# 		elif (y % 2 == 0):
# 			print(f"{tulos1}")
# 		y -= 1
			
# if __name__ == "__main__":
# 	shakkilauta(3)

# def nelio(jono, i):
	

# if __name__ == "__main__":
# 	nelio("ab", 3)
