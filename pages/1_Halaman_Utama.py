import streamlit as st
import os

st.set_page_config(page_title="Pantun Kelok", layout="wide")

st.title("📖 Pantun Kelok")
st.header("📜 Selamat Datang ke Pantun Kelok")
st.write("Aplikasi ini membolehkan anda mencari pantun dari buku *Pantun Kelok* dengan mudah.")

# Gambar buku (dari folder `data/`)
COVER_IMAGE_PATH = "data/cover_pantun_kelok.jpg"
if os.path.exists(COVER_IMAGE_PATH):
    st.image(COVER_IMAGE_PATH, caption="Beli Buku untuk Akses Penuh", width=300)
else:
    st.warning("⚠ Gambar tidak ditemui dalam folder `data/`. Pastikan fail bernama `cover_pantun_kelok.jpg`.")

st.write("📌 Untuk akses penuh, dapatkan QR Kod dalam buku.")

# Butang Navigasi
if st.button("🔎 Cari Pantun Sekarang"):
    st.switch_page("pages/2_Cari_Pantun.py")

if st.button("🔑 Pergi ke Akses QR Kod"):
    st.switch_page("pages/3_Akses_QR_Kod.py")
