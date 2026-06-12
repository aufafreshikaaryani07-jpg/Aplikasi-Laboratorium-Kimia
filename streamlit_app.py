import streamlit as st
import math

# =====================================================
# SESSION STATE (RIWAYAT)
# =====================================================
if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

def simpan_riwayat(teks):
    st.session_state.riwayat.append(teks)

# =====================================================
# SMART LAB CHEMISTRY LANDING PAGE
# =====================================================

st.set_page_config(
page_title="Smart Lab Chemistry",
page_icon="🧪",
layout="wide"
)

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
    background: linear-gradient(  
    135deg,  
    #001845,  
    #023e8a,  
    #00b4d8);  
    padding:50px;  
    border-radius:30px;  
    text-align:center;  
    color:white;  
    margin-bottom:25px;  
    box-shadow:0px 12px 30px rgba(0,0,0,0.2);  
}  

.hero h1{  
    font-size:58px;  
    margin-bottom:10px;  
}  

.hero h3{  
    color:#caf0f8;  
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

</style>  """, unsafe_allow_html=True)

st.divider()

# =====================================================
# SIDEBAR MENU + RIWAYAT
# =====================================================
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

st.sidebar.markdown("### 📜 Riwayat")
if st.session_state.riwayat:
    for item in st.session_state.riwayat[-10:][::-1]:
        st.sidebar.write("•", item)
else:
    st.sidebar.write("Belum ada data")

# =====================================================
# HOME
# =====================================================
if menu == "Home":

    st.snow()
    st.balloons()

    st.markdown("""  
    <div class="hero">  
    <h1>🧪 MOLEVIA</h1>  
    <h3>The Pathway Through Chemistry</h3>  
    <p>  
    Molevia hadir sebagai platform laboratorium digital yang mengintegrasikan perhitungan kimia  
    dan manajemen inventaris dalam satu aplikasi yang sederhana, cepat, dan akurat.  
    </p>  
    </div>  
    """, unsafe_allow_html=True)  

    st.image(
        "https://images.unsplash.com/photo-1579165466741-7f35e4755660",
        use_container_width=True
    )

# =====================================================
# DATABASE ALAT LAB
# =====================================================
alat_lab = ["Beaker Glass","Erlenmeyer","Buret","Pipet Volume","Tabung Reaksi"]

fungsi_alat = {
    "Beaker Glass": "Menampung dan mencampur larutan",
    "Erlenmeyer": "Wadah reaksi dan titrasi",
    "Buret": "Mengukur volume titrasi",
    "Pipet Volume": "Mengambil volume akurat",
    "Tabung Reaksi": "Reaksi skala kecil"
}

# =====================================================
# MENU CEK ALAT
# =====================================================
if menu == "Cek Stok Alat Laboratorium":

    st.header("CEK STOK ALAT LABORATORIUM")

    for alat in alat_lab:
        st.markdown(f"### {alat}")
        st.image(f"https://source.unsplash.com/400x300/?lab,{alat}")
        st.write("Fungsi:", fungsi_alat.get(alat,"Alat laboratorium"))
        st.markdown("---")

# =====================================================
# INFO BOX
# =====================================================
def info_box(judul, isi):
    st.markdown(f"""
    <div style="background:white;padding:15px;border-radius:10px;margin-bottom:10px;">
    <h3>{judul}</h3>
    <p>{isi}</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# MOLARITAS
# =====================================================
elif menu == "Kalkulator Molaritas":

    info_box("Kalkulator Molaritas","Rumus: M = n / V (mol/L)")

    mol = st.number_input("Mol")
    volume = st.number_input("Volume (L)",min_value=0.0001)

    if st.button("Hitung Molaritas"):
        hasil = mol/volume
        st.success(f"M = {round(hasil,3)}")
        simpan_riwayat(f"Molaritas {round(hasil,3)}")

# =====================================================
# PENGENCERAN
# =====================================================
elif menu == "Kalkulator Pengenceran":

    info_box("Pengenceran","Rumus: M1V1 = M2V2")

    M1 = st.number_input("M1")
    V1 = st.number_input("V1")
    M2 = st.number_input("M2",min_value=0.0001)

    if st.button("Hitung Pengenceran"):
        V2 = (M1*V1)/M2
        st.success(f"V2 = {round(V2,2)}")
        simpan_riwayat(f"Pengenceran {round(V2,2)}")

# =====================================================
# PH
# =====================================================
elif menu == "Kalkulator pH":

    info_box("pH","Rumus: pH = -log [H+]")

    st.warning("⚠️ Hanya untuk larutan sederhana")

    h = st.number_input("Konsentrasi H+",min_value=0.0000001)

    if st.button("Hitung pH"):
        ph = -math.log10(h)
        st.success(f"pH = {round(ph,2)}")
        simpan_riwayat(f"pH {round(ph,2)}")

# =====================================================
# CREATOR
# =====================================================
st.markdown("""
---
### 👨‍🔬 Creator
Politeknik AKA Bogor  
Kelompok 12_1D  

Aufa Freshika Aryani (2560588)  
Aura Halimah Natanegoro (2560589)  
Ayu Asyfa Mei Asyhari (2560593)  
Oscar Tirta Sugema (2560735)
""")
