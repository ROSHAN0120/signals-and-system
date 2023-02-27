

import matplotlib.pyplot as plt

a = 0.9
n = range(0, 26, 1)
y = []

for i in range(len(n)):
    temp = a**n[i]
    y.append(temp)
    


plt.axvline(x=0, c="red" )
plt.axhline(y=0, c="red")
plt.stem(y)
plt.axis([-0.3, 25.1, -0.1, 1.1])
plt.xlabel('  n ')
plt.ylabel('x(n)  ')
plt.title('Exponential signal discrete')
plt.grid(True)
plt.show()