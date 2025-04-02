
import matplotlib.pyplot as plt

# values
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# style output
plt.scatter(x_values, y_values, s=200) # s is the size of the dots
plt.title('Square numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Squares of value', fontsize=14)

# Set size of tick labels
plt.tick_params('both', which='major', labelsize=14)

plt.show()




