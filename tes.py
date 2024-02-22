import streamlit as st

st.title("HITUNG LUAS PERSEGI PANJANG")
panjang = st.number_input("Masukkan Nilai Panjang", 0)
lebar = st.slider ("Tentukan Nilai Lebar", 0, 100, 1, 1)
hitung = st.button("Hitung Luas")

   
if hitung :
    luas = panjang * lebar
    st.success (f"Luas Persegi Panjang = {luas}")
