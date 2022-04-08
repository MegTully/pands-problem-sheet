#This program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] 
# on the one set of axes.

#import packages to plot functions
import numpy as np
import matplotlib.pyplot as plt

#Create an array of x values and y values equal to the x values in the range[0,4]
xs = np.array(range(0,4))
ys= xs

#Plot xs and ys with label, linewidth and colour [1] [3] [4]
plt.plot(xs,ys,label = "f(x) = x", linewidth = '5', color = "m") # m = colour magenta
#label x-axis
plt.xlabel("x-Axis")
#label y-axis
plt.ylabel("y-Axis")
#add a legend to graph
plt.legend()
#Display graph
plt.show()

#Create 2 new arrays for x and y values of function g(x)= x^2
x2s = np.array(range(0,4))
#x^2
y2s= xs*xs

#Plot the graph this time with markers [1] [2] 
plt.plot(x2s,y2s,label = "$g(x) = x^2$", linewidth = '2', color = "c", marker = '*', mec = "k") # c = colour cyan, k= black
plt.xlabel("x-Axis")
plt.ylabel("$y-Axis (x^2)$")
plt.legend()
plt.show()

#Create 2 new arrays for x and y of the function h(x)=x^3
x3s = np.array(range(0,4))
#x^3
y3s= xs**3

#plot a scatter plot with yellow dots [5]
plt.scatter(x3s,y3s,label = "$h(x) = x^3$", color = "yellow") # y = colour yellow
plt.xlabel("x-Axis")
plt.ylabel("$y-Axis (x^3)$")
plt.legend()
plt.show()

#[1] https://www.w3schools.com/python/matplotlib_plotting.asp
#[2] https://www.w3schools.com/python/matplotlib_markers.asp
#[3] https://www.w3schools.com/python/matplotlib_line.asp
#[4] https://www.w3schools.com/python/matplotlib_labels.asp
#[5] https://www.w3schools.com/python/matplotlib_scatter.asp
