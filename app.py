
from tkinter import *

deg_mode_flag = False
rad_mode_flag = True
# Common butns propertires
btn_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': '#666666',
    'font': ('arial', 18),
    'width': 2,
    'height': 2,
    'relief': 'flat',
    'activebackground': "#666666"
}

window = Tk()
# Set tile
window.title("144 Calulator")
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
                justify='right', relief=RIDGE, textvariable=text_input)
display.pack(side = TOP)
# Make calculator buttons
# # DEG
# deg_mode = Checkbutton(bottom_frame, bg='#666666', fg= 'white', text="DEG", variable=deg_mode_flag,
#                         onvalue=True, offvalue=False)
# deg_mode.grid(row=0, column=0)
# # RAD
# rad_mode = Checkbutton(bottom_frame, text="DEG", variable=rad_mode_flag,
#                         onvalue=True, offvalue=False)
# rad_mode.grid(row=0, column=2)
# ^2
pow_2 = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="^2", command= '')
pow_2.grid(row=1, column=0)
# ^3
pow_3 = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="^3", command= '')
pow_3.grid(row=1, column=1)
# ^10
pow_10 = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="^10", command= '')
pow_10.grid(row=1, column=2)
# Sin
sin = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=6,
                        text="sin", command= '')
sin.grid(row=1, column=3)
# ^1/2
root = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="^1/2", command= '')
root.grid(row=2, column=0)
# 10^
pow_to_10 = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="10^", command= '')
pow_to_10.grid(row=2, column=1)
# log
log = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=3,
                        text="log", command= '')
log.grid(row=2, column=2)
# Cos
cos = Button(bottom_frame, bg='#666666', fg='white', bd=4,
                        height=1, width=6,
                        text="cos", command= '')
cos.grid(row=2, column=3)
# # (
# btn_left_brack = Button(bottom_frame, bg='#666666', fg='white', bd=4,
#                         height=1, width=3,
#                         text="(", command= '')
# btn_left_brack.grid(row=0, column=0)
# # )
# btn_left_brack = Button(bottom_frame, bg='#666666', fg='white', bd=4,
#                         height=1, width=3,
#                         text=")", command= '')
# btn_left_brack.grid(row=0, column=1)
# # 0
# btn_left_brack = Button(bottom_frame, bg='#666666', fg='white', bd=4,
#                         height=1, width=3,
#                         text="0", command= '')
# btn_left_brack.grid(row=0, column=2)
# # .
# btn_left_brack = Button(bottom_frame, bg='#666666', fg='white', bd=4,
#                         height=1, width=1,
#                         text=".", command= '')
# btn_left_brack.grid(row=0, column=3)
# # =
# btn_left_brack = Button(bottom_frame, bg='#666666', fg='white', bd=4,
#                         height=1, width=3,
#                         text="=", command= '')
# btn_left_brack.grid(row=0, column=4)

# btn_left_brack = Button(bottom_frame, bg='#666666', fg='white', bd=4,
#                         height=1, width=4,
#                         text="(", command= '')
# btn_left_brack.grid(row=0, column=5)

# btn_left_brack = Button(bottom_frame, bg='#666666', fg='white', bd=4,
#                         height=1, width=3,
#                         text="(", command= '')
# btn_left_brack.grid(row=1, column=0)
# Entry(window, relief=RIDGE, textvariable=display,
#         justify='right'
#         , bd=30, bg="powder blue").pack(side=TOP,
#         expand=YES, fill=BOTH)
# Show th App
window.mainloop()