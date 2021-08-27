#Pass any number X, write a function to check for palindrome 

# this function checks palindrome
#library(stringi)
checkPalindrome <-function(x) {
  #y=stri_reverse(x)
  x1=x
  y=0
  while(x1>0){
    l=x1%%10
    y=(y*10)+l
    x1=x1%/%10
  }
  if(x==y){
    print ("It is a palindrome number")
  }else{
    print ("It is not a palindrome number")
  }
}

x=123
print(x)
checkPalindrome(x)
x=12321
print(x)
checkPalindrome(x)
