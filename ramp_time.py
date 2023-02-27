

import matplotlib.pyplot as plt

n = range(-2, 6, 1)
y = []
for i in range(len(n)):
    temp = (n[i] if n[i]>=0 else 0)
    y.append(temp)
    
print(list(n))
print(y)


plt.axvline(x=0, c="red" )
plt.axhline(y=0, c="red")
plt.plot(n, y)
plt.axis([-2.1, 5.1, -0.1, 5.2])
plt.xlabel('  t ')
plt.ylabel('x(t)  ')
plt.title('Ramp signal time')
plt.grid(True)
plt.show()