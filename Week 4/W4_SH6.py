#
# Title:Change String.
# 
# Description: Python GUI Programming: This code accept a String 
#              and convert the entered string either into toGGLe or 
#              Sentence, UPPER, lower, Title case
# 
# Copyright: MD.ASHFAK US SALEHIN Â© 2021-10-08 
# 
# Author: MD.ASHFAK US SALEHIN
# 
# Version: 1.00	     2021-10-08  Baseline

from tkinter import * 
from tkinter import messagebox

#The GUI Window 
top = Tk()  
top.geometry("500x400")
top.title("GUI APP - Correlation in Python")

#Dynamic variables to get the inpput and show the output
myText=StringVar()
wr = StringVar()


#This function takes the input and coverts all of it to Capital letters
def uper():
	co= wr.get()
	myText.set(co.upper())

#This function takes the input and coverts all of it to Small letters
def loer():
	co= wr.get()
	myText.set(co.lower())

#This function takes the input and coverts Capitalletter to small letters and 
#  small letters to Capital letters
def tog():
	co= wr.get()
	str=""
	for x in co:
		if(x.isupper()):
			str+= x.lower()
		elif(x.islower()):
			str+=x.upper()
		else:
			str+=" "		
	myText.set(str)

#This function takes the input and coverts first letter to Capital letter
def sen():
	co= wr.get()
	str=""
	i=0
	for x in co:
		i=i+1
		if(i==1):
			str+= x.upper()
		else:
			str+=x.lower()
	myText.set(str)

#This function takes the input and coverts all first alphabet of each word to Capital letters
def title():
	co= wr.get()
	str=""
	i=0
	for x in co:
		i=i+1
		if(i==1):
			str+= x.upper()
		elif(x.isspace()):
			i=0
			print("space found")
			str+=" "
		else:
			str+=x.lower()
	myText.set(str)

#label for the title
heading = Label(top, text = "Enter a word or sentence")
heading.config(font=('Helvetica bold',20))
heading.place(x = 100,y = 10)

#label for the output
res = Label(top, text = "", textvariable=myText, fg='#00008b',font=('Helvetica bold',15)).place(x=150,y=200)
myText.set("The Result will be shown here")

#Textarea to give the input
word = Entry(top,textvariable = wr)
word.focus_set()
word.place(x=100, y=70,width=350)

#the buttons to perform the pre-defined operations
button1 = Button(top, text = "Upper",command=uper).place(x = 100, y = 250,width=100)
button2 = Button(top, text = "Lower",command=loer).place(x = 300, y = 250,width=100)
button3 = Button(top, text = "TOGGLE", command= tog).place(x = 100, y = 300,width=100)
button4 = Button(top, text = "Sentence", command=sen).place(x = 300, y = 300,width=100)
button5 = Button(top, text = "Title", command=title).place(x = 200, y = 345,width=100)

#Button to exit
quitBt= Button(top, text = "EXIT", fg='#ff0000', command = top.destroy).place(x=240,y =375)

#Runs the program
top.mainloop()  