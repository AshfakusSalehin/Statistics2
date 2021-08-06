import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, t1, color='tab:blue', marker='x')
plt.plot(t2, t2, color='black')

plt.subplot(212)
plt.plot(t2, np.cos(t2), color='tab:orange', linestyle='--')
plt.show()