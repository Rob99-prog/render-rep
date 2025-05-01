"""
Streamlit app para lanzar una moneda n veces y mostrar resultados.
"""

import random
from collections import Counter

import streamlit as st

st.header("Lanzar una moneda")

# Slider (key única)
n = st.slider(
    "¿Cuántas veces lanzar la moneda?", 1, 1000, 10, key="num_lanzamientos_slider"
)

# Inicializa session_state
if "resultados" not in st.session_state:
    st.session_state.resultados = []

# Botón (key única)
if st.button("¡Lanzar!", key="btn_lanzar"):
    st.session_state.resultados = [
        "Cara" if random.random() < 0.5 else "Cruz" for _ in range(n)
    ]

# Si hay resultados, muéstralos
if st.session_state.resultados:
    conteo = Counter(st.session_state.resultados)
    st.write(f"Resultados de {len(st.session_state.resultados)} lanzamientos:")
    st.bar_chart(conteo)

    # Checkbox (key única)
    if st.checkbox("Ver tabla de resultados", key="chk_tabla"):
        st.table([{"Resultado": r} for r in st.session_state.resultados])
else:
    st.write("Aún sin lanzamientos.")
