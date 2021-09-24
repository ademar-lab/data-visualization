import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
values = [x+1 for x in range(len(squares))]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize =24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis="both", which="major", labelsize=14)
plt.show()