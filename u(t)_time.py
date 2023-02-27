
import matplotlib.pyplot as plt

n = range(-1000, 1000, 1)
y = []
for i in range(len(n)):
    temp = (1 if n[i]>=0 else 0)
    y.append(temp)
    
print(n)
print(y)



plt.grid()
plt.axvline(x=0, c="red" )
plt.axhline(y=0, c="red")
plt.plot(n, y)
plt.xlabel('  t ')
plt.ylabel('x(t)  ')
plt.title('Unit Step signal time')
plt.show()