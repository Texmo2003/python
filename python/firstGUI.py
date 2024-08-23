# Import tkinter for GUI
import tkinter as tk

# Create a window
root = tk.Tk()

# Set window title
root.title("First GUI")

# Set window size
root.geometry("450x100")

# Create Entry field
entry = tk.Entry(root)

# Create drop down menu
options = ["+", "-", "*", "/"]
variable = tk.StringVar(root)
variable.set(options[0])
drop_down = tk.OptionMenu(root, variable, *options)
drop_down.grid(row=0, column=1, sticky="w")

# Place entry field in window
entry.grid(row=0, column=0, sticky="w")

# Create Entry field
entry2 = tk.Entry(root)

# Place entry field in window
entry2.grid(row=0, column=2, sticky="w")

# Create a label
label = tk.Label(root, text="Result: ")
label.grid(row=2, column=0, columnspan=3, sticky="ew")

# Calculate function
def calculate():
    num1 = int(entry.get())
    num2 = int(entry2.get())
    operation = variable.get()
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    label.config(text="Result: " + str(result))

# Create a button
button = tk.Button(root, text="Calculate", command=calculate)
button.grid(row=1, column=0, columnspan=3, sticky="ew")

# Open window
root.mainloop()