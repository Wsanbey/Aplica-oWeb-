import streamlit as st

st.title('Video exemplo')
st.selectbox('Selecione uma Opção',['Opção 1', 'Opção 2'])

st.sidebar.title('Menu')
paginaSelecionada = st.sidebar.selectbox('Selecione a página',['Opção 1', 'Opção 2'])

if paginaSelecionada == 'Página 1':
    st.title('Video exemplo')
    st.selectbox('Selecione uma Opção',['Opção 1', 'Opção 2'])
elif paginaSelecionada == 'Opção 2':
    st.title('Você esta na pagina 2')