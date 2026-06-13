import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("RAW_recipes.csv")

top = df["n_ingredients"].value_counts().head(10)

plt.bar(top.index, top.values)

plt.title("Ingredient Distribution")

plt.xlabel("Number of Ingredients")

plt.ylabel("Recipes")

plt.savefig("graph.png")

print("Graph Saved Successfully")

