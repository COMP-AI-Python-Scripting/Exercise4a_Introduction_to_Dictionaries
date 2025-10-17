from lolviz import objviz

inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"],
}

# Visualisation of dictionary
# c = objviz(inventory)
# c.view(cleanup=True, quiet=True)

print(f"Before:\n {inventory}")

inventory["pocket"] = ["seashell", "strange berry", "lint"]
inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
inventory["gold"] = inventory["gold"] + 50

print(f"After:\n {inventory}")

# # Visualisation of dictionary
c = objviz(inventory)
c.view(cleanup=True, quiet=True)
