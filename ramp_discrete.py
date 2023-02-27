
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
plt.stem(n, y)
plt.axis([-2.1, 5.1, -0.1, 5.2])
plt.xlabel('  n ')
plt.ylabel('x(n)  ')
plt.title('Ramp signal discrete')

plt.grid(True)
plt.show()