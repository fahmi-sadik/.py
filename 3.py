import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)




plt.figure(figsize=(5, 6))

plt.plot(x,np.sin(x) )


plt.plot(x, np.cos(x))


plt.plot(x,np.tan(x))


plt.ylim(-20, 20) 


plt.legend()
plt.grid(True)

plt.show()
