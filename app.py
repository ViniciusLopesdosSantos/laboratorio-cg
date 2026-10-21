import streamlit as st

st.title("Laboratório de Computação Gráfica")

st.write("Meu primeiro aplicativo com Streamlit!")

nome = st.text_input("Digite seu nome:")

if st.button("Enviar"):
    st.success(f"Olá, {nome}! Seja bem-vindo!")