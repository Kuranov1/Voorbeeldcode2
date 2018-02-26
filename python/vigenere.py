def returnStart():
	print()
	print("Wil je nog een bericht versleutelen of ontcijferen?")
	print("Typ 'ja' of 'nee'.")
	return input().lower().startswith('j')

def startGame():
	# Vraag gebruiker of hij wilt versleutelen of ontcijferen
	print("Wil je een bericht versleutelen of ontcijferen?")
	print("Typ '1' om een bericht te versleutelen, of typ '2' om iets te ontcijferen.")
	print()

	userChoice = input()
	print()

	# Een table om alle versleutelde tekst in te bewaren
	encryptedTextList = []

	# Een table om alle ontcijferde tekst in te bewaren
	decryptedTextList = []

	if userChoice == "1":
		# Vraag gebruiker naar een bericht
		print("Voer een bericht in om te versleutelen:")
		message = input()

		print()

		# Vraag gebruiker naar een sleutel
		print("Voer een sleutel in voor je bericht:")
		key = input()

		# Maak een range aan met de lengte van het bericht
		ran = range(len(message))

		# Iterate door de range en verander zo alle letters
		for i in ran:
			# Pak de meest nieuwe letter van deze iteration
			currentLetter = message[i]
			currentKeyLetter = key[i % len(key)]

			# Pak de bijbehorende nummers
			numberLetter = ord(currentLetter)
			numberKeyLetter = ord(currentKeyLetter)

			# Voeg twee letter nummers samen
			sumOfTwoLetters = numberLetter + numberKeyLetter

			# Pak de nummer van de versleutelde letter
			newNumberLetter = sumOfTwoLetters % 128

			# Pak de versleutelde letter via zijn nummer
			newLetter = chr(newNumberLetter)

			encryptedTextList.append(newLetter)

			# Print de methode uit
			print()
			printText = currentLetter + "(" + str(numberLetter) + ") + "
			printText += currentKeyLetter + "(" + str(numberKeyLetter) + ") % "
			printText += str(128) + " = "
			printText += newLetter + "(" + str(newNumberLetter) + ")"
			print(printText)

		# Print het resultaat uit
		print()
		print("De versleutelde tekst is: " + ''.join(encryptedTextList))

	if userChoice == "2":
		# Vraag gebruiker om versleuteld bericht
		print("Voer het versleuteld bericht in:")
		encryptedMessage = input()

		print()

		# Vraag gebruiker om sleutel in te voeren
		print("Voer de sleutel in:")
		key = input()

		# Maak een range aan met de lengte van het versleuteld bericht
		ran = range(len(encryptedMessage))

		# Iterate door de range en verander zo alle letters
		for i in ran:
			# Pak de nieuwste letter van deze iteration
			currentEncryptedLetter = encryptedMessage[i]
			currentKeyLetter = key[i % len(key)]

			# Pak de bijbehorende nummers van de versleutelde letters
			numberEncryptedLetter = ord(currentEncryptedLetter)
			numberKeyLetter = ord(currentKeyLetter)

			# Ontcijfer de versleutelde letter met de sleutel
			decryptedLetterNumber = (numberEncryptedLetter + 128) - numberKeyLetter

			# Pak het ontcijferde letter via zijn nummer
			decryptedLetter = chr(decryptedLetterNumber)

			decryptedTextList.append(decryptedLetter)
			
		# Print het ontcijferde tekst
		print()
		print("Het ontcijferde tekst is: " + ''.join(decryptedTextList))

	if returnStart():
		print()
		startGame()

startGame()