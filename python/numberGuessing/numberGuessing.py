import tkinter as tk
import random

# Create window
root = tk.Tk()

# Set windowsize
root.geometry("400x400")

# Create answer
correctNmb = -1

# Create a list of all guesses
guessList = []

# Create answer input
answerInput = tk.Entry(root)
answerInput.grid(row=0, column=0)

# Create update label
updateLabel = tk.Label(root, text="")
updateLabel.grid(row=1, column=0)

# Create label for amount of guesses
guessesLabel = tk.Label(root, text="")
guessesLabel.grid(row=0, column=2)

# Function for guessing number
def guessNumber():
    global amtGuesses
    guess = int(answerInput.get())
    guessList.append(guess)
    guessList.sort()
    guessesLabel.config(text=("Guesses used: " + str(len(guessList))))
    label = tk.Label(root, text=("Guessed: " + str(guess)))
    label.grid(row=(len(guessList) + 2), column=0)
    if guess == correctNmb:
        updateLabel.config(text="Correct!")
        guessBtn.config(text="New game", command=newGame)
        answerInput.delete(0, tk.END)
        answerInput.config(state='disable')
    elif guess > correctNmb:
        updateLabel.config(text="Lower!")
        answerInput.delete(0, tk.END)
    else:
        updateLabel.config(text="higher")
        answerInput.delete(0, tk.END)

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