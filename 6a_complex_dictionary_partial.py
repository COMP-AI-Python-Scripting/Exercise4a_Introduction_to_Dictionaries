import matplotlib.pyplot as plt

fruitplot = {
    # Dictionary items here
    # Delete and replace with code
    # Delete and replace with code
    # Delete and replace with code
}

# Get a figure object
fig = plt.figure()
# Get an axis object for plotting
ax = fig.add_subplot()

# List comprehension to go here for title case
fruit_types = [# Replace with list comprehension]
fruit_data = # Get the integer values

ax.bar(fruit_types, fruit_data)
ax.set_xlabel(fruitplot["x_label"].title())
ax.set_ylabel(fruitplot["y_label"].title())
ax.set_title(fruitplot["plot_title"].title())

plt.savefig("fruit_histogram.png")

plt.show()
