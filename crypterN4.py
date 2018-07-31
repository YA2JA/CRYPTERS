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
print("Le_resulta: ",encryptDecrypt(cryptMode, startMessage))