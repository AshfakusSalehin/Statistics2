
i=29
  a=0
  for(j in 2:(i-1))
  {
    if((i%%j) == 0)
    {
      a=1
    }
  }  
 
  if(a==0){
    print("It is a prime no")
  }else{
      print("It is not a prime no")
    }
 