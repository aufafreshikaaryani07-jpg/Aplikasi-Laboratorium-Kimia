import streamlit as st
import math
import random

# =====================================================
# SMART LAB CHEMISTRY LANDING PAGE
# =====================================================

st.set_page_config(
    page_title="Smart Lab Chemistry",
    page_icon="🧪",
    layout="wide"
)

# SESSION STATE (RIWAYAT)
if "history" not in st.session_state:
    st.session_state.history = []

st.markdown("""
<style>  

.main{  
    background: linear-gradient(135deg,#f8fbff,#edf6ff);  
}  

[data-testid="stSidebar"]{  
    background: linear-gradient(180deg,#001845,#023e8a,#0077b6);  
}  

[data-testid="stSidebar"] *{  
    color:white;  
}  

.hero{  
    background: linear-gradient(135deg,#001845,#023e8a,#00b4d8);  
    padding:50px;  
    border-radius:30px;  
    text-align:center;  
    color:white;  
    margin-bottom:25px;  
    box-shadow:0px 12px 30px rgba(0,0,0,0.2);  
}  

.card{  
    background:white;  
    padding:20px;  
    border-radius:20px;  
    box-shadow:0px 4px 15px rgba(0,0,0,0.1);  
    text-align:center;  
}  

.stButton > button{  
    width:100%;  
    height:50px;  
    border:none;  
    border-radius:12px;  
    background:#0077b6;  
    color:white;  
    font-size:16px;  
}  

.stButton > button:hover{  
    background:#0096c7;  
}  

.snow{
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
pointer-events:none;
z-index:9999;
}

</style>
""", unsafe_allow_html=True)

# efek animasi
st.markdown("""
<div class="snow">
✨ ❄️ 🧪 ⚗️ ✨ ❄️ 🧪 ⚗️ ✨ ❄️ 🧪 ⚗️
</div>
""", unsafe_allow_html=True)

st.divider()

menu = st.sidebar.selectbox(
    "MENU UTAMA",
    [
        "Home",
        "Cek Stok Alat Laboratorium",
        "Kalkulator Molaritas",
        "Kalkulator Pengenceran",
        "Kalkulator Kadar",
        "Kalkulator pH"
    ]
)

# CREATOR
st.sidebar.markdown("---")
st.sidebar.markdown("""
**Creator By :**  
Kelompok 12_1D_Politeknik AKA Bogor  
Aufa Freshika Aryani (2560588)  
Aura Halimah Natanegoro (2560589)  
Ayu Asyfa Mei Asyhari (2560593)  
Oscar Tirta Sugema (2560735)
""")

# =====================================================
# HOME
# =====================================================
if menu == "Home":

    st.markdown("""
    <div class="hero">
    <h1>🧪 MOLEVIA</h1>
    <h3>The Pathway Through Chemistry</h3>
    <p>Platform laboratorium digital modern</p>
    </div>
    """, unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1579165466741-7f35e4755660",
        use_container_width=True
    )

# =====================================================
# DATABASE ALAT + FUNGSI
# =====================================================
alat_info = {
"Beaker Glass":"Wadah mencampur larutan",
"Buret":"Untuk titrasi",
"Erlenmeyer":"Wadah reaksi",
"pH meter":"Mengukur pH",
"Mikropipet":"Mengambil volume kecil",
"Hot Plate":"Memanaskan larutan",
"Spektrofotometer":"Analisis absorbansi",
"Tabung Reaksi":"Reaksi skala kecil"
}

# =====================================================
# CEK ALAT
# =====================================================
elif menu == "Cek Stok Alat Laboratorium":

    st.markdown("## 📦 CEK STOK ALAT LAB")

    cari = st.text_input("Cari alat")

    if st.button("Cek"):
        if cari in alat_info:
            st.success("Tersedia")
            st.image("https://images.unsplash.com/photo-1581091870627-3d3b4e6d0c5f")
            st.info(alat_info[cari])

            st.session_state.history.append(f"Cek alat: {cari}")

        else:
            st.error("Tidak ditemukan")

# =====================================================
# MOLARITAS
# =====================================================
elif menu == "Kalkulator Molaritas":

    st.markdown("## 🧮 KALKULATOR MOLARITAS")

    st.info("M = n / V")

    mol = st.number_input("Mol")
    vol = st.number_input("Volume")

    if st.button("Hitung"):
        hasil = mol/vol
        st.success(hasil)
        st.session_state.history.append(f"Molaritas = {hasil}")

# =====================================================
# PENGENCERAN
# =====================================================
elif menu == "Kalkulator Pengenceran":

    st.markdown("## 🧪 KALKULATOR PENGENCERAN")

    st.info("M1V1 = M2V2")

    M1 = st.number_input("M1")
    V1 = st.number_input("V1")
    M2 = st.number_input("M2")

    if st.button("Hitung"):
        V2 = (M1*V1)/M2
        st.success(V2)
        st.session_state.history.append(f"Pengenceran = {V2}")

# =====================================================
# KADAR
# =====================================================
elif menu == "Kalkulator Kadar":

    st.markdown("## ⚗️ KALKULATOR KADAR")

    st.info("Menghitung kadar zat dalam larutan")

# =====================================================
# PH
# =====================================================
elif menu == "Kalkulator pH":

    st.markdown("## 🧪 KALKULATOR pH")

    st.warning("Catatan: hanya untuk larutan sederhana (tidak buffer)")

    h = st.number_input("H+")

    if st.button("Hitung"):
        ph = -math.log10(h)
        st.success(ph)
        st.session_state.history.append(f"pH = {ph}")

# =====================================================
# RIWAYAT
# =====================================================
st.sidebar.markdown("### 🕒 Riwayat")

for item in st.session_state.history[-5:]:
    st.sidebar.write(item)
