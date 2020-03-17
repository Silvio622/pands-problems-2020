# Silvio Dunst
# Plotting

import numpy as np # Import numpy library as variable np
import matplotlib.pyplot as plt # Import matplotlib libarary and use pyplot function as variable plt

x = np.linspace(0, 4, 48) # x axis start value 0 and end value 4 with 48 x values in between
# f(x) = x
f = x * 1 # f is the linear function of x

# g(x) = x² # type in 2 after x, select 2, press Alt key and Number pad 0178 to get squared of a variable
g = x **2 # g is the squared function x

# h(x) = x³ # type in 3 after x, select 3, press Alt key and Number pad 0179 to get squared of a variable
h = x **3 # h is the qubed function x


plt.plot(x, f, 'b.', label = "Linear Function of x") # plot the scatter linear function in blue color and label "Linear Function of x"
plt.plot(x, g, 'g.', label = "Squared Function of x²") # plot the scatter squared function in green color and label "Squared Function of x²"
plt.plot(x, h, 'r.', label = "Qubed Function of x³") # plot the scatter qubed function in red color and label "Squared Function of x³"
plt.legend() # show legend on the plot
# the legend is upper center , anchored center of the plot, legend has one label per line, the box has a shadow, the legend title, facecolr gray in hex
plt.legend(loc="upper center", bbox_to_anchor = [0.5,1], ncol = 1, shadow = True, title = "Legend", fancybox = True, facecolor = '#D8D8D8')
plt.title("Plot Functions") # show Title on the plot
plt.xlabel("X Axis", fontsize = 10, color = 'red') # show x axis label in fontsize 10 and red color
plt.ylabel("Y Axis", fontsize = 16, color = 'blue', rotation = 0) # show y axis label in fontsize 16 and blue color rotation of 0 degree
plt.savefig("Plotting.png") # save the file in the same root folder


