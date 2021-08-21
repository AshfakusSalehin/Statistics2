myVal <- c(23,34,14,45,56,76)
#For loop example
print("This is printed using for loop")
for (i in 1:5){
  print(myVal[i])
}
# While loop example
print("This is printed using while loop")
j=0
while(j<5){
  j=j+1
  print(myVal[j])
}

#this is control structure
a=2
b=5

if(a<b){
  print("a is smaller than b")
}else if(a==b){
  print("a is equal to b")
}else if(a>b){
  print("a is greater than b")
}else{
  print("Unexpected error")
}
