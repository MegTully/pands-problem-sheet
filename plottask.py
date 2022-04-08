#This program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] 
# on the one set of axes.

#import packages to plot functions
import numpy as np
import matplotlib.pyplot as plt

#Create an array of x values and y values equal to the x values in the range[0,4]
xs = np.array(range(0,4))
ys= xs

plt.plot(xs,ys,label = "f(x) = x", linewidth = '5', color = "m") # m = colour magenta
plt.xlabel("x-Axis")
plt.ylabel("y-Axis")
plt.legend()
plt.show()

x2s = np.array(range(0,4))
y2s= xs*xs

plt.plot(x2s,y2s,label = "$g(x) = x^2$", linewidth = '2', color = "c", marker = '*', mec = "k") # c = colour cyan
plt.xlabel("x-Axis")
plt.ylabel("$y-Axis (x^2)$")
plt.legend()
plt.show()

x3s = np.array(range(0,4))
y3s= xs**3

plt.scatter(x3s,y3s,label = "$h(x) = x^3$", color = "yellow") # y = colour yellow
plt.xlabel("x-Axis")
plt.ylabel("$y-Axis (x^3)$")
plt.legend()
plt.show()

