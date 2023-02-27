
import matplotlib.pyplot as plt
temp =0
n = [0,6,10]
y = []
for i in range(len(n)):
    if n[i]==0:
        temp=0
  
    y.append(temp)
    
print(n)
print(y)

plt.grid()
plt.axvline(x=0, c="green" )
plt.axhline(y=0, c="green")
plt.xlabel('  t')
plt.ylabel('x(t)  ')
plt.title('Impulse time')
plt.plot(y,n)

plt.show()