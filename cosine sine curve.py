import numpy as np
import matplotlib.pyplot as plt

#sine curve

x= np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.sin(x)
#plt.plot(x,y)

#cosine curve

y2 = np.cos(x)
#plt.plot(x,y2,"r")

#sine curver graphed with degrees

x2 = np.arange((-2*np.pi)*180/np.pi, (2*np.pi)*180/np.pi, 180/31.5)
plt.plot(x2,y)

#cosine curve graphed with degrees

plt.plot(x2,y2, "r")

#grapher
plt.show()
