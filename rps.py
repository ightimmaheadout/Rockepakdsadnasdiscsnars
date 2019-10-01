# Verne Bauman
# Rock Paper Scissors
import random

pScore = 0
cScore = 0
Ties = 0
computerChoices = ["r", "p", "s"]
# Welcome Message
print("Welcome to Paper Scissors Rock")
pName = input("What beith ya name laddy? ")

def printScore():
	print("The score is: ")
	print(pName + ": " + str(pScore))
	print("Computer: " + str(cScore))
	print("Ties: " + str(Ties))

while True:
	printScore()
	pChoice = input("Enter R for (ROCK Solid), P for (PAPER Thin), S for (SHARP Scissors), or Q for (Quitter): ")
	if pChoice == "q":
		break
	cChoice = random.choice(computerChoices)
	if pChoice == "r":
		print(pName + " picked Rock")
		if cChoice == "r":
			print("Computer picked ROCK Solid")
			print("It's a tie dumb fk")
			ties = ties + 1
		elif cChoice == "p":
			print("Computer picked PAPER Thin")
			print("HAHA COMPUTER WON YOU USELESS MF")
			cScore = cScore + 1
		else:
			print("Computer picked SHARP Scissors")
			print("You won against a bot... so cool")
			pScore = pScore + 1
	elif pChoice == "p":
		print(pName + " picked Paper")
		if cChoice == "r":
			print("Computer picked ROCK Solid")
			print("You won against a bot... so cool")
			pScore = pScore + 1
		elif cChoice == "p":
			print("Computer picked PAPER Thin")
			print("It's a tie dumb fk")
			Ties = Ties + 1
		else:
			print("Computer picked SHARP Scissors")
			print("HAHA COMPUTER WON YOU USELESS MF")
			cScore = cScore + 1
	elif pChoice == "s":
		print(pName + " picked Scissors")
		if cChoice == "r":
			print("Computer picked ROCK Solid")
			print("HAHA COMPUTER WON YOU USELESS MF")
			cScore = cScore + 1
		elif cChoice == "p":
			print("Computer picked PAPER Thin")
			print("You won against a bot... so cool")
			pScore = pScore + 1
		else:
			print("Computer picked SHARP Scissors")
			print("It's a tie dumb fk")
			Ties = Ties + 1
# Game Loop