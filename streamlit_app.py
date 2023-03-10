import streamlit


streamlit.title("My Parents New Healthy Menu")
streamlit.subheader("Breakfast Menu")
streamlit.write("🥣 Omega 3 and Blueberry Oatmeal \n")
streamlit.write("🥗 Kale, Spinach & Rocket Smoothie \n")
streamlit.write("🐔 Hard-Boild Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast\n")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)) 

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries']) 
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page  
streamlit.dataframe(fruits_to_show)
