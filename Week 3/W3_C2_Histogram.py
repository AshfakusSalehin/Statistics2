import matplotlib.pyplot as plt 
import numpy as np

x = (12,34,56,75,93)
y= (10,20,30,40,50)

plt.hist(x,y)

plt.xlabel('x-values')
plt.ylabel('y-values')
plt.title('Histogram')
plt.grid(True)
plt.show()