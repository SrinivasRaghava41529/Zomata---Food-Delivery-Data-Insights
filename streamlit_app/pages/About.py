import streamlit as st
from PIL import Image

image = Image.open("src\zomato-1738850455.jpeg") 
st.image(image, caption="Zomato - Your food discovery and delivery partner", use_column_width=True)

st.title("About Zomato")


st.write("""
Zomato is a leading global restaurant discovery and food delivery platform. 
Founded in 2008, it provides a comprehensive range of services, including restaurant 
reviews, menus, photos, and online food ordering. Zomato operates in multiple countries 
and helps users make informed decisions about where to dine or order from based on their preferences.

With a user-friendly mobile app and website, Zomato aims to bridge the gap between restaurants 
and food lovers by providing seamless experiences.
""")
