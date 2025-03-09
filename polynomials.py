import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
x = []
y = []
print("This program finds roots and graphs simple quadratic equations")
A = int(input("Enter first constant"))
B = int(input("Enter second constant"))
C = int(input("Enter third constant"))
if(B*B - 4*A*C <0):
    print("There is no real number roots")
else:
    r1 = (-B + np.sqrt(B*B - 4*A*C))/(2*A)
    r2 = (-B - np.sqrt(B*B - 4*A*C))/(2*A)
    print("The roots are", r1 , "and", r2)
low = int(input("Enter the lowest number of visible x values you want to see"))
high = int(input("Enter the highest number of visible x values you want to see"))
per = int(input("Enter the number of points between integers you want plotted"))
while(low != (high+1)):
    if(per == 0):
        x.append(low)
        z = A*low*low + B*low +C
        y.append(z)
        low += 1
    else:
        x.append(low)
        z = A*low*low + B*low +C
        y.append(z)
        low = low + ((10/(per+1))/10)
ax.axvline(x = 0, color= 'k')
ax.axhline(y = 0, color= 'k')
ax.plot(x,y)
plt.show()

