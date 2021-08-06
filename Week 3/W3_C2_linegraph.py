import matplotlib.pyplot as plt 
import numpy as np

x = (12,34,56,75,93)
y = (27,44,68,83,97)
z = (5,10,15,20,25)

plt.plot(x,z,color='blue')
plt.plot(y,z,color='red')
plt.plot(x,y,color='green')

plt.hist(x,y)

#plt.imshow("clickme")

plt.xlabel('x-values')
plt.ylabel('y-values')
plt.title('line plot')
plt.grid(True)
plt.show()