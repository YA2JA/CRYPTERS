import algorithms
while True:
	print("Quelle est le moyen de chiffrement voulez vous utiliser ?")
	print("1- Chiffrement par décalage", end = "		")
	print("2- Chiffrement taipex")
	print("3- Chiffrement affine", end = "			")
	print("4- Chiffrement  de Port")
	answer = input("")
	try:
		eval("algorithms.N"+answer+"()")#Execute the function N1, N2, N3 or N4
		print("\n"*2,"_"*60)
	except:
		print("Pardon, j'ai pas compris","\n"*2, "_"*60)