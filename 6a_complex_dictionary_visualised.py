import matplotlib.pyplot as plt
from lolviz import objviz

fruitplot = {
    "plot_title": "fruit sales",
    "x_label": "fruit",
    "y_label": "unit sales",
    "data": {"apples": 10, "oranges": 15, "bananas": 5, "grapes": 20},
}

# Visualisation of dictionary
c = objviz(fruitplot)
c.view(cleanup=True, quiet=True)

fig = plt.figure()
ax = fig.add_subplot()

fruit_types = [f.title() for f in fruitplot["data"].keys()]
fruit_data = fruitplot["data"].values()
ax.bar(fruit_types, fruit_data)
ax.set_xlabel(fruitplot["x_label"].title())
ax.set_ylabel(fruitplot["y_label"].title())
ax.set_title(fruitplot["plot_title"].title())

plt.savefig("fruit_histogram.png")

plt.show()
