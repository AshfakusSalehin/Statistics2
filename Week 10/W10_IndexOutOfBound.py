import sys
x=[]
j=0
try:
	f = open('myfile.txt')
	s = f.readline()
	i=1
	while (i<5):
		x.append(int(s.strip()))
		i=i+1
	while(j<10):
		print(x[j])
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except IndexOutOfBound:
    print("Index out of bound error:")
    
