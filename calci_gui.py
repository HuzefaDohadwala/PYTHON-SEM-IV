from tkinter import *

def press(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(num))

def clear():
    entry.delete(0, END)

def equalto():
    try:
        current = entry.get()
        result = eval(current)
        entry.delete(0, END)
        entry.insert(END, result)
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

root = Tk()
root.title("Simple Calculator")

entry = Entry(root, width=30, justify="right")
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

buttons = [
    ['1', '2', '3', '+'],
    ['4', '5', '6', '-'],
    ['7', '8', '9', '*'],
    ['0', '.', '=', '/']
]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        button = Button(root, text=buttons[i][j], padx=20, pady=20, command=lambda x=buttons[i][j]: press(x))
        button.grid(row=i+1, column=j, padx=5, pady=5)

clear_button = Button(root, text="C", padx=20, pady=20, command=clear)
clear_button.grid(row=5, column=0, padx=5, pady=5)

equal_button = Button(root, text="=", padx=20, pady=20, command=equalto)
equal_button.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

root.mainloop()
