import streamlit as st
import math
import random

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="Smart Lab Chemistry",
    page_icon="🧪",
    layout="wide"
)

# =====================================================
# SESSION STATE (RIWAYAT)
# =====================================================

if "history" not in st.session_state:
    st.session_state.history = []

# =====================================================
# STYLE + EFFECT
# =====================================================

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
    position:relative;
    overflow:hidden;
}

/* efek animasi */
.bubble{
    position:absolute;
    border-radius:50%;
    background:rgba(255,255,255,0.2);
    animation: float 10s infinite;
}

@keyframes float{
    0%{transform:translateY(0);}
    50%{transform:translateY(-30px);}
    100%{transform:translateY(0);}
}

.card{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.1);
    text-align:center;
}

.info-box{
    background:white;
    padding:20px;
    border-radius:15px;
    margin-top:10px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
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

</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

menu = st.sidebar.selectbox(
    "MENU UTAMA",
    [
        "Home",
        "Cek Stok Alat Laboratorium",
        "Kalkulator Molaritas",
        "Kalkulator Pengenceran",
        "Kalkulator Kadar",
        "Kalkulator pH",
        "Riwayat Perhitungan"
    ]
)

# =====================================================
# HOME
# =====================================================

if menu == "Home":

    st.markdown("""
    <div class="hero">
        <div class="bubble" style="width:60px;height:60px;top:10px;left:10px;"></div>
        <div class="bubble" style="width:40px;height:40px;top:80px;right:20px;"></div>
        <h1>🧪 MOLEVIA</h1>
        <h3>The Pathway Through Chemistry</h3>
        <p>Platform laboratorium digital modern</p>
    </div>
    """, unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1579165466741-7f35e4755660",
        use_container_width=True
    )

    st.markdown("""
    <div class="info-box">
    <h4>👨‍🔬 Creator</h4>
    <p>
    Politeknik AKA Bogor <br>
    Kelompok 12_1D <br><br>
    Aufa Freshika Aryani (2560588)<br>
    Aura Halimah Natanegoro (2560589)<br>
    Ayu Asyfa Mei Asyhari (2560593)<br>
    Oscar Tirta Sugema (2560735)
    </p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# DATA ALAT + DESKRIPSI
# =====================================================

alat_detail = {
    "Beaker Glass": ("Wadah mencampur larutan", "https://images.unsplash.com/photo-1581091870622-3c5f0fbc5b75"),
    "Erlenmeyer": ("Wadah reaksi & titrasi", "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b"),
    "Buret": ("Untuk titrasi presisi", "https://images.unsplash.com/photo-1603126857599-f6e157fa2fe6"),
    "Pipet Tetes": ("Memindahkan cairan", "https://images.unsplash.com/photo-1582719478171-2c3d2d5c1d1d"),
    "Labu Takar": ("Menyiapkan larutan volume tepat", "https://images.unsplash.com/photo-1581092335878-9c1d0c3b1d2f"),
    "Gelas Ukur": ("Mengukur volume", "https://images.unsplash.com/photo-1582719478147-9c2d2c9f1c2c"),
    "pH meter": ("Mengukur pH", "https://images.unsplash.com/photo-1581093588401-22b6d9d2b9c2")
}

# =====================================================
# CEK ALAT
# =====================================================

if menu == "Cek Stok Alat Laboratorium":

    st.header("🔬 CEK STOK ALAT LAB")

    cari = st.text_input("Cari alat")

    if st.button("Cek"):

        if cari in alat_detail:
            st.success("Alat tersedia")
            fungsi, img = alat_detail[cari]
            st.image(img)
            st.info(f"Fungsi: {fungsi}")
        else:
            st.error("Tidak ditemukan")

# =====================================================
# MOLARITAS
# =====================================================

elif menu == "Kalkulator Molaritas":

    st.header("🧮 KALKULATOR MOLARITAS")

    st.markdown("""
    <div class="info-box">
    M = n / V <br>
    Satuan: mol/L
    </div>
    """, unsafe_allow_html=True)

    mol = st.number_input("Mol")
    vol = st.number_input("Volume (L)", min_value=0.0001)

    if st.button("Hitung"):

        hasil = mol/vol
        st.success(f"{round(hasil,3)} M")

        st.session_state.history.append(f"Molaritas = {hasil}")

# =====================================================
# PENGENCERAN
# =====================================================

elif menu == "Kalkulator Pengenceran":

    st.header("🧪 KALKULATOR PENGENCERAN")

    st.markdown("""
    <div class="info-box">
    M1V1 = M2V2
    </div>
    """, unsafe_allow_html=True)

    M1 = st.number_input("M1")
    V1 = st.number_input("V1")
    M2 = st.number_input("M2", min_value=0.0001)

    if st.button("Hitung"):

        V2 = (M1*V1)/M2
        st.success(f"V2 = {round(V2,2)}")

        st.session_state.history.append(f"Pengenceran V2 = {V2}")

# =====================================================
# pH
# =====================================================

elif menu == "Kalkulator pH":

    st.header("⚗️ KALKULATOR pH")

    st.markdown("""
    <div class="info-box">
    pH = -log [H+]
    </div>
    """, unsafe_allow_html=True)

    h = st.text_input("Input H+")

    if st.button("Hitung"):

        try:
            if "^" in h:
                base, exp = h.split("^")
                h_val = 10**float(exp)
            else:
                h_val = float(h)

            ph = -math.log10(h_val)
            st.success(f"pH = {round(ph,2)}")

            st.session_state.history.append(f"pH = {ph}")

        except:
            st.error("Format salah")

    st.warning("⚠️ Keterbatasan: hanya untuk larutan kuat sederhana")

# =====================================================
# RIWAYAT
# =====================================================

elif menu == "Riwayat Perhitungan":

    st.header("📜 RIWAYAT")

    if st.session_state.history:
        for item in st.session_state.history[::-1]:
            st.write(item)
    else:
        st.info("Belum ada data")
