#
# Title: RadioButton, CheckButton, ComboBox, and ListBox.
# 
# Description: Python GUI Programming: This code demonstrates basic Widgets   
#              RadioButton, CheckButton, ComboBox, and ListBox.
# 
# Copyright: MD.ASHFAK US SALEHIN Â© 2021-11-08 
# 
# Author: MD.ASHFAK US SALEHIN
# 
# Version: 1.00	     2021-11-08  Baseline


import tkinter as tk
from tkinter import ttk
from tkinter import *


# Creating tkinter window 
window = tk.Tk() 
window.title('RadioButton, CheckButton, ComboBox & ListBox') 
window.geometry('500x500') 


#This function will be called when ever a radio buttion is selected to 
# declare which radio button is selected
def sel():
   selection = "You selected the option " + str(var.get())
   label2.config(text = selection)


# Dynamic Variables to convey messages 
var = IntVar()
CheckVar1 = IntVar()
CheckVar2 = IntVar()

#label text for title
label1 = Label(window, text = "Reservation System",font = ("Times New Roman", 15))
label1.pack()

# The radio buttons 
R1 = Radiobutton(window, text="One way", variable=var, value=1,command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(window, text="Round Trip", variable=var, value=2,command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(window, text="Multi cities", variable=var, value=3,command=sel)
R3.pack( anchor = W)

#A label to declare which radio button is selected
label2 = Label(window)
label2.pack()


#Label to give hint
label3 = Label(window, text = "Select Port of Departure :",font = ("Times New Roman", 10))
label3.pack()

# Combobox creation
d = StringVar()
portchoosen = ttk.Combobox(window, width = 27, textvariable = d)
  
# Adding combobox drop down list
portchoosen['values'] = (' Delhi',' Haryana',' Punjab',' Chandighar',' Himachapradesh',' Jummu',' Kashmir',' Mumbai',' Banglore',' KolKata',' Darjeeling',' Guwahati')
portchoosen.pack()
portchoosen.current()

#label to give hint
label4 = Label(window, text = "Select Port of Arrival :",font = ("Times New Roman", 10))
label4.pack()

# Combobox creation
a = StringVar()
portch = ttk.Combobox(window, width = 27, textvariable = a)
  
# Adding combobox drop down list
portch['values'] = (' Delhi',' Haryana',' Punjab',' Chandighar',' Himachapradesh',' Jummu',' Kashmir',' Mumbai',' Banglore',' KolKata',' Darjeeling',' Guwahati')
portch.pack()
portch.current()


#label to give hint
label5 = Label(window, text = "Select Facilities :",font = ("Times New Roman", 10))
label5.pack()

# The Check Buttons
C1 = Checkbutton(window, text = "Food", variable = CheckVar1, onvalue = 1, offvalue = 0, width = 20)
C2 = Checkbutton(window, text = "Cancel/Change", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20)
C1.pack()
C2.pack()

#label to give hint
label5 = Label(window, text = "Select Concession type :",font = ("Times New Roman", 10))
label5.pack()

# Listbox creation
Lb1 = Listbox(window)

#Adding Listbox items
Lb1.insert(1, "Senior Citizen")
Lb1.insert(2, "Armed force")
Lb1.insert(3, "Student")
Lb1.insert(4, "Police force")
Lb1.insert(5, "Disabled")
Lb1.insert(6, "Sportsman")
Lb1.pack()

 
window.mainloop()