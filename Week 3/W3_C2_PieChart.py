import matplotlib.pyplot as plt 
import numpy as np

x = (12,34,56,75,93)
y = (27,44,68,83,97)
z = (5,10,15,20,25)
plt.subplot(211)
plt.pie(x)
plt.subplot(212)
plt.pie(y)

plt.title('Pie Chart')
plt.show()