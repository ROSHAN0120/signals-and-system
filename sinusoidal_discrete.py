
import numpy as np

import matplotlib.pyplot as plt
time        = np.arange(0, 10, 0.1)
amplitude   = np.sin(time)
plt.stem(time, amplitude)


plt.title('Sinusoidal signal discrete')


plt.xlabel('t')
plt.ylabel('x(t)') 

plt.grid()
plt.axhline(y=0, color='green')
plt.axvline(x=0, color='green')
plt.show()


plt.show()