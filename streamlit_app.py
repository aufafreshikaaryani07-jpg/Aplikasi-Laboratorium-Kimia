import streamlit as st
import math

# =====================================================
# DATABASE ALAT LAB
# =====================================================

alat_lab = [

    "Alu",
    "Batang Pengaduk",
    "Beaker Glass",
    "Botol Reagen",
    "Botol Timbang",
    "Botol Semprot",
    "Buret",
    "Bunsen",
    "Cawan Petri",
    "Corong Kaca",
    "Cawan Porselen",
    "Corong Pisah",
    "Desikator",
    "Erlenmeyer",
    "Gelas Ukur",
    "Gegep Besi",
    "Gegep Kayu",
    "Hot Plate",
    "Inkubator",
    "Jarum Ose",
    "Kaca Arloji",
    "Kaki Tiga",
    "Kasa Asbes",
    "Kertas Saring",
    "Klem Buret",
    "Kuvet",
    "Labu Alas Bulat",
    "Labu Takar",
    "Laminar Air Flow",
    "Mikropipet",
    "Mortar",
    "Mekker",
    "Neraca Analitik",
    "Oven",
    "pH meter",
    "Pipet Volume",
    "Pipet Tetes",
    "Pipet Mohr",
    "Piknometer",
    "Polismen",
    "Rak Tabung Reaksi",
    "Sentrifus",
    "Segitiga Porselen",
    "Spatula",
    "Spektrofotometer",
    "Statif",
    "Spirtus",
    "Soxhlet",
    "Tabung Reaksi",
    "Tanur",
    "Tutup Kaca",
    "Termometer",
    "Vortex",
    "Water bath"
]

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

</style>
""", unsafe_allow_html=True)

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
st.write("")

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
<div style="
background:linear-gradient(135deg,#001845,#023e8a,#0077b6);
padding:25px;
border-radius:20px;
color:white;
text-align:center;
margin-top:10px;
margin-bottom:20px;
">

<h2>🧪 Welcome to Smart Lab Chemistry</h2>

<p style="font-size:17px;">
Selamat menggunakan aplikasi laboratorium kimia yang dirancang untuk membantu
mahasiswa, praktikan, dan peneliti dalam melakukan perhitungan serta pencarian
alat laboratorium secara cepat, mudah, dan akurat.
</p>

<p>
Gunakan menu di sebelah kiri untuk mengakses seluruh fitur laboratorium
</p>

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

# =====================================================
# MENU CEK ALAT
# =====================================================

if menu == "Cek Stok Alat Laboratorium":

    st.header("CEK STOK ALAT LABORATORIUM")

    cari = st.text_input("Cari alat apa?")

    if st.button("Cek Alat"):

        if cari.title() in alat_lab:
            st.success(f"Alat '{cari}' TERSEDIA di laboratorium")

        else:
            st.error(f"Alat '{cari}' TIDAK DITEMUKAN")

    if st.checkbox("Tampilkan Semua Alat"):
        for alat in alat_lab:
            st.write("-", alat)

# =====================================================
# MENU MOLARITAS
# =====================================================

elif menu == "Kalkulator Molaritas":

    st.header("KALKULATOR MOLARITAS")

    mol = st.number_input("Masukkan jumlah mol (mol):", min_value=0.0)
    volume = st.number_input("Masukkan volume larutan (L):", min_value=0.0001)

    if st.button("Hitung Molaritas"):

        hasil = mol / volume

        st.success(f"Molaritas = {round(hasil, 3)} M")

# =====================================================
# MENU PENGENCERAN
# =====================================================

elif menu == "Kalkulator Pengenceran":

    st.header("KALKULATOR PENGENCERAN")

    M1 = st.number_input("Masukkan M1 (M):", min_value=0.0)
    V1 = st.number_input("Masukkan V1 (mL):", min_value=0.0)
    M2 = st.number_input("Masukkan M2 (M):", min_value=0.0001)

    if st.button("Hitung Pengenceran"):

        V2 = (M1 * V1) / M2

        st.success(f"V2 = {round(V2, 2)} mL")

# =====================================================
# MENU KADAR
# =====================================================

elif menu == "Kalkulator Kadar":

    pilihan = st.selectbox(
        "Pilih Jenis Kadar",
        [
            "Kadar Asam Asetat",
            "NaOH dan Na2CO3 (Warder)",
            "Kadar Besi(Fe)",
            "Kadar Klorida(Cl) Iodometri",
            "Kadar Klorida(Cl) Argentometri",
            "Kesadahan Air"
        ]
    )

    # =====================================================
    # KADAR ASAM ASETAT
    # =====================================================

    if pilihan == "Kadar Asam Asetat":

        V = st.number_input("Volume titrasi/V(mL)")
        N = st.number_input("Normalitas/N(mgrek/mL)")
        FP = st.number_input("Faktor pengenceran")
        V_sampel = st.number_input("Volume sampel (mL)")

        if st.button("Hitung Kadar"):

            hasil = ((V * N * 60) * (10**-3) * FP * 100) / V_sampel

            st.success(f"Kadar CH3COOH = {round(hasil,2)} %")

    # =====================================================
    # WARDER
    # =====================================================

    elif pilihan == "NaOH dan Na2CO3 (Warder)":

        a = st.number_input("Volume titrasi 1/a(mL)")
        b = st.number_input("Volume titrasi 2/b(mL)")
        N = st.number_input("Normalitas/N(mgrek/mL)")
        V_sampel = st.number_input("Volume sampel (mL)")

        if st.button("Hitung Kadar"):

            BE_NaOH = 40
            BE_Na2CO3 = 53

            Na2CO3 = ((2 * (b-a)* N * BE_Na2CO3) * (10**-3) * 100) / V_sampel
            NaOH = ((2*a - b)* N * BE_NaOH) * (10**-3) * 100 / V_sampel

            st.success(f"Kadar NaOH = {round(NaOH,2)} %")
            st.success(f"Kadar Na2CO3 = {round(Na2CO3,2)} %")

    # =====================================================
    # BESI
    # =====================================================

    elif pilihan == "Kadar Besi(Fe)":

        V = st.number_input("Volume titrasi/V(mL)")
        N = st.number_input("Normalitas/N(mgrek/mL)")
        V_sampel = st.number_input("Volume sampel (mL)")

        if st.button("Hitung Kadar"):

            hasil = ((V * N * 56) * (10**-3) * 100) / V_sampel

            st.success(f"Kadar Fe = {round(hasil,2)} %")

    # =====================================================
    # IODOMETRI
    # =====================================================

    elif pilihan == "Kadar Klorida(Cl) Iodometri":

        V = st.number_input("Volume titrasi/V(mL)")
        N = st.number_input("Normalitas/N(mgrek/mL)")
        V_sampel = st.number_input("Volume sampel (mL)")

        if st.button("Hitung Kadar"):

            hasil = ((V * N * 17.75) * (10**-3) * 100/5 * 100) / V_sampel

            st.success(f"Kadar Cl = {round(hasil,2)} %")

    # =====================================================
    # ARGENTOMETRI
    # =====================================================

    elif pilihan == "Kadar Klorida(Cl) Argentometri":

        V = st.number_input("Volume titrasi/V(mL)")
        N = st.number_input("Normalitas/N(mgrek/mL)")
        V_sampel = st.number_input("Volume sampel (mL)")

        if st.button("Hitung Kadar"):

            hasil = ((V * N * 35.5) * (10**-3) * 100) / V_sampel

            st.success(f"Kadar Cl = {round(hasil,2)} %")

    # =====================================================
    # KESADAHAN
    # =====================================================

    elif pilihan == "Kesadahan Air":

        V = st.number_input("Volume titrasi/V(mL)")
        M = st.number_input("Molaritas/M(mmol/mL)")
        V_sampel = st.number_input("Volume sampel (L)")

        if st.button("Hitung Kadar"):

            hasil = ((V * M * 100)) / V_sampel

            st.success(f"Kadar CaCO3 = {round(hasil,2)} %")

# =====================================================
# MENU pH
# =====================================================

elif menu == "Kalkulator pH":

    st.header("KALKULATOR pH")

    h = st.number_input("Masukkan konsentrasi H+ (mol/L):", min_value=0.0000001)

    if st.button("Hitung pH"):

        hasil = -math.log10(h)

        st.success(f"pH = {round(hasil,2)}")
