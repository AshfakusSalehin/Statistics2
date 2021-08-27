#Pass any number X, write a function to check for fibonacci number

#This function checks fibonacci
checkFibonacci <- function(x){
  f=a=i=0
  b=1
  while(i<=x)
  {
    c=a+b
    if (c==x){
      f=1
    break;
      }
    a=b
    b=c
    i=i+1
  }
  if(f==1){
    print ("It belongs to fibonacci series")
  }else{
    print ("It does not belongs to fibonacci series")
  }
  
}

#Calling function to check if it a fibonacci number
print(34)
checkFibonacci(34)
print(123)
checkFibonacci(123)

