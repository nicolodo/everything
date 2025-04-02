
import matplotlib.pyplot as plt

# values
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

# style output
plt.scatter(x_values, y_values, s=200) # s is the size of the dots
plt.title('Square numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Squares of value', fontsize=14)

# Set size of tick labels
plt.tick_params('both', which='major', labelsize=14)

# Set range of tick axis
plt.axis([0,1100, 0, 1100000])

plt.show()




