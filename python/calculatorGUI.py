# Import GUI
import tkinter as tk

value1 = 0
value2 = 0
value3 = None

operation = "+"

operations = ["/", "*", "-", "+"]

# Create window
root = tk.Tk()

# Set windowsize
root.geometry("200x150")

# Create label
label = tk.Label(root, text="")
label.grid(row=0, column=1, sticky="w")

# Create label
numberField = tk.Label(root, text="")

# Function to calculate
def calculate(v1, v2):
    if operation == "+":
        result = v1 + v2
    elif operation == "-":
        result = v1 - v2
    elif operation == "*":
        result = v1 * v2
    elif operation == "/":
        result = v1 / v2
    return(result)

# Function to put the number you click in label
def putNmb(nmb):
    global value3
    if value3 != None:
        label.config(text="")
        value3 = None
    label.config(text=label.cget("text") + str(nmb))

# Function to choose operand
def chooseOperand(op):
    if label.cget("text") != "":
        global value1, value2, operation
        value2 = int(label.cget("text"))
        value1 = calculate(value1, value2)
        operation = op
        label.config(text="")

# Function equal
def equal():
    if label.cget("text") != "":
        global value1, value2, value3
        value2 = int(label.cget("text"))
        value3 = calculate(value1, value2)
    else:
        value3 = value1
    value1, value2 = 0, 0
    label.config(text=str(value3))

# Function for restarting calculator
def delete():
    global value1, value2, value3, operation
    value1, value2, value3 = 0, 0, 0
    operation = "+"
    label.config(text="")


# Create 10 buttons
for i in range(10):
    number = tk.Button(root, text=9-i, command=lambda i=9-i: putNmb(i))
    number.grid(row=(int(i/3)+1), column=(i%3))

# Create operations buttons
for i in range(len(operations)):
    print(i)
    operand = tk.Button(root, text=operations[i], command=lambda i=operations[i]: chooseOperand(i))
    operand.grid(row=i+1, column=3)

# Create equal button
equalBtn = tk.Button(root, text="=", command=equal)
equalBtn.grid(row=4, column=2)

# Create delete button
deleteBtn = tk.Button(root, text="AC", command=delete)
deleteBtn.grid(row=4, column=1)

# Open window
root.mainloop()