import streamlit as st
import math

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
# HOME
# =====================================================

if menu == "Home":

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

    h_input = st.text_input(
        "Masukkan konsentrasi H+ (contoh: 10^-4 atau 0.0001)"
    )

    if st.button("Hitung pH"):

        try:
            # Ubah koma jadi titik (format Indonesia)
            h_input = h_input.replace(",", ".")

            # Support format 10^-4
            if "^" in h_input:
                base, exp = h_input.split("^")
                if base.strip() == "10":
                    h = 10 ** float(exp)
                else:
                    h = float(h_input)
            else:
                h = float(h_input)

            # Validasi
            if h <= 0:
                st.error("Konsentrasi H+ harus lebih dari 0!")
            else:
                hasil = -math.log10(h)
                ph = round(hasil, 2)

                # Batasi skala pH
                if ph < 0:
                    ph = 0
                elif ph > 14:
                    ph = 14

                # Klasifikasi
                if ph < 1:
                    sifat = "Asam Sangat Kuat"
                elif ph < 3:
                    sifat = "Asam Kuat"
                elif ph < 6:
                    sifat = "Asam Lemah"
                elif ph == 7:
                    sifat = "Netral"
                elif ph <= 9:
                    sifat = "Basa Lemah"
                elif ph <= 12:
                    sifat = "Basa Kuat"
                else:
                    sifat = "Basa Sangat Kuat"

                # Output warna
                if ph < 7:
                    st.error(f"pH = {ph} ({sifat})")
                elif ph == 7:
                    st.info(f"pH = {ph} ({sifat})")
                else:
                    st.success(f"pH = {ph} ({sifat})")

        except:
            st.error("Masukkan angka yang valid! (contoh: 10^-4 atau 0.0001)")
# =====================================================
# TAMBAHAN FITUR GLOBAL
# =====================================================

# ================= RIWAYAT =================
if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

def tambah_riwayat(data):
    st.session_state.riwayat.append(data)

st.sidebar.markdown("---")
st.sidebar.subheader("📜 Riwayat Perhitungan")

if st.session_state.riwayat:
    for r in reversed(st.session_state.riwayat[-10:]):
        st.sidebar.write("•", r)
else:
    st.sidebar.write("Belum ada riwayat")

# =====================================================
# TAMBAHAN CREATOR (FOOTER GLOBAL)
# =====================================================
st.markdown("""
---
### 👨‍🔬 Creator
**Politeknik AKA Bogor**  
**Kelompok 12_1D**

- Aufa Freshika Aryani (2560588)  
- Aura Halimah Natanegoro (2560589)  
- Ayu Asyfa Mei Asyhari (2560593)  
- Oscar Tirta Sugema (2560735)  
""")

# =====================================================
# TAMBAHAN HOME EFFECT
# =====================================================
if menu == "Home":
    st.markdown("""
    <style>
    body {
        background-image: url("https://www.transparenttextures.com/patterns/cubes.png");
    }
    </style>
    """, unsafe_allow_html=True)

    st.balloons()

# =====================================================
# TAMBAHAN DESKRIPSI KALKULATOR
# =====================================================

def info_kalkulator(judul, isi):
    st.markdown(f"""
    <div style="
    background:#ffffff;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.1);
    margin-bottom:15px;">
    <h3>{judul}</h3>
    <p>{isi}</p>
    </div>
    """, unsafe_allow_html=True)

if menu == "Kalkulator Molaritas":
    info_kalkulator(
        "Pengertian Molaritas",
        "Molaritas adalah jumlah mol zat terlarut dalam 1 liter larutan.<br><b>Rumus:</b> M = n / V<br><b>Satuan:</b> mol/L"
    )

if menu == "Kalkulator Pengenceran":
    info_kalkulator(
        "Pengertian Pengenceran",
        "Pengenceran digunakan untuk mengurangi konsentrasi larutan.<br><b>Rumus:</b> M1V1 = M2V2<br><b>Satuan:</b> M (mol/L), V (mL)"
    )

if menu == "Kalkulator Kadar":
    info_kalkulator(
        "Pengertian Kadar",
        "Kadar adalah persentase kandungan zat dalam suatu sampel.<br><b>Satuan:</b> % (persen)"
    )

if menu == "Kalkulator pH":
    info_kalkulator(
        "Pengertian pH",
        "pH adalah ukuran tingkat keasaman larutan.<br><b>Rumus:</b> pH = -log[H+]<br><b>Rentang:</b> 0 - 14"
    )

# =====================================================
# TAMBAHAN CATATAN pH
# =====================================================
if menu == "Kalkulator pH":
    st.warning("""
    ⚠️ Keterbatasan:
    - Hanya untuk larutan sederhana
    - Tidak mendukung buffer kompleks
    - Tidak menghitung suhu
    """)

# =====================================================
# TAMBAHAN STOK ALAT (GAMBAR + FUNGSI)
# =====================================================
fungsi_alat = {alat: "Fungsi umum alat laboratorium kimia" for alat in alat_lab}

gambar_alat = {
    alat: "https://source.unsplash.com/400x300/?laboratory," + alat.replace(" ", "")
    for alat in alat_lab
}

if menu == "Cek Stok Alat Laboratorium":
    st.markdown("## 🔬 Daftar Alat Laboratorium Lengkap")

    for alat in alat_lab:
        st.markdown(f"### {alat}")
        st.image(gambar_alat[alat])
        st.write("Fungsi:", fungsi_alat[alat])
        st.markdown("---")

# =====================================================
# TAMBAHAN RIWAYAT PER MENU
# =====================================================

# Molaritas
if menu == "Kalkulator Molaritas":
    if st.button("Hitung Molaritas"):
        hasil = mol / volume
        tambah_riwayat(f"Molaritas: {round(hasil,3)} M")

# Pengenceran
if menu == "Kalkulator Pengenceran":
    if st.button("Hitung Pengenceran"):
        V2 = (M1 * V1) / M2
        tambah_riwayat(f"Pengenceran: V2={round(V2,2)} mL")

# pH
if menu == "Kalkulator pH":
    if st.button("Hitung pH"):
        try:
            tambah_riwayat(f"pH dihitung dari input: {h_input}")
        except:
            pass

# =====================================================
# TAMBAHAN HEADER PUTIH SETIAP MENU
# =====================================================
if menu != "Home":
    st.markdown(f"""
    <div style="
    background:white;
    padding:15px;
    border-radius:10px;
    margin-bottom:10px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.1);">
    <h2>{menu}</h2>
    </div>
    """, unsafe_allow_html=True)
