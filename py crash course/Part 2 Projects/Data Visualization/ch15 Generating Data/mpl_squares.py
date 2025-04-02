
import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
# customising the graph
plt.plot(squares, linewidth=5)

# set chart title and label axes
plt.title('square numbers', fontsize=24)
plt.xlabel('value',fontsize=14)
plt.ylabel('Square of value', fontsize=14)

# set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()



