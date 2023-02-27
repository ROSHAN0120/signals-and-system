
import matplotlib.pyplot as plt

n = range(-1, 6, 1)
y = []
for i in range(len(n)):
    temp = (1 if n[i]== 0 else 0)
    y.append(temp)
    
print(n)
print(y)



plt.grid()
plt.xlabel('  n ')
plt.ylabel('x(n)  ')
plt.title('Impulse discrete')

plt.stem(n, y)

plt.show()