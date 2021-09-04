#reading data from a CSV file

mydata <-(read.csv("D:/Education/Semester 5/Statistic 2/myfile.csv"))
print("Printing the data which is read from myfile.csv")
print(mydata)
#Printing data with specific properties
print("Printing data with department as CSE:")
print(subset(mydata,Dept=="CSE"))
print("Printing data with marks more than 60")
print(subset(mydata,Marks>60))

#Writing the data of cse department into a csv file
write.csv(subset(mydata,Dept=="CSE"),"D:/Education/Semester 5/Statistic 2/copyfile.csv")