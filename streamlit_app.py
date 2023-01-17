import streamlit
import pandas



streamlit.title("My Parents New Healthy Menu")
streamlit.subheader("Breakfast Menu")
streamlit.write("🥣 Omega 3 and Blueberry Oatmeal \n")
streamlit.write("🥗 Kale, Spinach & Rocket Smoothie \n")
streamlit.write("🐔 Hard-Boild Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast\n")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
