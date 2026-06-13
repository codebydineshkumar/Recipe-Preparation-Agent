import streamlit as st
import pandas as pd

df = pd.read_csv("RAW_recipes.csv")

st.title("Smart Recipe Preparation Agent")
st.markdown("""
### AI Powered Recipe Recommendation System

Enter available ingredients and get recipe suggestions instantly.
""")

ingredient = st.text_input("Enter Ingredient")

if ingredient:

    result = df[
        df["ingredients"]
        .astype(str)
        .str.contains(ingredient, case=False, na=False)
    ]


    st.success(f"{len(result)} recipes found")
    st.write(result[["name"]].head(5))

    if not result.empty:

        selected = result.iloc[0]

        st.subheader("Recipe Name")
        st.write(selected["name"])

        st.subheader("Ingredients")
        st.write(selected["ingredients"])

        st.subheader("Steps")
        st.write(selected["steps"])