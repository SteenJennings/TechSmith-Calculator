import tkinter as tk
from tkinter import ttk

key = tk.Tk()

# TODO: 
    # decimals
    # rounding (How many places and when)
    # negative values
    # passing just "." as a value (I want this to be treated as 0)

# used to store a running calulation
display = ""
prev = None
operator = None

operators = {"/": "/", "+": "+", "-": "-", "^": "^", "*": "*"}

key.title("TechSmith Calculator")

#TODO: Change the Icon to a Calculator
key.iconbitmap("/Users/steen/Documents/Cs/Various_Coding/TechSmith-Calculator/calculator.icns")

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
clear = ttk.Button(key,text = 'CLEAR' , width = 4, command = lambda : press('CLEAR'))
clear.grid(row = 5 , column = 0, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

enter   = ttk.Button(key,text = 'ENTER' , width = 15, command = lambda : press('ENTER'))
enter.grid(row = 5, column = 1, columnspan = 2, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

neg_operator = ttk.Button(key,text = 'neg' , width = 4, command = lambda : press('neg'))
neg_operator.grid(row = 5 , column = 3, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

def doMath(prev, display, operator):
    num1, num2 = checkDecimals(prev, display)
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        if num2 == 0:
            return "ERROR"
        return num1 / num2
    if operator == "^":
        return num1 ** num2
    return

# checks whether two values are decimals or integers and returns the floating point value
def checkDecimals(prev, display):
    if "." in prev:
        num1 = float(prev)
    else:
        num1 = int(prev)
    if "." in display:
        num2 = float(display)
    else:
        num2 = int(display)
    return num1, num2

def cleanNum(num):
    """takes in an integer or floating point value and returns a 
    string of the number with at most 8 decimal places"""
    res = "{:.8g}".format(num)
    return str(res)

def press(ele):
    global prev
    global display
    global operator
    global operators
    
    #todo: handle negatives in the calculator
    # clearing the display logic, resets everything to starting form
    if ele == "CLEAR":
        display = ""
        prev = None
        operator = None
        equation.set(display)
        return
    
    # logic to handle bad input while there is an error (WORKING)
    if ele != "CLEAR" and display == "ERROR - Press CLEAR":
        return
    
    # blocks the user from using multiple decimal places (WORKING)
    if ele == ".":
        if "." in display:
            return
    
    # handle the ENTER key
    if ele == "ENTER":
        if prev != None and display != None:
            # logic to handle
            calcNum = doMath(prev, display, operator)
            if calcNum == "ERROR":
                display = "ERROR - Press CLEAR"
                equation.set(display)
                return
            display = cleanNum(calcNum)
            operator = None
            equation.set(display)
            prev = None
            return
        # we return if we are not "ready" for the ENTER key
        else:
            return        
    
    # in this case we are evaluating without a running operator
    if ele not in operators and operator == None:
        display=display + str(ele)
        equation.set(display)
        return
        
    if ele in operators and display != "":
        operator = ele
        return
    
    # if we already have a value in the display and we just added an operator, create a second display value 
    if operator != None and ele not in operators:  # we will also need to make sure its not clear or enter, but we can handle that above
        # if we have not assigned our "Prev" operator yet, we also need to reset display
        if prev == None:
            prev = display
            display = ""
        
        display=display + str(ele)
        equation.set(display)
        return
    
    if operator != None and prev != None and display != None and (ele in operators or ele == "enter"):
        calcNum = doMath(prev, display, operator)
        if calcNum == "ERROR":
            display = "ERROR - Press CLEAR"
            equation.set(display)
            return
        display = cleanNum(calcNum)
        operator = ele
        equation.set(display)
        prev = None
        return
        
key.mainloop()