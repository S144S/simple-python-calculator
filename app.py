from tkinter import *
from math import *

expression = ""
convert_constant = 1

def btn_click(expression_val):
    global expression
    if len(expression) >= 18:
        text_input.set('Too big')
    else:
        expression = expression + str(expression_val)
        text_input.set(expression)
    

def clear_all():
    global expression
    expression = ""
    text_input.set("")

def btn_equal():
    global expression
    try:
        if('pi' in expression):
            expression = expression.replace('pi', '3.1415')
        sum_up = str(eval(expression))
        text_input.set(sum_up)
        expression = sum_up
    except:
        expression = ""
        text_input.set('Invalid equation')


window = Tk()
# Set tile
window.title("Simple Calulator")
# Set the App size
window.geometry('320x500')
# Make the App not resizable
window.resizable(False, False)
# Add font
window.option_add('*Font', 'arial 20 bold')
# Create string for input text
text_input = StringVar()
# The frame that contains input
top_frame = Frame(window, width=320, height=20, bd=4, relief='flat', bg='#666666')
top_frame.pack(side = TOP)
# The frame that contains all buttons
bottom_frame = Frame(window, width=320, height=470, bd=4, relief='flat', bg='#666666')
bottom_frame.pack(side = BOTTOM)
# Make calculator display
display = Entry(top_frame, bg='#2c31c7', fg='white', bd=15,
                justify='left', relief=RIDGE, textvariable=text_input)
display.pack(side = TOP)
# Make calculator buttons
# clear
clear = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="C", command= lambda: clear_all())
clear.grid(row=1, column=0)

# ^2
pow_3 = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="^3", command= lambda: btn_click('**3'))
pow_3.grid(row=2, column=0)
# Root
root = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="√", command= lambda: btn_click('sqrt('))
root.grid(row=2, column=1)
# ^10
pow_10 = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="^10", command= lambda: btn_click('**10'))
pow_10.grid(row=2, column=2)
# residual
residual = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=6,
                        text="%", command= lambda: btn_click('%'))
residual.grid(row=2, column=3)

# 9
nine = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="9", command= lambda: btn_click('9'))
nine.grid(row=3, column=0)
# square
square = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="^2", command= lambda: btn_click('**2'))
square.grid(row=3, column=1)
# x^-1
pi = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="π", command= lambda: btn_click('pi'))
pi.grid(row=3, column=2)
# /
divide = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=6,
                        text="/", command= lambda: btn_click('/'))
divide.grid(row=3, column=3)

# 6
six = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="6", command= lambda: btn_click('6'))
six.grid(row=4, column=0)
# 7
seven = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="7", command= lambda: btn_click('7'))
seven.grid(row=4, column=1)
# 8
eight = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="8", command= lambda: btn_click('8'))
eight.grid(row=4, column=2)
# X
cross = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=6,
                        text="X", command= lambda: btn_click('*'))
cross.grid(row=4, column=3)

# 3
three = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="3", command= lambda: btn_click('3'))
three.grid(row=5, column=0)
# 4
four = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="4", command= lambda: btn_click('4'))
four.grid(row=5, column=1)
# 5
five = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="5", command= lambda: btn_click('5'))
five.grid(row=5, column=2)
# +
plus = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=6,
                        text="+", command= lambda: btn_click('+'))
plus.grid(row=5, column=3)

# 0
zero = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="0", command= lambda: btn_click('0'))
zero.grid(row=6, column=0)
# 1
one = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="1", command= lambda: btn_click('1'))
one.grid(row=6, column=1)
# 2
two = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="2", command= lambda: btn_click('2'))
two.grid(row=6, column=2)
# +
minus = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=6,
                        text="-", command= lambda: btn_click('-'))
minus.grid(row=6, column=3)

# )
open_brack = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="(", command= lambda: btn_click('('))
open_brack.grid(row=7, column=0)
# (
close_brack = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text=")", command= lambda: btn_click(')'))
close_brack.grid(row=7, column=1)
# .
dot = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text=".", command= lambda: btn_click('.'))
dot.grid(row=7, column=2)
# =
equal = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=6,
                        text="=", command= lambda: btn_equal())
equal.grid(row=7, column=3)

# Show th App
window.mainloop()