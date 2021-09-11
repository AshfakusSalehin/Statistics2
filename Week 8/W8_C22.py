#Named function
def add(x,y,z):
	sum = x+y+z
	return sum

#Lambda function
sum1 = lambda x,y,z: (x+y+z)
	


a= add(5,6,7)

print("Added 5,6,7 using named function add :")
print(a)

print("Added 5,6,7 using lambda function")
print(sum1(5,6,7))