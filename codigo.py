import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.title('Mi primera barra lateral de Streamlit')
st.sidebar.header('¡Hola, Barra Lateral!')
st.sidebar.write('Esto es una barra lateral')
st.sidebar.image('FUSHIBOOL.PNG')
if st.sidebar.button('Haz clic pero en la barra lateral'):
    st.sidebar.write('¡Has hecho clic en el boton de la barra lateral!')
user_input = st.sidebar.text_input('Escribe algo en la barra:')
st.sidebar.write('Escribe en la barra:', user_input)
