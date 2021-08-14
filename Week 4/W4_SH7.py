#
# Title:Project 1: Correlation in Python.
# 
# Description: A tikinter application: This code extracts the datates from an excel file 
#              and returns the corellation using three different method. It also has a panel
#              to represent the datas visually.
# 
# Copyright: MD.ASHFAK US SALEHIN Â© 2021-12-08 
# 
# Author: MD.ASHFAK US SALEHIN
# 
# Version: 1.00	2021-12-08 Baseline


from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog as fd
import collections
import math
import xlrd 
import openpyxl
import math
import matplotlib.pyplot as plt 
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from scipy.stats import spearmanr

xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True

#Declaring the GUI. it's size and title 
top = Tk()  
top.geometry("500x600")
top.title("GUI APP - Correlation in Python")

#Global variables
myText=StringVar()             #this is a dynamic variable to show the result
data=[]                        #this a list which recieves the extracted datas and puts them in the treeView
Xcor=[]                        # this is a list which will containe all the X-coordinates
Ycor=[]                        # this is a list which will containe all the X-coordinates


#This function helps to browse through the documents and extract X and Y coordinates from the selected file
# and stores the values in their respective list and also in data list. Then it calls another function
# to add data.
def browse():
	name=fd.askopenfilename()
	loc=(name)
	wb = xlrd.open_workbook(loc)
	worksheet = wb.sheet_by_name('Sheet1') 
	worksheet = wb.sheet_by_index(0) 	
	i=1
	while (i<11):
		x = worksheet.cell(i, 0)
		y = worksheet.cell(i, 1)
		print(" ", int(x.value), " ", int(y.value)) #, " ", int(mrks.value))		
		data.append((int(x.value),int(y.value)))
		Xcor.append(int(x.value))
		Ycor.append(int(y.value))
		i=i+1
	adddata()
	
# This function adds the retrieved data to the treeview which is then presented in GUI
def adddata():
	for d in data:
		tree.insert('', tk.END, values=d)
	def item_selected(event):
		for selected_item in tree.selection():
			# dictionary
			item = tree.item(selected_item)
			# list
			record = item['values']
			showinfo(title='Information',message=','.join(record))
	tree.bind('<<TreeviewSelect>>', item_selected)


def mean(m):
	n= len(m)
	data.sort()
	mean= (sum(data)/n)
	#myText.set("Mean is: %f"%(mean))
	return mean

def median():
	n= len(data)
	data.sort()
	if((n%2)==0):
    		median =((data[int(n/2)]+data[int(n/2)+1])/2)
	else:
    		median = data[int(n/2)+1]
	myText.set("Median is: %f"%(median))

def mode():
	n= len(data)
	data.sort()
	count = collections.Counter(data)
	max_value = max(list(count.values()))
	mode = [num for num, freq in count.items() if freq == max_value] 			
	myText.set("Mode is: %s"%str(mode))

def sd():
	n= len(data)
	data.sort()
	diff=[]
	diff_sq=[]
	mean= (sum(data)/n)
	for i in data:
		diff.append(i-mean)
	for j in diff:
		diff_sq.append(j*j)
	var = (sum(diff_sq)/n)
	std = math.sqrt(var)
	myText.set("Standard deviation is: %.5f"%(std))

# This function computes correlation using Karl-Pearson Correlation coefficient method and then prints
# the result in the result area. 
def karl():
	i=0
	sum_xy=0
	sum_x=0
	sum_y=0
	sum_x2=0
	sum_y2=0
	while(i<10):
		sum_x += Xcor[i]
		sum_y += Ycor[i]
		sum_x2 += (Xcor[i]*Xcor[i])
		sum_y2 += (Ycor[i]*Ycor[i])
		sum_xy+= (Xcor[i]*Ycor[i])
		i=i+1
	nExy= sum_xy*10
	nEx2= sum_x2*10
	ExEy= sum_x*sum_y
	nEy2 = sum_y2*10
	Ex2 = sum_x*sum_x
	Ey2 = sum_y*sum_y
	u = nExy-ExEy
	d = ((math.sqrt(nEx2-Ex2 ))*(math.sqrt(nEy2-Ey2)))
	r=u/d
	myText.set("Karl-Pearson Coorelation: %.10f"%(r))

#This method calculate coorelation using spearman rank's  correlation method
def rank():
	coef, p = spearmanr(Xcor, Ycor)
	myText.set("Rank Coorelation: %.10f"%(coef))

#This function graphically represents the datas in a line graph 
def linegraph():
	plt.plot(Xcor,Ycor,color='blue')
	plt.xlabel('x-values')
	plt.ylabel('y-values')
	plt.title('line plot')
	plt.show()
	plt.place(x=50,y=370)

#This button graphically represents the datas in a Pie-graph
def pie():
	plt.subplot(211)
	plt.pie(Xcor)
	plt.subplot(212)
	plt.pie(Ycor)
	plt.title('Pie Chart')
	plt.show()

#this title is for giving hint to the user
heading = Label(top, text = "Select the data file .xls/.xlsx")
heading.config(font=('Helvetica bold',20))
heading.place(x = 100,y = 10)

#this label shows the results after every calculation
res = Label(top, text = "", textvariable=myText, fg='#00008b',font=('Helvetica bold',15)).place(x=50,y=400)
myText.set("The Result will be shown here")


# columns for the treeView
columns = ('#1', '#2')

#Creating tree
tree = ttk.Treeview(top, columns=columns, show='headings')

# The headings of the column are defined here
tree.heading('#1', text='X Coordinates')
tree.heading('#2', text='Y coordinates')
tree.place(x=50,y=100,width=400,height=250)      #the position and size of the tree is declared here

#this button calls the browse function which is used to select file by the user
browseBt = Button(top, text = "Browse File",command=browse).place(x=200, y=350)

#This button calls the karl() method which computes correlation using Karl-Pearson Correlation coefficient method 
button1 = Button(top, text = "Karl-Pearson Method",command=karl).place(x = 50, y = 450,width=150)

#This button calls the karl() method which computes correlation using Rank Correlation method
button2 = Button(top, text = "Rank Correlation Method",command=rank).place(x = 300, y = 450,width=150)

#This button graphically represents the datas in a linegraph
button3 = Button(top, text = "Line-Graph", command= linegraph).place(x = 50, y = 500,width=150)

#This button graphically represents the datas in a Pie-graph
button4 = Button(top, text = "Pie Graph", command=pie).place(x = 300, y = 500,width=150)


#This button closes or destrys the GUI
quitBt= Button(top, text = "EXIT", fg='#ff0000', command = top.destroy).place(x=240,y =550)

#This runs the application
top.mainloop()  