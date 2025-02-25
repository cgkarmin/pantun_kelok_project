import streamlit as st
import pandas as pd
import os

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="Pantun Kelok", layout="wide")

# --- Simpan status halaman dalam sesi Streamlit ---
if "halaman" not in st.session_state:
    st.session_state["halaman"] = "utama"

# --- Halaman Utama ---
def halaman_utama():
    st.title("📖 Pantun Kelok")
    st.header("📜 Selamat Datang ke Pantun Kelok")
    st.write("Aplikasi ini membolehkan anda mencari pantun dari buku *Pantun Kelok* dengan mudah.")

    # Gambar buku
    COVER_IMAGE_PATH = "data/cover_pantun_kelok.jpg"
    if os.path.exists(COVER_IMAGE_PATH):
        st.image(COVER_IMAGE_PATH, caption="Beli Buku untuk Akses Penuh", width=300)
    else:
        st.warning("⚠ Gambar tidak ditemui dalam folder `data/`. Pastikan fail bernama `cover_pantun_kelok.jpg`.")

    st.write("📌 Untuk akses penuh, dapatkan QR Kod dalam buku.")

    # Butang Navigasi
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔎 Cari Pantun Sekarang"):
            st.session_state["halaman"] = "cari_pantun"
            st.rerun()

    with col2:
        if st.button("🔑 Pergi ke Akses QR Kod"):
            st.session_state["halaman"] = "akses_qr"
            st.rerun()

# --- Halaman Carian Pantun ---
def halaman_cari_pantun():
    st.title("🔎 Cari Pantun Kelok")
    
    DATA_DIR = "data"
    NAMA_FILE_CSV = os.path.join(DATA_DIR, "pantun_kelok.csv")

    # Baca data pantun
    def muat_data_pantun(namafile):
        try:
            df = pd.read_csv(namafile)
            return df
        except FileNotFoundError:
            return pd.DataFrame(columns=["pemantun", "tajuk_pantun", "teks_pantun", "muka_surat"])

    df_pantun = muat_data_pantun(NAMA_FILE_CSV)

    if not df_pantun.empty:
        pemantun_pilihan = st.selectbox("Pilih Pemantun:", df_pantun["pemantun"].unique())

        pantun_pemantun = df_pantun[df_pantun["pemantun"] == pemantun_pilihan]

        for index, row in pantun_pemantun.iterrows():
            with st.expander(f"{row['tajuk_pantun']} (M/S {row['muka_surat']})"):
                st.write(row["teks_pantun"])
                st.button(f"📖 Buka Muka Surat {row['muka_surat']} dalam PDF", key=f"pdf_{index}")
    else:
        st.warning("⚠ Tiada data pantun tersedia. Sila pastikan fail `pantun_kelok.csv` mengandungi data.")

    # Butang kembali ke Halaman Utama
    if st.button("⬅ Kembali ke Halaman Utama"):
        st.session_state["halaman"] = "utama"
        st.rerun()

# --- Halaman QR Kod ---
def halaman_akses_qr():
    st.title("🔑 Akses Eksklusif QR Kod")
    qr_input = st.text_input("Masukkan QR Kod:")

    if qr_input:
        if qr_input == "KODRAHSIA123":  # Contoh kod akses
            st.success("✅ Akses berjaya! Anda boleh membaca semua pantun.")
        else:
            st.error("❌ Kod tidak sah. Sila cuba lagi.")

    # Butang kembali ke Halaman Utama
    if st.button("⬅ Kembali ke Halaman Utama"):
        st.session_state["halaman"] = "utama"
        st.rerun()

# --- Pemilihan Halaman ---
if st.session_state["halaman"] == "utama":
    halaman_utama()
elif st.session_state["halaman"] == "cari_pantun":
    halaman_cari_pantun()
elif st.session_state["halaman"] == "akses_qr":
    halaman_akses_qr()
