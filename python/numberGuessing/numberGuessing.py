import tkinter as tk
import random

# Create window
root = tk.Tk()

root.title("Guess a number between 0 and 1000")

# Set windowsize
root.geometry("400x400")

# Create answer
correctNmb = -1

# Create guess
guess = -1

# Create a list of all guesses
guessList = []

# Create variables for range
lower = 0
higher = 1000

# Create label for range
rangeLabel = tk.Label(root, text=(str(lower) + " - " + str(higher)))
rangeLabel.grid(row=2, column=2)

# Create answer input
answerInput = tk.Entry(root)
answerInput.grid(row=0, column=0)

# Create update label
updateLabel = tk.Label(root, text="")
updateLabel.grid(row=1, column=0)

# Create label for amount of guesses
guessesLabel = tk.Label(root, text="")
guessesLabel.grid(row=0, column=2)

#Function to update higher range
def updateHigher():
    global guess, higher
    if guess < higher:
        higher = guess

#Function to update lower range
def updateLower():
    global guess, lower
    if guess > lower:
        lower = guess

# Function for guessing number
def guessNumber():
    global amtGuesses, guessList, guess, lower, higher
    guess = int(answerInput.get())
    guessDic = {}
    if guess == correctNmb:
        updateLabel.config(text="Correct!")
        guessBtn.config(text="New game", command=newGame)
        answerInput.delete(0, tk.END)
        answerInput.config(state='disable')
        guessDic = {
            "guess":guess,
            "result":"Correct"
        }
    elif guess > correctNmb:
        updateLabel.config(text="Lower!")
        answerInput.delete(0, tk.END)
        guessDic = {
            "guess":guess,
            "result":"Lower!"
        }
        updateHigher()
    else:
        updateLabel.config(text="higher")
        answerInput.delete(0, tk.END)
        guessDic = {
            "guess":guess,
            "result":"Higher!"
        }
        updateLower()
    rangeLabel.config(text=(str(lower) + " - " + str(higher)))
    guessesLabel.config(text=("Guesses used: " + str(len(guessList))))
    guessList.append(guessDic)
    guessList = sorted(guessList, key=lambda k: k['guess'])
    for i in range(len(guessList)):
        label = tk.Label(root, text=("Guessed: " + str(guessList[i]['guess']) + " " + guessList[i]['result']))
        label.grid(row=(i + 2), column=0)

# Function for new game
def newGame():
    global correctNmb, amtGuesses
    amtGuesses = 0
    correctNmb = random.randint(0, 1000)
    updateLabel.config(text="")
    guessBtn.config(text="guess number", command=guessNumber)
    guessBtn.config(state='normal')

# Create guess button
guessBtn = tk.Button(root, text="guess number", command=guessNumber)
guessBtn.grid(row=1, column=2)

# Start game
newGame()

# Run window
root.mainloop()