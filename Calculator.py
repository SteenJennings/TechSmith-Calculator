import tkinter as tk
from tkinter import ttk

calc = tk.Tk()

# TODO: 
    # negative values
        # integrate a "-" symbol by pre-pending a negative sign
        # this should be handled by string conversions to int
        # we will need to make sure we are not overwriting, unless we want to be able to remove negative signs
        
    # passing just "." as a value (I want this to be treated as 0)
        # if we are placing a decimal point at the start, we should automatically add a 0 to pre-pend it
        
    # handling leading 0's before non-decimal occurrences
        # 0437.55 -> 437.55
        # Could add a rule to ONLY allow leading zeros if the value is a decimal and between -1 and 1
        # if we are already past the decimal point then 0's can be used freely
        
    # accepting input from stdin
        # would function the same as the "press" method, would have issues if 'illegal' keys are pressed
        

# used to store a running calulation
class calcVariables:
    def __init__(self):
        self.prev = None
        self.display = ""
        self.operator = None
        self.count = 0
        self.operators = {"/": "/", "+": "+", "-": "-", "^": "^", "*": "*"}

# calc = Calculation()
# display = ""
# prev = None
# operator = None
# operators = {"/": "/", "+": "+", "-": "-", "^": "^", "*": "*"}
# count = 0

vars = calcVariables()

calc.title("TechSmith Calculator")

#TODO: Change the Icon to a Calculator
calc.iconbitmap("calculator.icns")

# establishing the window
calc.geometry('1010x250')         # normal size
calc.maxsize(width=360, height= 360)      # maximum size
calc.minsize(width= 360 , height = 360)     # minimum size
calc.configure(bg = 'black')

# Create a TKINTER GUI for a Calculator
equation = tk.StringVar()
disp_output = ttk.Entry(calc,state= 'readonly',textvariable = equation)
disp_output.grid(rowspan= 1 , columnspan = 100, ipadx = 999 , ipady = 20)


# adding the calcboard buttons first row
seven = ttk.Button(calc,text = '7' , width = 4, command = lambda : press('7'))
seven.grid(row = 1 , column = 0, ipadx = 1 , ipady = 10, padx = 0, pady = 5)

eight = ttk.Button(calc,text = '8' , width = 4, command = lambda : press('8'))
eight.grid(row = 1 , column = 1, ipadx = 1 , ipady = 10, padx = 0, pady = 5)

nine = ttk.Button(calc,text = '9' , width = 4, command = lambda : press('9'))
nine.grid(row = 1 , column = 2, ipadx = 1, ipady = 10, padx = 1, pady = 5)

div_operator = ttk.Button(calc,text = '/' , width = 4, command = lambda : press('/'))
div_operator.grid(row = 1 , column = 3, ipadx = 1, ipady = 10, padx = 1, pady = 5)

# adding the calcboard buttons second row
four = ttk.Button(calc,text = '4' , width = 4, command = lambda : press('4'))
four.grid(row = 2 , column = 0, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

five = ttk.Button(calc,text = '5' , width = 4, command = lambda : press('5'))
five.grid(row = 2 , column = 1, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

six  = ttk.Button(calc,text = '6' , width = 4, command = lambda : press('6'))
six.grid(row = 2, column = 2, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

mult_operator = ttk.Button(calc,text = '*' , width = 4, command = lambda : press('*'))
mult_operator.grid(row = 2 , column = 3, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

# adding the calcboard buttons third row
one = ttk.Button(calc,text = '1' , width = 4, command = lambda : press('1'))
one.grid(row = 3 , column = 0, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

two = ttk.Button(calc,text = '2' , width = 4, command = lambda : press('2'))
two.grid(row = 3 , column = 1, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

three  = ttk.Button(calc,text = '3' , width = 4, command = lambda : press('3'))
three.grid(row = 3, column = 2, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

min_operator = ttk.Button(calc,text = '-' , width = 4, command = lambda : press('-'))
min_operator.grid(row = 3 , column = 3, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

# adding the calcboard buttons fourth row
zero = ttk.Button(calc,text = '0' , width = 4, command = lambda : press('0'))
zero.grid(row = 4 , column = 0, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

decimal = ttk.Button(calc,text = '.' , width = 4, command = lambda : press('.'))
decimal.grid(row = 4 , column = 1, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

enter   = ttk.Button(calc,text = '^' , width = 4, command = lambda : press('^'))
enter.grid(row = 4, column = 2, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

add_operator = ttk.Button(calc,text = '+' , width = 4, command = lambda : press('+'))
add_operator.grid(row = 4 , column = 3, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

# adding the calcboard buttons fourth row
clear = ttk.Button(calc,text = 'CLEAR' , width = 4, command = lambda : press('CLEAR'))
clear.grid(row = 5 , column = 0, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

enter   = ttk.Button(calc,text = 'ENTER' , width = 15, command = lambda : press('ENTER'))
enter.grid(row = 5, column = 1, columnspan = 2, ipadx = 2 , ipady = 10, padx = 1, pady = 5)

# todo: implement the negative function
neg_operator = ttk.Button(calc,text = 'neg' , width = 4, command = lambda : press('neg'))
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

def updateDisplay(newOperator=None):
  
    calcNum = doMath(vars.prev, vars.display, vars.operator)
    if calcNum == "ERROR":
        vars.displa = "ERROR - Press CLEAR"
        equation.set(vars.display)
        return
    
    vars.display = cleanNum(calcNum)
    vars.operator = newOperator
    equation.set(vars.display)
    vars.prev = None
    return

def press(ele):
    """Handles all the possible routes for key presses on the calculator"""
    vars.count += 1
    
    print(vars.prev, vars.display, vars.operator, vars.count)
    
    #todo: handle negatives in the calculator
    
    # clearing the display logic, resets everything to starting form (WORKING)
    if ele == "CLEAR":
        vars.display = ""
        vars.prev = None
        vars.operator = None
        equation.set(vars.display)
        vars.count = 0
        return
    
    # logic to handle bad input while there is an error (WORKING)
    if ele != "CLEAR" and vars.display == "ERROR - Press CLEAR":
        return
    
    # blocks the user from using multiple decimal places (WORKING)
    if ele == ".":
        if "." in vars.display:
            return
    
    # handle the ENTER key (WORKING)
    if ele == "ENTER":
        if vars.prev != None and vars.display != None:
            # logic to handle
            return updateDisplay()
        # we return if we are not "ready" for the ENTER key to avoid errors
        else:
            return        
    
    # in this case we are evaluating without a running operator (WORKING)
    # we are only checking against operators because the CLEAR and ENTER keys are processed above
    if ele not in vars.operators and vars.operator == None:
        vars.display=vars.display + str(ele)
        equation.set(vars.display)
        return

    # if we already have a value in the display and we just added an operator, create a second display value 
    if vars.operator != None and ele not in vars.operators:  # we will also need to make sure its not clear or enter, but we can handle that above
        print("im here")
        # if we have not assigned our "vars.prev" operator yet, we also need to reset display
        if vars.prev == None:
            vars.prev = vars.display
            vars.display = ""
        
        vars.display=vars.display + str(ele)
        equation.set(vars.display)
        return
    
    #
    if vars.operator != None and vars.prev != None and vars.display != None and ele in vars.operators:
        return updateDisplay(ele)  
    
    # if we have something in the vars.display, we are going to 
    if ele in vars.operators and vars.display != "":
        print("vars.operator print check")
        vars.operator = ele
        return
    
calc.mainloop()