#This is multiplication of two matrixes

firstM <-matrix(c(1,2,3,4,5,6,7,8,9),nrow=3,ncol=3)

secondM <-matrix(c(1,0,0,0,1,0,0,0,1),nrow=3,ncol=3)

result <-matrix(c(0,0,0,0,0,0,0,0,0),nrow=3,ncol=3)

print("This is first matrix")
print(firstM)
print("This is second matrix/ identity matrix")
print(secondM)
print("The multiplication between the two matrixes using'*'")
print(firstM*secondM)
print("The multiplication between the two matrixes using proper mathmatical rules")
print(firstM%*%secondM)
print("Manually conducting multiplication between two")
i=j=1
while(i<=3){
  while(j<=3){
    x= firstM[i,]
    y=secondM[,j]
    z=x*y
    result[i,j]=sum(z)
    j=j+1
  }
  i=i+1
}
print(result)
