import streamlit as st

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
    exec(open("app.py").read())
