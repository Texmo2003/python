import random

# Function for dice sim
def diceSim():
    rollAgain = True
    amtSideDice = int(input("How many sides will there be on your dice? "))
    print("Okey")
    amtDice = int(input("How many dice would you like to roll? "))
    while rollAgain:
        for i in range(amtDice):
            randDice = random.randint(1, amtSideDice)
            print("Dice " + str(i+1) + ": " + str(randDice))
        again = (input("Would you like to roll again?(Y/N)")).lower()
        if again == "n":
            rollAgain = False

diceSim()