import streamlit as st
import math

# =====================================================
# SESSION STATE (RIWAYAT)
# =====================================================
if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

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
.hero::after{
content:"⚗️ 🧪 ⚛️ 🧬";
position:absolute;
bottom:10px;
right:20px;
font-size:30px;
opacity:0.3;
}

.card{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.1);
    text-align:center;
}

.info{
    background:white;
    padding:15px;
    border-radius:15px;
    margin-top:10px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.1);
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

st.divider()

menu = st.sidebar.selectbox(
    "MENU UTAMA",
    [
        "Home",
        "Cek Stok Alat Laboratorium",
        "Kalkulator Molaritas",
        "Kalkulator Pengenceran",
        "Kalkulator Kadar",
        "Kalkulator pH",
        "Riwayat"
    ]
)

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

    # CREATOR
    st.markdown("""
    <div class="info">
    <b>Creator:</b><br>
    Politeknik AKA Bogor<br>
    Kelompok 12_1D<br><br>
    Aufa Freshika Aryani (2560588)<br>
    Aura Halimah Natanegoro (2560589)<br>
    Ayu Asyfa Mei Asyhari (2560593)<br>
    Oscar Tirta Sugema (2560735)
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# DATABASE ALAT + FUNGSI
# =====================================================

alat_info = {
"Beaker Glass":"Wadah mencampur larutan",
"Erlenmeyer":"Wadah titrasi",
"Buret":"Alat titrasi presisi",
"pH meter":"Mengukur pH",
"Pipet Tetes":"Memindahkan cairan",
"Gelas Ukur":"Mengukur volume"
}

# =====================================================
# MENU CEK ALAT
# =====================================================

if menu == "Cek Stok Alat Laboratorium":

    st.header("CEK STOK ALAT LABORATORIUM")

    cari = st.text_input("Cari alat apa?")

    if st.button("Cek Alat"):

        if cari.title() in alat_info:
            st.success(f"Alat '{cari}' TERSEDIA")
            st.info(alat_info[cari.title()])
            st.image("https://images.unsplash.com/photo-1582719478250-c89cae4dc85b")

            st.session_state.riwayat.append(f"Cek alat: {cari}")

        else:
            st.error(f"Alat '{cari}' TIDAK DITEMUKAN")

# =====================================================
# MENU MOLARITAS
# =====================================================

elif menu == "Kalkulator Molaritas":

    st.header("KALKULATOR MOLARITAS")

    st.markdown("""
    <div class="info">
    Rumus: M = n / V <br>
    Satuan: mol/L
    </div>
    """, unsafe_allow_html=True)

    mol = st.number_input("Mol")
    volume = st.number_input("Volume (L)", min_value=0.0001)

    if st.button("Hitung Molaritas"):

        hasil = mol / volume
        st.success(f"Molaritas = {round(hasil, 3)} M")

        st.session_state.riwayat.append(f"Molaritas = {hasil}")

# =====================================================
# MENU PENGENCERAN
# =====================================================

elif menu == "Kalkulator Pengenceran":

    st.header("KALKULATOR PENGENCERAN")

    st.markdown("""
    <div class="info">
    Rumus: M1V1 = M2V2
    </div>
    """, unsafe_allow_html=True)

    M1 = st.number_input("M1")
    V1 = st.number_input("V1")
    M2 = st.number_input("M2", min_value=0.0001)

    if st.button("Hitung"):

        V2 = (M1*V1)/M2
        st.success(f"V2 = {round(V2,2)}")

        st.session_state.riwayat.append(f"Pengenceran V2 = {V2}")

# =====================================================
# MENU pH
# =====================================================

elif menu == "Kalkulator pH":

    st.header("KALKULATOR pH")

    st.markdown("""
    <div class="info">
    Rumus: pH = -log [H+]
    </div>
    """, unsafe_allow_html=True)

    h_input = st.text_input("Masukkan H+")

    if st.button("Hitung pH"):

        try:
            if "^" in h_input:
                base, exp = h_input.split("^")
                h = 10**float(exp)
            else:
                h = float(h_input)

            ph = -math.log10(h)
            st.success(f"pH = {round(ph,2)}")

            st.session_state.riwayat.append(f"pH = {ph}")

        except:
            st.error("Input salah")

    st.warning("⚠️ Keterbatasan: hanya larutan sederhana (tidak buffer/kuat-lemah campuran)")

# =====================================================
# RIWAYAT
# =====================================================

elif menu == "Riwayat":

    st.header("RIWAYAT PENGGUNA")

    if st.session_state.riwayat:
        for r in reversed(st.session_state.riwayat):
            st.write("-", r)
    else:
        st.info("Belum ada riwayat")
