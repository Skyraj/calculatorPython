import tkinter as tk

root = tk.Tk()
root.title("Calculator")

output = tk.Entry(root, width=60, bd=5)
output.grid(row=0, columnspan=4)

expression = "" # works but should avoid global variable use

def buttonClick(digit):
    output.insert("end", digit) # inserts digit at the end of the string in Entry widget

def buttonClick_neg():
    output.insert(0, "-")

def buttonClick_clear():
    output.delete(0, "end")

def buttonClick_root():
    global expression
    expression = output.get()
    output.delete(0, "end")
    output.insert(0, int(expression) ** 0.5)

def buttonClick_operation(oper):
    global expression
    expression = output.get() + oper
    output.delete(0, "end")

def buttonClick_equal():
    global expression
    expression += output.get()
    expression = expression.split()
    #print(expression)

    if "+" in expression:
        output.delete(0, "end")
        output.insert(0, int(expression[0]) + int(expression[2]))
    elif "-" in expression:
        output.delete(0, "end")
        output.insert(0, int(expression[0]) - int(expression[2]))
    elif "*" in expression:
        output.delete(0, "end")
        output.insert(0, int(expression[0]) * int(expression[2]))
    elif "/" in expression:
        output.delete(0, "end")
        output.insert(0, int(expression[0]) / int(expression[2]))
    elif "%" in expression:
        output.delete(0, "end")
        output.insert(0, int(expression[0]) % int(expression[2]))
    elif "**" in expression:
        output.delete(0, "end")
        output.insert(0, int(expression[0]) ** int(expression[2]))


button_9 = tk.Button(root, text="9", padx=40, pady=40, command=lambda: buttonClick(9))
button_8 = tk.Button(root, text="8", padx=40, pady=40, command=lambda: buttonClick(8))
button_7 = tk.Button(root, text="7", padx=40, pady=40, command=lambda: buttonClick(7))
button_6 = tk.Button(root, text="6", padx=40, pady=40, command=lambda: buttonClick(6))
button_5 = tk.Button(root, text="5", padx=40, pady=40, command=lambda: buttonClick(5))
button_4 = tk.Button(root, text="4", padx=40, pady=40, command=lambda: buttonClick(4))
button_3 = tk.Button(root, text="3", padx=40, pady=40, command=lambda: buttonClick(3))
button_2 = tk.Button(root, text="2", padx=40, pady=40, command=lambda: buttonClick(2))
button_1 = tk.Button(root, text="1", padx=40, pady=40, command=lambda: buttonClick(1))
button_0 = tk.Button(root, text="0", padx=40, pady=40, command=lambda: buttonClick(0))

button_clear = tk.Button(root, text="AC", padx=36, pady=40, command=lambda: buttonClick_clear())
button_exp = tk.Button(root, text="x**y", padx=32, pady=40, command=lambda: buttonClick_operation(" ** "))
button_root = tk.Button(root, text="x**1/2", padx=26, pady=40, command=lambda: buttonClick_root())
button_mod = tk.Button(root, text="%", padx=38, pady=40, command=lambda: buttonClick_operation(" % "))
button_neg = tk.Button(root, text="(-)", padx=36, pady=40, command=lambda: buttonClick_neg())
button_equal = tk.Button(root, text="=", padx=40, pady=40, command=lambda: buttonClick_equal())
button_plus = tk.Button(root, text="+", padx=40, pady=40, command=lambda: buttonClick_operation(" + "))
button_minus = tk.Button(root, text="-", padx=40, pady=40, command=lambda: buttonClick_operation(" - "))
button_multiply = tk.Button(root, text="*", padx=40, pady=40, command=lambda: buttonClick_operation(" * "))
button_divide = tk.Button(root, text="/", padx=40, pady=40, command=lambda: buttonClick_operation(" / "))

button_9.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_7.grid(row=2, column=2)
button_6.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_4.grid(row=3, column=2)
button_3.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_1.grid(row=4, column=2)
button_0.grid(row=5, column=1)

button_exp.grid(row=1, column=1)
button_root.grid(row=1, column=0)
button_mod.grid(row=1, column=2)
button_clear.grid(row=1, column=3)
button_neg.grid(row=5, column=0)
button_equal.grid(row=5, column=2)
button_plus.grid(row=2, column=3)
button_minus.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)
button_divide.grid(row=5, column=3)

root.mainloop()