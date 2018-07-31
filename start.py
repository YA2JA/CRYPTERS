print("Quelle est le moyen de chiffrement voulez vous utiliser ?")
print("1- Chiffrement par décalage", end = "		")
print("2- Chiffrement taipex")
print("3- Chiffrement affine", end = "			")
print("4- Chiffrement  de Port")
answer = input("")
if answer == "1":
	import crypterN2
elif answer=="2":
	import crypterN2
elif answer=="3":
	import crypterN3
elif answer=="4":
	import crypterN4
else:
	print("Pardon, j'ai pas compris")
input()
