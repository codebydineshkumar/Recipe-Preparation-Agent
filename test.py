# import pandas as pd

# df = pd.read_csv("RAW_recipes.csv")

# print(df.head())
# print(df.columns)
# print(df.shape)


# column check
# import pandas as pd

# df = pd.read_csv("RAW_recipes.csv")

# print(df[['name','ingredients','steps']].head())



#Recipes search test 
import pandas as pd

df = pd.read_csv("RAW_recipes.csv")

ingredient = "potato"

result = df[
    df["ingredients"]
    .astype(str)
    .str.contains(ingredient, case=False, na=False)
]

print(result[["name"]].head(10))