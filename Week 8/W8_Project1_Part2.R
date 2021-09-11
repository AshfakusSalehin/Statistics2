#Reading data from a csv file
data <-(read.csv("D:/Education/Semester 5/Statistic 2/Week 7/coordinates.csv"))
#printing the data
print("The extracted data are:")
print(data)
#saparating the x & y data using $
X = data$x
Y=data$y

#This function takes two vectors and calculates the correlation among them
correlation <-function(Xcor,Ycor){
  i=1
  sum_xy=sum_x2=sum_y2=0
  sum_x =sum(Xcor)
  sum_y= sum(Ycor)
  
  while(i<11)
  {
    sum_x2=sum_x2+ (Xcor[i]*Xcor[i])
    sum_y2=sum_y2+ (Ycor[i]*Ycor[i])
    sum_xy=sum_xy+ (Xcor[i]*Ycor[i])
    i=i+1
  }
  nExy= sum_xy*10
  nEx2= sum_x2*10
  ExEy= sum_x*sum_y
  nEy2 = sum_y2*10
  Ex2 = sum_x*sum_x
  Ey2 = sum_y*sum_y
  u = nExy-ExEy
  d = ((sqrt(nEx2-Ex2 ))*(sqrt(nEy2-Ey2)))
  r=u/d
  cat("The calculated correlation using manual method:",r)
  print("  ")
  #writing the result into a .csv file
  write.csv(r,"D:/Education/Semester 5/Statistic 2/result.csv")
}

pa <-function(){
  pie(X,col=rainbow(10)) 
  pie(Y,col=rainbow(10))
}
sam <-function(){
  #The built-in function to calculate correlation
  result = cor.test(X, Y, method = "pearson") 
  
  # Printing the result 
  print("The result of built in class: ") 
  print(result) 
}


#the  main function starts here



 
k=0
ext<-function(){
  print("Exiting ......")
  k=1
}
while(s==0)
{
  print("Choose an option:")
  print("1.Pearson method ")
  print("2.Simson methon ")
  print("3.pie chart ")
  print("4.bargraph")
  print("0.Exit")
  print("Enter your choice:")
  a <- readline()
  s = strtoi(a, base=0L)
  result =switch(s,
               "1"= cat("Car Pearson correlation",correlation(X,Y)),
               "2"= sam(),
               "3"= pa(),
               "4"= barplot(X,Y,col=rainbow(10)),
               "0"= ext())
  print(result)
}





