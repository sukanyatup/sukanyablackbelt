from random import randint
if __name__ == '__main__':
	randomGuess = randint(1, 10)
	#print(randomGuess)
	while(True):
		inputNumber = input("Guess the number: ")
		if (int(inputNumber)==int(randomGuess)):
			print("Correct!")
			break
		else:
			print("Wrong, try again!")
