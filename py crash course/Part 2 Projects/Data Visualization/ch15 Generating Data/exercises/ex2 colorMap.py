
import matplotlib.pyplot as plt

# ex 2 apply color map

# setup values
x_values = list(range(1,5001))
y_values = [x**2 for x in x_values]

# setup and style output 
plt.scatter(x_values, y_values, c=y_values)
# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds)

# plot onto a window
plt.show()







