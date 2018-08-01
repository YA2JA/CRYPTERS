import algorithms
while True:
	print("Quelle est le moyen de chiffrement voulez vous utiliser ?")
	print("1- Chiffrement par décalage", end = "		")
	print("2- Chiffrement taipex")
	print("3- Chiffrement affine", end = "			")
	print("4- Chiffrement  de Port")
	answer = input("")
	if answer == "1":
		algorithms.N1()
	elif answer=="2":
		algorithms.N2()
	elif answer=="3":
		algorithms.N3()
	elif answer=="4":
		algorithms.N4()
	else:
		print("Pardon, j'ai pas compris")
	input()
