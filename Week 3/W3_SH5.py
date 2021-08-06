from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog as fd
import collections
import math
import xlrd
 
top = Tk()  
top.geometry("500x400")
top.title("GUI APP - Correlation in Python")

myText=StringVar()
data = [1,3,5,7,9,2,4,3,8]
n= len(data)
data.sort()


def browse():
	name=fd.askopenfilename()
	loc=(name)
	wb = xlrd.open_workbook(loc)
	worksheet = wb.sheet_by_index(0)
	total=0
	i=1
	while(i<15):
		sn = worksheet.cell(i,0)
		rn = worksheet.cell(i,1)
		mrks=worksheet(i,2)
		print(" ", int(sn.value), " ",int(rn.value)," ",int(mrks.value))
		i=i+1
		total+=int(mrks.value)
		marks.append(mrks.value) 
	messagebox.showinfo("File Selected:", name)

def mean():
	mean= (sum(data)/n)
	myText.set("Mean is: %f"%(mean))

def median():
	if((n%2)==0):
    		median =data[(n/2)]+data[(n/2)+1]/2
	else:
    		median = data[int(n/2)+1]
	myText.set("Median is: %f"%(median))

def mode():
	count = collections.Counter(data)
	max_value = max(list(count.values()))
	mode = [num for num, freq in count.items() if freq == max_value] 			
	myText.set("Mode is: %s"%str(mode))

def sd():
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


heading = Label(top, text = "Select the data file .xls/.xlsx")
heading.config(font=('Helvetica bold',20))
heading.place(x = 100,y = 10)

#values = Entry(top).place(x = 100, y = 40,width=300,height=400) 

res = Label(top, text = "", textvariable=myText, fg='#00008b',font=('Helvetica bold',15)).place(x=150,y=200)
myText.set("The Result will be shown here")

#res.pack()

browseBt = Button(top, text = "Browse File",command=browse).place(x=400, y=100)

button1 = Button(top, text = "Mean",command=mean).place(x = 100, y = 250,width=100)
button2 = Button(top, text = "Median",command=median).place(x = 300, y = 250,width=100)
button3 = Button(top, text = "Mode", command= mode).place(x = 100, y = 300,width=100)
button4 = Button(top, text = "Standard Deviation", command=sd).place(x = 300, y = 300,width=100)

#result = Entry(top).place(x = 100, y = 600,width=300,height=100) 

quitBt= Button(top, text = "EXIT", fg='#ff0000', command = top.destroy).place(x=240,y =370)

top.mainloop()  