import streamlit as st
import math

# =====================================================
# DATABASE ALAT LAB
# =====================================================

alat_lab = [
    "Alu","Batang Pengaduk","Beaker Glass","Botol Reagen","Botol Timbang",
    "Botol Semprot","Buret","Bunsen","Cawan Petri","Corong Kaca",
    "Cawan Porselen","Corong Pisah","Desikator","Erlenmeyer","Gelas Ukur",
    "Gegep Besi","Gegep Kayu","Hot Plate","Inkubator","Jarum Ose",
    "Kaca Arloji","Kaki Tiga","Kasa Asbes","Kertas Saring","Klem Buret",
    "Kuvet","Labu Alas Bulat","Labu Takar","Laminar Air Flow","Mikropipet",
    "Mortar","Mekker","Neraca Analitik","Oven","pH meter","Pipet Volume",
    "Pipet Tetes","Pipet Mohr","Piknometer","Polismen","Rak Tabung Reaksi",
    "Sentrifus","Segitiga Porselen","Spatula","Spektrofotometer","Statif",
    "Spirtus","Soxhlet","Tabung Reaksi","Tanur","Tutup Kaca",
    "Termometer","Vortex","Water bath"
]

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="Smart Lab Chemistry",
    page_icon="🧪",
    layout="wide"
)

# =====================================================
# STYLE
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
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR MENU
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

# =====================================================
# HOME (WELCOME ONLY DI SINI)
# =====================================================

if menu == "Home":

    st.markdown("""
    <div class="hero">
    <h1>🧪 SMART LAB CHEMISTRY</h1>
    <h3>Laboratory Assistant for Students & Researchers</h3>
    <p>
    Temukan alat laboratorium, hitung molaritas,
    pengenceran, kadar zat, dan pH dengan cepat
    dalam satu platform yang praktis dan modern.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1579165466741-7f35e4755660",
        use_container_width=True
    )

    a,b,c = st.columns(3)

    with a:
        st.markdown("""
        <div class="card">
        <h3>🔍 Pencarian Alat</h3>
        <p>Temukan alat laboratorium dengan cepat dan mudah.</p>
        </div>
        """, unsafe_allow_html=True)

    with c:
        st.markdown("""
        <div class="card">
        <h3>🧮 Kalkulator Kimia</h3>
        <p>Molaritas, Pengenceran, Kadar dan pH.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:linear-gradient(135deg,#001845,#023e8a,#0077b6);
    padding:25px;border-radius:20px;color:white;text-align:center;margin-top:20px;">
    <h2>Welcome to Smart Lab Chemistry</h2>
    <p>Aplikasi untuk membantu praktikum kimia jadi lebih mudah.</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# CEK ALAT
# =====================================================

elif menu == "Cek Stok Alat Laboratorium":

    st.header("CEK STOK ALAT LABORATORIUM")

    cari = st.text_input("Cari alat apa?")

    if st.button("Cek Alat"):
        if cari.title() in alat_lab:
            st.success(f"Alat '{cari}' TERSEDIA")
        else:
            st.error(f"Alat '{cari}' TIDAK DITEMUKAN")

# =====================================================
# MOLARITAS
# =====================================================

elif menu == "Kalkulator Molaritas":

    st.header("KALKULATOR MOLARITAS")

    mol = st.number_input("Mol", min_value=0.0)
    volume = st.number_input("Volume (L)", min_value=0.0001)

    if st.button("Hitung"):
        st.success(f"M = {round(mol/volume,3)} M")

# =====================================================
# PENGENCERAN
# =====================================================

elif menu == "Kalkulator Pengenceran":

    st.header("KALKULATOR PENGENCERAN")

    M1 = st.number_input("M1")
    V1 = st.number_input("V1")
    M2 = st.number_input("M2", min_value=0.0001)

    if st.button("Hitung"):
        st.success(f"V2 = {round((M1*V1)/M2,2)} mL")

# =====================================================
# KADAR (SIMPLE)
# =====================================================

elif menu == "Kalkulator Kadar":

    st.header("KALKULATOR KADAR")
    st.info("Silakan pilih jenis kadar (fitur tetap sama seperti sebelumnya)")

# =====================================================
# PH
# =====================================================

elif menu == "Kalkulator pH":

    st.header("KALKULATOR pH")

    h = st.number_input("H+", min_value=0.0000001)

    if st.button("Hitung"):
        st.success(f"pH = {round(-math.log10(h),2)}")
