# Import GUI
import tkinter as tk

value1 = 0
value2 = 0
value3 = 0

# Create window
root = tk.Tk()

# Set windowsize
root.geometry("400x400")

# Create label
label = tk.Label(root, text="hei")
label.grid(row=0, column=1, sticky="w")

# Create label
numberField = tk.Label(root, text="")

def putNmb():
    print("hei")

# Create 10 buttons
for i in range(10):
    number = tk.Button(root, text=i, command=putNmb)


# Open window
root.mainloop()