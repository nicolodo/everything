
import matplotlib.pyplot as plt

# part 2 do 5000 cube numbers

# setup values
x_values = list(range(1,5001))
y_values = [x**2 for x in x_values]

# setup and style output 
plt.scatter(x_values,y_values)

# plot onto a window
plt.show()







