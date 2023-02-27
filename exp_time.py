
import matplotlib.pyplot as plt

a = .9
n = range(0, 26, 1)
y = []

for i in range(len(n)):
    temp = a**n[i]
    y.append(temp)
    


plt.axvline(x=0, c="green" )
plt.axhline(y=0, c="green")
plt.plot(y)
plt.xlabel(' t  ')
plt.ylabel('x(t) ')
plt.title('Exponential signal time')
plt.grid(True)
plt.show()