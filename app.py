import streamlit as st
import random
import string

st.title("Generador de Contraseñas Seguras Online")

longitud = st.slider("Elegí la longitud", 4, 30, 10)

if st.button("Generar contraseña"):

    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation

    todos = letras + numeros + simbolos

    contraseña = ''.join(random.choice(todos) for i in range(longitud))

    st.success(f"Tu contraseña es: {contraseña}")
