#taipex le chiffrement de la machine Enigma
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