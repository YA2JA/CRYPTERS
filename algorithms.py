def N1():
	arr1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
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
			print("\nLe_resultat: "+str(msgd))
		else:
			print("Pardon, j'ai pas compris")


	except ValueError:
		print("Pardon, j'ai pas compris")
"""Le chifrement de César
"""
def N2():
	cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
	if cryptMode not in ['E','D']: 
		print("Pardon, j'ai pas compris"); raise SystemExit
	mainMessage = input("Text: ").upper() 

	rotors = (
	(10,24,14,12,23,2,7,15,24,2,7,5,22,6,2,1,22,12,6,9,7,2,11,23,14,2),
	(1,7,11,26,12,5,11,20,11,7,18,6,17,18,19,1,13,5,2,9,11,13,6,17,26,24),
	(9,1,21,6,4,19,25,6,17,10,26,1,23,6,1,17,19,17,25,21,3,21,17,1,18,20)
	)

	switch = {
	'H':'Z', 'S':'N', 'L':'M',
	'P':'Q', 'R':'W', 'X':'Y'
	}
	# e1
	def stageOne(mode, message):
		X,Y,Z = 2,0,1 # postion de rotors 
		x,y,z = 7,1,8 # parametre
		finalMessage = ""
		for symbol in message:
			rotor = rotors[X][x] + rotors[Y][y] + rotors[Z][z]
			if mode == 'E':
				if symbol in [chr(x) for x in range(65,91)]:
					finalMessage += chr((ord(symbol) - 13 + rotor)%26 + ord('A'))
				else: continue
			else: 
				finalMessage += chr((ord(symbol) - 13 - rotor)%26 + ord('A'))
			if x != 25: x += 1
			else:
				x = 0
				if y != 25: y += 1
				else:
					y = 0
					if z != 25: z += 1
					else: z = 0
		return finalMessage

	# e2
	def stageTwo(message):
		finalMessage = list(message)
		for symbol in range(len(finalMessage)):
			for key in switch:
				if finalMessage[symbol] == key:
					finalMessage[symbol] = switch[key]
				elif finalMessage[symbol] == switch[key]:
					finalMessage[symbol] = key
				else: pass
		return "".join(finalMessage)

	# mode
	def encryptDecrypt(mode, message):
		if mode == 'E': 
			message = stageOne(mode, message)
			message = stageTwo(message)
		else: 
			message = stageTwo(message)
			message = stageOne(mode, message)
		return message
	print("Le_resultat:",encryptDecrypt(cryptMode, mainMessage))
"""Chiffrement taipex ou le chiffrement de la machine de """

def N3():
	mod = 26
	print(end = "Les clé possible: ")
	for key in range(mod):
	    if (pow(int(key),2)*int(key))%mod == 1:
	        print(key, end = " ")
	print()
	cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
	if cryptMode not in ['E','D']:
	    print("Pardon, j'ai pas compris"); raise SystemExit
	startMessage = input("Text: ").upper()
	mainKey = input("La cle (en 2 chiffre) ").split()
	try: 
	    for number in mainKey: int(number)
	except ValueError: 
	    print("Entrée uniquement les chifres "); raise SystemExit
	if len(mainKey) != 2:
	    print("Entrée 2 chifres"); raise SystemExit
	if (pow(int(mainKey[0]),2)*int(mainKey[0]))%mod != 1: 
	    print("vous êtes tromper de chifre"); raise SystemExit
	def encryptDecrypt(mode, message, key, final = ""):
	    for symbol in message:
	            if mode == 'E': 
	                final += chr((int(key[0]) * ord(symbol) + int(key[1]) - 13)%mod + ord('A'))
	            else: 
	                final += chr(pow(int(key[0]),2) * ((ord(symbol) + mod - int(key[1]) - 13))%mod + ord('A'))
	    return final
	print("Le_resultat:",encryptDecrypt(cryptMode, startMessage, mainKey))

def N4():
	from re import findall
	ONE = 1

	stageOne = ['00'+str(x) for x in range(ONE,10)] # 001 - 009
	stageTwo = ['0'+str(x) for x in range(10,100)] # 010 - 099
	stageThree = [str(x) for x in range(100,676+ONE)] # 100 - 676

	keys = tuple(stageOne + stageTwo + stageThree)

	del stageOne, stageTwo, stageThree, ONE

	coordinateX = tuple([chr(alpha) for alpha in range(65,91)])
	coordinateY = tuple([chr(alpha) for alpha in range(65,91)])

	cryptKeys = {x:None for x in keys}

	counter = 0
	for x in coordinateX:
		for y in coordinateY:
			cryptKeys[keys[counter]] = x + y
			counter += 1

	del coordinateX, coordinateY, counter, keys

	cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
	if cryptMode not in ['E','D']:
		print("Pardon, j'ai pas compris")
		raise SystemExit
	startMessage = input("Text: ").upper()

	def regular(mode, text):
		if mode == 'E': template = r"[A-Z]{2}" # HELLOZ = HE LL OZ
		else: template = r"[0-9]{3}" # 187298390 = 187 298 390
		return findall(template, text)

	def encryptDecrypt(mode, message, final = ""):
		if mode == 'E':
			for symbol in message:
				if symbol not in [chr(x) for x in range(65,91)]: # A - Z
					message = message.replace(symbol,'')
			if len(message)%2 != 0: message += 'Z'
			for symbols in regular(mode, message):
				for key in cryptKeys:
					if symbols == cryptKeys[key]:
						final += key
		else:
			for number in regular(mode, message):
				if number in cryptKeys:
					final += cryptKeys[number]
		return final
	print("Le_resultat: ",encryptDecrypt(cryptMode, startMessage))