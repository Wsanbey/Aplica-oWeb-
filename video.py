import streamlit as st

st.sidebar.title("Menu")
paginaSelecionada = st.sidebar.selectbox("Selecione a página", ["Opção 1", "Opção 2"])

if paginaSelecionada == "Opção 1":
    st.title("Video exemplo")
    st.selectbox("Selecione a página", ["Opção 1", "Opção 2"])
elif paginaSelecionada == "Opção 2":
    st.title("Você esta na pagina 2")
