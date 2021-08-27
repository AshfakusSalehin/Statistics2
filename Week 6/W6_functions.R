x <-c(2,4,8,16,32,64,128)
#example of a simple inbuild sum function
print(x)
print("Sum of the array:")
print(sum(x))

#example of inbuild mean function
print("Mean of the array:")
print(mean(x))

#making a function to find factorial
factoria <-function(x){
  fac=1
  while(x>0){
    fac=fac*x
    x=x-1
  }
  print(fac)
}
print("Factorial of 5")
factoria(5)

#making nCr function
nCr <-function(n,r){
  s=factoria(n)/(factoria(r)*factoria(n-r))
  print(s)
}

print("Finding the value of 4C2")
nCr(4,2)