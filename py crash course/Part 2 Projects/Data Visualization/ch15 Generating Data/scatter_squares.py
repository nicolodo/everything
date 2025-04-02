
import matplotlib.pyplot as plt

# style output
plt.scatter(2, 4, s=200) # s is the size of the dots
plt.title('Square numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Squares of value', fontsize=14)

# Set size of tick labels
plt.tick_params('both', which='major', labelsize=14)

plt.show()




