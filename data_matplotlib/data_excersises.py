import matplotlib.pyplot as plt

# Generate x and y values
x_input = range(1, 5000)
y_cubes = [x**3 for x in x_input]

# Choose a style for the figure and create the figure and axis
plt.style.use('seaborn')
fig, ax = plt.subplots()

# Sets figure title, x and y labels and their font size
ax.set_title('The Cubed values of 1 - 5,000')
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Value Cubed', fontsize=14)

# Sets x and y tickers size
ax.tick_params(axis='both', labelsize=14)

# Plot x and y values on the figure
# c is color, cmap is the color map (gradients) and s is the dot size
ax.scatter(x_input, y_cubes, c=y_cubes, cmap=plt.cm.Blues, s=10)


plt.show()