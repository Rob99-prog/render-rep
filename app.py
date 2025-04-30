import streamlit as st
import random
import pandas as pd

st.header('Lanzar una moneda')


n = st.slider('¿Cuántas veces lanzar la moneda?', min_value=1, max_value=1000, value=10)


if 'resultados' not in st.session_state:
    st.session_state.resultados = []


if st.button('¡Lanzar!'):
    st.session_state.resultados = [
        'Cara' if random.random() < 0.5 else 'Cruz'
        for _ in range(n)
    ]


if st.session_state.resultados:
    conteo = pd.Series(st.session_state.resultados).value_counts()
    st.write(f"Resultados de {len(st.session_state.resultados)} lanzamientos:")
    st.bar_chart(conteo)


    if st.checkbox('Ver tabla de resultados'):
        st.table(pd.DataFrame({'Resultado': st.session_state.resultados}))
else:
    st.write('Aún sin lanzamientos.')
