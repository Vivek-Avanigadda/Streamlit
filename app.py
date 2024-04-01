import streamlit as st 
from keras import load_model
st.title("Streamlit App")
st.header("Welcome to Streamlit!")
# Show a simple text element
st.write("This is a simple text element.")
st.file_uploader('',type==['jpg', 'png','jpeg'])
model = load_model('C:/Users/vivek/Downloads/model1.h5')
classes=[0,1]
