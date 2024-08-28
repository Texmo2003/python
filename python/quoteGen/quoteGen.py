import tkinter as tk
import os
import json
import random

# Create window
root = tk.Tk()

root.title("Quote Generator")

# Set windowsize
root.geometry("400x400")

# Create label for quote
quoteDisp = tk.Label(root, text="Her kommer det en quote")
quoteDisp.grid(row=0, column=0)

# Create label for author
authorDisp = tk.Label(root, text="her kommer forfatter")
authorDisp.grid(row=1, column=0)

# Get the directory of the script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Define quotes
quotes = []

# Read all quotes from file
with open(os.path.join(dir_path, "quotes.json"), "r") as file:
    quotes = json.load(file)

# Make quotes a list
quotes = quotes["quotes"]

# Function for new quote
def newQuote():
    randNmb = random.randint(0, len(quotes))
    newAuthor = quotes[randNmb]["author"]
    newQuotes = quotes[randNmb]["quote"]
    quoteDisp.config(text=("Quote: " + newQuotes))
    authorDisp.config(text=("Author: " + newAuthor))

# Create button for new quote
newBtn = tk.Button(root, text="New quote", command=newQuote)
newBtn.grid(row=1, column=1)

# Run window
root.mainloop()