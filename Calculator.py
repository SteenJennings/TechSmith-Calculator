import tkinter as tk
from tkinter import ttk

key = tk.Tk()

# used to store a running calulation
prev = ""
exp = ""

key.title("TechSmith Calculator")

#TODO: Change the Icon to a Calculator
key.iconbitmap("/Users/steen/Documents/Cs/Various_Coding/TechSmith-Calculator/calculator.ico")

# establishing the window
key.geometry('1010x250')         # normal size
key.maxsize(width=360, height= 500)      # maximum size
key.minsize(width= 360 , height = 500)     # minimum size
key.configure(bg = 'black')

# Create a TKINTER GUI for a Calculator
equation = tk.StringVar()
disp_output = ttk.Entry(key,state= 'readonly',textvariable = equation)
disp_output.grid(rowspan= 1 , columnspan = 100, ipadx = 999 , ipady = 20)


# adding the keyboard buttons first row
seven = ttk.Button(key,text = '7' , width = 4, command = lambda : press('7'))
seven.grid(row = 1 , column = 0, ipadx = 1 , ipady = 10, padx = 0, pady = 5)

eight = ttk.Button(key,text = '8' , width = 4, command = lambda : press('8'))
eight.grid(row = 1 , column = 1, ipadx = 1 , ipady = 10, padx = 0, pady = 5)

nine = ttk.Button(key,text = '9' , width = 4, command = lambda : press('9'))
nine.grid(row = 1 , column = 2, ipadx = 1, ipady = 10, padx = 1, pady = 5)

div_operator = ttk.Button(key,text = '/' , width = 4, command = lambda : press('/'))
div_operator.grid(row = 1 , column = 3, ipadx = 1, ipady = 10, padx = 1, pady = 5)

# adding the keyboard buttons second row
four = ttk.Button(key,text = '4' , width = 4, command = lambda : press('4'))
four.grid(row = 2 , column = 0, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

five = ttk.Button(key,text = '5' , width = 4, command = lambda : press('5'))
five.grid(row = 2 , column = 1, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

six  = ttk.Button(key,text = '6' , width = 4, command = lambda : press('6'))
six.grid(row = 2, column = 2, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

mult_operator = ttk.Button(key,text = '*' , width = 4, command = lambda : press('*'))
mult_operator.grid(row = 2 , column = 3, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

# adding the keyboard buttons third row
one = ttk.Button(key,text = '1' , width = 4, command = lambda : press('1'))
one.grid(row = 3 , column = 0, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

two = ttk.Button(key,text = '2' , width = 4, command = lambda : press('2'))
two.grid(row = 3 , column = 1, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

three  = ttk.Button(key,text = '3' , width = 4, command = lambda : press('3'))
three.grid(row = 3, column = 2, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

min_operator = ttk.Button(key,text = '-' , width = 4, command = lambda : press('-'))
min_operator.grid(row = 3 , column = 3, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

# adding the keyboard buttons fourth row
zero = ttk.Button(key,text = '0' , width = 4, command = lambda : press('0'))
zero.grid(row = 4 , column = 0, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

decimal = ttk.Button(key,text = '.' , width = 4, command = lambda : press('.'))
decimal.grid(row = 4 , column = 1, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

enter   = ttk.Button(key,text = '^' , width = 4, command = lambda : press('^'))
enter.grid(row = 4, column = 2, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

add_operator = ttk.Button(key,text = '+' , width = 4, command = lambda : press('+'))
add_operator.grid(row = 4 , column = 3, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

# adding the keyboard buttons fourth row
clear = ttk.Button(key,text = 'CLEAR' , width = 15, command = lambda : press('CLEAR'))
clear.grid(row = 5 , column = 0, columnspan = 2, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

enter   = ttk.Button(key,text = 'ENTER' , width = 15, command = lambda : press('ENTER'))
enter.grid(row = 5, column = 2, columnspan = 2, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

def press(num):
    global exp
    global prev
    
    # in this case we are evaluating from a clean slate
    if prev == "":
    
    # we have already received input
    else:
            
    exp=exp + str(num)
    equation.set(exp)


key.mainloop()