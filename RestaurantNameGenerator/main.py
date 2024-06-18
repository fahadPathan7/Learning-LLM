# external imports
import streamlit as st
import warnings

# internal imports
import langchain_helper

# ignore deprecation warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

# setting title
st.title("Restaurant Name Generator")

# sidebar to select cuisine type
cuisine = st.sidebar.selectbox("pick a cuisine",
                               ("Bangladeshi", "Indian", "Italian",
                                "Arabian", "Pakistani", "Chinese", "Lebanese"))

# generate restaurant name and menu items
if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Suggested Menu Items**")
    for item in menu_items:
        st.write("-", item)
