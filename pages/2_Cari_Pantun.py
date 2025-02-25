import streamlit as st
import pandas as pd
import os

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

# Dropdown untuk memilih pemantun
if not df_pantun.empty:
    pemantun_pilihan = st.selectbox("Pilih Pemantun:", df_pantun["pemantun"].unique())

    # Senarai pantun berdasarkan pemantun dipilih
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
    exec(open("app.py").read())
