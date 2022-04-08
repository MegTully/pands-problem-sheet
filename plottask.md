# Task08: Write a program that displays a plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0, 4] on the one set of axes. 
## Author: Megan Tully

## Plot One: f(x)=x
After importing the necessary packages numpy as np and matplotlib.pyplot as plt,two arrays of x values and y values were created. The array of x values was called "xs" and they ranged from 0 to 4 which doesnt include 4. The array of y values was created and set equal to the xs and called "ys" because f(x)=x i.e y=x. The plt.plot function was used to plot the xs and ys where the label was set as f(x)=x, the linewidth was set to 5 and the colour was set to magenta. This resulted in a nice thick pinky purple straight diagonal line. The x-axis and y-axis were also labelled. The .legend function creates a legend in the top left hand corner of the graph. The function plt.show displays the graph.

## Plot Two: g(x)=x^2
For this graph the array of x values was called "x2s" and they ranged from 0 to 4 again. The array of y values was created and set equal to the (x2s)^2 and called "y2s" because g(x)=x^2. The plt.plot function was used to plot the x2s and y2s where the label was set as g(x)=x^2, the linewidth was set to 2, the colour was set to cyan and a marker was set to the shape of a star and its colour (mec) was set to k which is black. A marker is a symbol that marks where the graph changes shape. This resulted in a nice blue line marked with black stars where the shape of the graph changed. The x-axis and y-axis were also labelled. The .legend function creates a legend in the top left hand corner of the graph.

## Plot Three: h(x)=x^3
For this graph the array of x values was called "x3s" and they ranged from 0 to 4. The array of y values was created and set equal to the (x3s)^3 and called "y3s" because h(x)=x^3. The plt.scatter function was used to plot the x3s and y3s on a scatter plot where the label was set as h(x)=x^3 and the colour of the dots was set to yellow. This resulted in a scatter plot with yellow dots representing all the points. The x-axis and y-axis were also labelled. The .legend function creates a legend in the top left hand corner of the graph. The function plt.show displays the graph.


