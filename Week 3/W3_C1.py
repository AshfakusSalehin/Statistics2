from tkinter import *

#Defineing tkinter instance
root= Tk()
root.title("Week 3 Practice Problems")
root.geometry("700x500")

#Defining the working of the button
def mess():
   text.config(text= "You have clicked the button",font=('Helvetica bold',15))

#Defining a function to change the bg of button
def change_color():
   button2.configure(bg="OrangeRed3", fg= "white")

#Creating label for the button
label1= Label(root, text="This is a image in a Button")
label1.pack()

#Importing the image using PhotoImage function
click_btn= PhotoImage(file='clickme.png')

#creating a button to pass the image
button1= Button(root, image=click_btn,command= mess,cursor="clock")
button1.pack()

text= Label(root, text= "")
text.pack()

#Creating label for the button
label2= Label(root, text="This Button changes Background Color")
label2.pack()

button2= Button(root, text ="RESET", command=change_color, cursor="spider")
button2.pack()

l1= Label(root,text="Name:",fg='#00008b').place(x=120,y=310)
name = Entry(root)#.place(x=160,y=310)
name.focus_set()
name.pack()
name.place(x=160,y=310)
l2= Label(root,text="ID:",fg='#00008b').place(x=120,y=350)
l3= Label(root,text="Email:",fg='#00008b').place(x=120,y=390)


id = Entry(root).place(x=160,y=350)
email=Entry(root).place(x=160,y=390)

root.mainloop()