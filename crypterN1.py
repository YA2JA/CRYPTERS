arr1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','.',',',' ',':','!', '?']

arr2=[]
for i in range(len(arr1)):
	arr2.append(arr1[i])

def change_arr2():
	for i in range(number):
		arr2.append(arr2[0])
		arr2.remove(arr2[0])

try:

	ans=input("[E]ncrypt|[D]ecrypt: ")

	if ans=="E":
		number=int(input("La clé de chiffrement [0-%s] : "%(str(len(arr1)))))

		change_arr2()

		msg=input("Text: ")

		msgc=""
		for i in msg:
			for j in range(len(arr1)):
				if i==arr1[j]:
					msgc+=arr2[j]
		print("\nLe_resultat: "+msgc+"\n")

	elif ans=="D":
		number=int(input("La clé de chiffrement [0-%s]: "%(str(len(arr1)))))

		change_arr2()

		msg=input("inseré le text: ")
		msgd=""
		for i in msg:
			for j in range(len(arr1)):
				if i==arr2[j]:
					msgd+=arr1[j]
		print("Dechiffre le text:")
		print("\nLe_resulta: "+str(msgd))
	else:
		print("Pardon, j'ai pas compris")


except ValueError:
	print("Pardon, j'ai pas compris")
