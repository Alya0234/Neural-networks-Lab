import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

plt.plot(x, y)
plt.title("Simple Line Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.savefig("line_graph.png")
plt.close()

labels = ["A", "B", "C", "D"]
values = [10, 20, 15, 25]

plt.bar(labels, values)
plt.title("Bar Graph")
plt.savefig("bar_graph.png")
plt.close()