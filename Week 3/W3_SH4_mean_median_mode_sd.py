import collections
import math

data = [1,3,5,7,9,2,4,3,8]
#Finding size of array
n= len(data)

#Finding mean
mean= (sum(data)/n)
data.sort() #sorting the array elements

#Finding Median
if((n%2)==0):
    median =data[(n/2)]+data[(n/2)+1]/2
else:
    median = data[int(n/2)+1]

#Finding Mode 
count = collections.Counter(data)
max_value = max(list(count.values()))
mode = [n for n, freq in count.items() if freq == max_value] 
		
#finding standard deviation
diff=[]
diff_sq=[]
for i in data:
	diff.append(i-mean)
for j in diff:
	diff_sq.append(j*j)
var = (sum(diff_sq)/n)
sd = math.sqrt(var)


print(data)
print("\nMean=",mean)
print("\nMedian=",median)
if (len(mode) == n):
   print("\nNo mode in the list")
else:
   print("\nThe Mode is : " ,mode)
print("\nVariance:",var)
print("\nStandard Deviation:",sd)