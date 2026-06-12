import streamlit as st
import math

# =====================================================
# SMART LAB CHEMISTRY LANDING PAGE & CONFIG
# =====================================================
st.set_page_config(
    page_title="Smart Lab Chemistry",
    page_icon="🧪",
    layout="wide"
)

# Inisialisasi Session State untuk Riwayat agar tidak hilang saat navigasi menu
if "riwayat_pencarian" not in st.session_state:
    st.session_state.riwayat_pencarian = []

st.markdown("""
<style>    
.main{    
    background: linear-gradient(135deg,#f8fbff,#edf6ff);    
}    
[data-testid="stSidebar"]{    
    background: linear-gradient(180deg,#001845,#023e8a,#0077b6);    
}    
/* Mengatur teks menu utama di sidebar agar tetap putih */
[data-testid="stSidebar"] p, [data-testid="stSidebar"] label {    
    color: white !important;    
}    
/* Memperbaiki teks di dalam selectbox/dropdown agar tidak putih kosong saat diklik */
div[data-baseweb="select"] * {
    color: #333333 !important;
}
.hero{    
    background: linear-gradient(135deg, #001845, #023e8a, #00b4d8);    
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
    color: #333333;
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
/* Box Penjelasan Khusus di dalam Sidebar (Latar Biru/Gelap) */
.penjelasan-sidebar {
    background: rgba(255, 255, 255, 0.1);
    padding: 15px;
    border-radius: 12px;
    border-left: 4px solid #00b4d8;
    margin-top: 20px;
    color: #caf0f8 !important;
    font-size: 13px;
    line-height: 1.5;
}
.penjelasan-sidebar strong {
    color: #ffffff !important;
}
</style>  
""", unsafe_allow_html=True)  

st.divider()

# Menu Utama di Sidebar
menu = st.sidebar.selectbox(
    "MENU UTAMA",
    [
        "Home",
        "Cek Stok Alat Laboratorium",
        "Kalkulator Molaritas",
        "Kalkulator Pengenceran",
        "Kalkulator Kadar",
        "Kalkulator pH",
        "Riwayat",
        "Creator"
    ]
)

# =====================================================
# MENAMPILKAN PENGERTIAN & RUMUS DI SIDEBAR
# =====================================================
if menu == "Kalkulator Molaritas":
    st.sidebar.markdown("""
    <div class="penjelasan-sidebar">
        <strong>📚 Pengertian:</strong><br>
        Digunakan untuk menghitung konsentrasi larutan secara otomatis berdasarkan jumlah mol dan volume larutan.<br><br>
        <strong>🧪 Rumus Kimia:</strong>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.latex(r"M = \frac{n}{V}")
    st.sidebar.markdown("""
    <div class="penjelasan-sidebar" style="margin-top:0px; border-left:none; background:transparent; padding-top:0px;">
        <strong>Unit Satuan:</strong><br>
        • M: Molaritas (mol/L)<br>
        • n: Jumlah mol (mol)<br>
        • V: Volume larutan (L)
    </div>
    """, unsafe_allow_html=True)

elif menu == "Kalkulator Pengenceran":
    st.sidebar.markdown("""
    <div class="penjelasan-sidebar">
        <strong>📚 Pengertian:</strong><br>
        Digunakan untuk menghitung volume larutan akhir setelah proses penambahan pelarut murni tanpa mengubah massa zat terlarut.<br><br>
        <strong>🧪 Rumus Kimia:</strong>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.latex(r"M_1 \times V_1 = M_2 \times V_2")
    st.sidebar.markdown("""
    <div class="penjelasan-sidebar" style="margin-top:0px; border-left:none; background:transparent; padding-top:0px;">
        <strong>Unit Satuan:</strong><br>
        • M1 / M2: Molaritas awal dan akhir (M)<br>
        • V1 / V2: Volume awal dan akhir (mL)
    </div>
    """, unsafe_allow_html=True)

elif menu == "Kalkulator Kadar":
    st.sidebar.markdown("""
    <div class="penjelasan-sidebar">
        <strong>📚 Pengertian:</strong><br>
        Digunakan untuk mengukur persentase kandungan fraksi zat analit tertentu di dalam sampel melalui teknik volumetri.<br><br>
        <strong>🧪 Rumus Kadar Umum:</strong>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.latex(r"\% \text{Kadar} = \frac{(V \times N \times BE) \times 10^{-3} \times FP \times 100}{V_{\text{sampel}}}")

elif menu == "Kalkulator pH":
    st.sidebar.markdown("""
    <div class="penjelasan-sidebar">
        <strong>📚 Pengertian:</strong><br>
        Digunakan untuk mendeteksi derajat kekuatan keasaman zat senyawa cair berbasis aktivitas konsentrasi logaritma ion hidrogen.<br><br>
        <strong>🧪 Rumus Kimia:</strong>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.latex(r"\text{pH} = -\log_{10}[H^+]")


# =====================================================
# DATABASE INVENTARIS ALAT LAB (A-Z & LINK KELOMPOK)
# =====================================================
database_alat = {
    "Alu dan Mortar": {"fungsi": "Menghancurkan atau menghaluskan sampel padat laboratorium.", "stok": 15, "img": "https://share.google/yRNFVgSD5DqKpzZ3K"},
    "Batang Pengaduk": {"fungsi": "Mengaduk larutan kimia agar komponen zat terlarut dapat tercampur homogen.", "stok": 40, "img": "https://share.google/xUk3ly8duN0GSorzL"},
    "Beaker Glass": {"fungsi": "Wadah penampung, pengaduk, pencampur, dan pemanas cairan kimia.", "stok": 60, "img": "https://share.google/2DZ3pffUitLDJOsvN"},
    "Botol Reagen": {"fungsi": "Tempat penyimpanan larutan reagen kimia agar terhindar dari kontaminasi udara luar.", "stok": 35, "img": "https://share.google/WXokxGJHpuEmkp1up"},
    "Botol Semprot": {"fungsi": "Menyimpan akuades yang digunakan untuk membersihkan atau membilas sisa larutan.", "stok": 25, "img": "https://share.google/vBz01z8WE4Ssz7o3P"},
    "Botol Timbang": {"fungsi": "Menimbang zat padat atau sampel cair yang bersifat higroskopis.", "stok": 20, "img": "https://share.google/fUwisDQn8bkpmsOpI"},
    "Bunsen": {"fungsi": "Alat pemanas lab dengan sistem pembakaran gas untuk sterilisasi dan pemanasan zat.", "stok": 15, "img": "https://share.google/uJg5JEaafaKsYciM3"},
    "Buret": {"fungsi": "Mengeluarkan larutan dengan volume spesifik dan akurat pada analisis titrasi.", "stok": 30, "img": "https://share.google/HnTF6gOKZEWdiArTc"},
    "Cawan Petri": {"fungsi": "Wadah sirkular jernih untuk membiakkan media mikroorganisme dan bakteri.", "stok": 50, "img": "https://share.google/PdgCkAzXbcDdCVnJl"},
    "Cawan Porselen": {"fungsi": "Mereaksikan atau menguapkan larutan pada suhu tinggi di atas kaki tiga.", "stok": 25, "img": "https://share.google/CEpSh37pfcJw3GzpQ"},
    "Corong Kaca": {"fungsi": "Mempermudah pemindahan cairan ke wadah bermulut kecil dan menopang kertas saring.", "stok": 30, "img": "https://share.google/0KxE58ph9HxmfMHU6"},
    "Corong Pisah": {"fungsi": "Memisahkan komponen fraksi dari dua cairan fase berbeda berdasarkan berat jenis.", "stok": 10, "img": "https://share.google/gOiMWNpHDNmbcMJ8s"},
    "Desikator": {"fungsi": "Menjaging kelembapan dan mengeringkan sampel padat yang sensitif terhadap air.", "stok": 6, "img": "https://share.google/jIfFmySQlBTUBqppq"},
    "Erlenmeyer": {"fungsi": "Wadah mencampur larutan analit, menampung hasil titrasi, dan memanaskan cairan.", "stok": 55, "img": "https://share.google/OQya3oXlUy6921atC"},
    "Gelas Ukur": {"fungsi": "Mengukur volume larutan kimia secara makro dengan kepatuhan akurasi menengah.", "stok": 45, "img": "https://share.google/ac7hZoZ1bafRLkflz"},
    "Gegep Besi": {"fungsi": "Menjepit buret, labu alas bulat, atau peralatan gelas lain pada tiang statif.", "stok": 25, "img": "https://share.google/docXEUUhkWTuUIFYe"},
    "Gegep Kayu": {"fungsi": "Menjepit tabung reaksi ketika dalam proses pemanasan di atas api.", "stok": 30, "img": "https://share.google/BAzgJifuk6xWiAOQX"},
    "Hot Plate": {"fungsi": "Alat elektronik pemanas datar sekaligus mengaduk sampel secara otomatis.", "stok": 8, "img": "https://share.google/Sm7MQ20rL57J6QZSl"},
    "Inkubator": {"fungsi": "Menginkubasi kultur sel mikrobiologi pada kondisi suhu konstan.", "stok": 4, "img": "https://share.google/yrMpR0a5VpAaIdRs6"},
    "Jarum Ose": {"fungsi": "Mengambil mikroba atau melakukan inokulasi bakteri secara aseptik.", "stok": 20, "img": "https://share.google/rKbISgQkSwXmai2gi"},
    "Kaca Arloji": {"fungsi": "Wadah penimbangan sampel kristal padat atau penutup gelas beaker.", "stok": 35, "img": "https://share.google/LCvh5RTGWNo4xRLwA"},
    "Kaki Tiga": {"fungsi": "Penyangga besi melingkar tiga kaki untuk menopang wadah sampel saat pemanasan.", "stok": 20, "img": "https://share.google/qv2Y7wukJsdJI64pM"},
    "Kasa Asbes": {"fungsi": "Meratakan rambatan panas api dari bunsen agar wadah kaca tidak pecah.", "stok": 25, "img": "https://share.google/6UitwF3WuamArD8s6"},
    "Kertas Saring": {"fungsi": "Menyaring partikel residu padatan terlarut dari cairan filtrat.", "stok": 100, "img": "https://share.google/r4TMYTqYpP4iW9CsD"},
    "Labu Takar": {"fungsi": "Membuat larutan standar primer atau sekunder dengan ketelitian volume sangat tinggi.", "stok": 35, "img": "https://share.google/1ub7VwA2v5HWYyfuw"},
    "Mikropipet": {"fungsi": "Memindahkan cairan bervolume ultra kecil (skala mikroliter) secara akurat.", "stok": 12, "img": "https://share.google/aYcHRDGhgb5ejp8g1"},
    "Neraca Analitik": {"fungsi": "Mengukur berat massa substansi kimia berpresisi mikro tinggi.", "stok": 6, "img": "https://share.google/eak1JwX1Nuz8aKvpK"},
    "Oven Laboratorium": {"fungsi": "Mengeringkan peralatan gelas pasca cuci atau menghilangkan kadar air sampel.", "stok": 4, "img": "https://share.google/U6kVqBUo4gKgqcq5Q"},
    "pH meter": {"fungsi": "Mengukur nilai derajat keasaman atau nilai konsentrasi ion hidrogen secara digital.", "stok": 10, "img": "https://share.google/NBsYiRCehqnsrOqBd"},
    "Pipet Mohr": {"fungsi": "Mengambil larutan dengan rentang volume bervariasi sesuai garis tanda skala.", "stok": 30, "img": "https://share.google/SoX9AzQ0FhW6QQLwN"},
    "Pipet Tetes": {"fungsi": "Memindahkan cairan reagen dalam volume sangat kecil secara tetes demi tetes.", "stok": 80, "img": "https://share.google/oHmP2DVLVUz3pmgtg"},
    "Pipet Volume": {"fungsi": "Mengambil larutan cair dengan volume tunggal spesifik berakurasi tinggi.", "stok": 40, "img": "https://share.google/9IV4xvZPnQffLKKro"},
    "Rak Tabung Reaksi": {"fungsi": "Tempat menata dan menegakkan posisi tabung reaksi agar tidak tumpah.", "stok": 25, "img": "https://share.google/p0Zt4qKW7OzHkGeJW"},
    "Spatula Logam": {"fungsi": "Sendok kecil logam untuk mengambil sampel berwujud padat atau serbuk.", "stok": 40, "img": "https://share.google/onTymKCjesuyDUe6J"},
    "Statif dan Klem": {"fungsi": "Tiang logam vertikal dasar kokoh yang menyangga dudukan klem buret.", "stok": 30, "img": "https://share.google/XBb243k8Xu4S5vzDe"},
    "Tabung Reaksi": {"fungsi": "Wadah silindris kaca kecil untuk uji reaksi kualitatif zat kimia.", "stok": 120, "img": "https://share.google/9BzBKArTi4KIx6SqN"},
    "Termometer": {"fungsi": "Mengukur tingkat suhu lingkungan larutan reaksi kimia.", "stok": 25, "img": "https://share.google/PjvAYG80K9vVtRI6t"},
    "Waterbath": {"fungsi": "Pemanas lab tidak langsung dengan media air untuk menjaga stabilitas suhu sampel.", "stok": 4, "img": "https://share.google/y3sRhRXBYbENWNowW"}
}
alat_lab = list(database_alat.keys())

# =====================================================
# HOME
# =====================================================
if menu == "Home":
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
    st.write("")

    a,b,c = st.columns(3)

    with a:
        st.markdown("""
        <div class="card">
        <h3>🔍 Pencarian Alat</h3>
        <p>Temukan alat laboratorium dengan cepat dan mudah beserta visual gambarnya.</p>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class="card">
        <h3>📊 Riwayat Data</h3>
        <p>Akses kembali hasil perhitungan terdahulu Anda secara real-time.</p>
        </div>
        """, unsafe_allow_html=True)

    with c:
        st.markdown("""
        <div class="card">
        <h3>🧮 Kalkulator Kimia</h3>
        <p>Molaritas, Pengenceran, Kadar dan pH dengan rumus transparan.</p>
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
    ">    <p style="font-size:17px;">    
    Selamat menggunakan aplikasi laboratorium kimia yang dirancang untuk membantu    
    mahasiswa, praktikan, dan peneliti dalam melakukan perhitungan serta pencarian    
    alat laboratorium secara cepat, mudah, dan akurat.    
    </p>    <p>    
    Gunakan menu di sebelah kiri untuk mengakses seluruh fitur laboratorium    
    </p>    </div>    
    """, unsafe_allow_html=True)    
    st.divider()

# =====================================================
# MENU CEK ALAT
# =====================================================
elif menu == "Cek Stok Alat Laboratorium":
    st.header("CEK STOK ALAT LABORATORIUM")
    
    pilihan_alat = st.selectbox("Pilih alat yang ingin dicek:", ["-- Pilih Alat --"] + alat_lab)
    
    if st.button("Cek Detail Alat"):
        if pilihan_alat != "-- Pilih Alat --":
            st.success(f"Alat '{pilihan_alat}' TERSEDIA di Laboratorium")    
            
            c_img, c_fng = st.columns([1, 2])
            with c_img:
                st.image(database_alat[pilihan_alat]["img"], use_container_width=True, caption=pilihan_alat)
            with c_fng:
                st.info(f"**Fungsi Utama:** {database_alat[pilihan_alat]['fungsi']}")
                st.metric(label="Jumlah Stok Tersedia (Qty)", value=f"{database_alat[pilihan_alat]['stok']} unit")
                
            st.session_state.riwayat_pencarian.append(f"Cek Stok ➔ Alat: '{pilihan_alat}' ditemukan. Stok: {database_alat[pilihan_alat]['stok']} unit.")
        else:
            st.warning("Silakan pilih salah satu nama alat pada menu drop-down terlebih dahulu.")

    st.write("---")
    st.subheader("Katalog Inventaris Lengkap (Urutan Abjad A-Z)")
    
    for nama_item, data_item in database_alat.items():
        with st.expander(f"📦 {nama_item} (Stok: {data_item['stok']} Unit)"):
            col_kiri, col_kanan = st.columns([1, 4])
            with col_kiri:
                st.image(data_item["img"], use_container_width=True)
            with col_kanan:
                st.write(f"**Deskripsi Fungsi:** {data_item['fungsi']}")
                st.write(f"**Status Ketersediaan:** {data_item['stok']} unit siap digunakan praktikum.")

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
        st.session_state.riwayat_pencarian.append(f"Kalkulator Molaritas ➔ Mol: {mol} mol, Vol: {volume} L | Hasil: {round(hasil, 3)} M")

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
        st.session_state.riwayat_pencarian.append(f"Kalkulator Pengenceran ➔ M1: {M1} M, V1: {V1} mL, M2: {M2} M | V2 Hasil: {round(V2, 2)} mL")

# =====================================================
# MENU KADAR (DENGAN RUMUS PECAHAN ATAS-BAWAH)
# =====================================================
elif menu == "Kalkulator Kadar":
    st.header("KALKULATOR KADAR")

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

    if pilihan == "Kadar Asam Asetat":
        st.latex(r"\% \text{Kadar Asam Asetat} = \frac{V \times N \times 60 \times 10^{-3} \times FP \times 100}{V_{\text{sampel}}}")
        
        V = st.number_input("Volume titrasi / V (mL)")    
        N = st.number_input("Normalitas / N (mgrek/mL)")    
        FP = st.number_input("Faktor pengenceran (FP)")    
        V_sampel = st.number_input("Volume sampel (mL)")    

        if st.button("Hitung Kadar"):    
            hasil = ((V * N * 60) * (10**-3) * FP * 100) / V_sampel    
            st.success(f"Kadar CH3COOH = {round(hasil,2)} %")
            st.session_state.riwayat_pencarian.append(f"Kadar CH3COOH ➔ V: {V} mL, N: {N} | Hasil: {round(hasil,2)} %")

    elif pilihan == "NaOH dan Na2CO3 (Warder)":
        st.latex(r"\% \text{Na}_2\text{CO}_3 = \frac{2 \times (b - a) \times N \times 53 \times 10^{-3} \times 100}{V_{\text{sampel}}}")
        st.latex(r"\% \text{NaOH} = \frac{(2a - b) \times N \times 40 \times 10^{-3} \times 100}{V_{\text{sampel}}}")
        
        a = st.number_input("Volume titrasi 1 / a (mL)")    
        b = st.number_input("Volume titrasi 2 / b (mL)")    
        N = st.number_input("Normalitas / N (mgrek/mL)")    
        V_sampel = st.number_input("Volume sampel (mL)")    

        if st.button("Hitung Kadar"):    
            BE_NaOH = 40    
            BE_Na2CO3 = 53    
            Na2CO3 = ((2 * (b-a)* N * BE_Na2CO3) * (10**-3) * 100) / V_sampel    
            NaOH = (((2*a - b)* N * BE_NaOH) * (10**-3) * 100) / V_sampel    
            st.success(f"Kadar NaOH = {round(NaOH,2)} %")    
            st.success(f"Kadar Na2CO3 = {round(Na2CO3,2)} %")
            st.session_state.riwayat_pencarian.append(f"Kadar Warder ➔ a: {a} mL, b: {b} mL | NaOH: {round(NaOH,2)}%, Na2CO3: {round(Na2CO3,2)}%")

    elif pilihan == "Kadar Besi(Fe)":
        st.latex(r"\% \text{Kadar Fe} = \frac{V \times N \times 56 \times 10^{-3} \times 100}{V_{\text{sampel}}}")
        
        V = st.number_input("Volume titrasi / V (mL)")    
        N = st.number_input("Normalitas / N (mgrek/mL)")    
        V_sampel = st.number_input("Volume sampel (mL)")    

        if st.button("Hitung Kadar"):    
            hasil = ((V * N * 56) * (10**-3) * 100) / V_sampel    
            st.success(f"Kadar Fe = {round(hasil,2)} %")
            st.session_state.riwayat_pencarian.append(f"Kadar Fe ➔ V: {V} mL, N: {N} | Hasil: {round(hasil,2)} %")

    elif pilihan == "Kadar Klorida(Cl) Iodometri":
        st.latex(r"\% \text{Kadar Cl (Iodometri)} = \frac{V \times N \times 17.75 \times 10^{-3} \times \frac{100}{5} \times 100}{V_{\text{sampel}}}")
        
        V = st.number_input("Volume titrasi / V (mL)")    
        N = st.number_input("Normalitas / N (mgrek/mL)")    
        V_sampel = st.number_input("Volume sampel (mL)")    

        if st.button("Hitung Kadar"):    
            hasil = ((V * N * 17.75) * (10**-3) * (100/5) * 100) / V_sampel    
            st.success(f"Kadar Cl = {round(hasil,2)} %")
            st.session_state.riwayat_pencarian.append(f"Kadar Cl Iodometri ➔ V: {V} mL, N: {N} | Hasil: {round(hasil,2)} %")

    elif pilihan == "Kadar Klorida(Cl) Argentometri":
        st.latex(r"\% \text{Kadar Cl (Argentometri)} = \frac{V \times N \times 35.5 \times 10^{-3} \times 100}{V_{\text{sampel}}}")
        
        V = st.number_input("Volume titrasi / V (mL)")    
        N = st.number_input("Normalitas / N (mgrek/mL)")    
        V_sampel = st.number_input("Volume sampel (mL)")    

        if st.button("Hitung Kadar"):    
            hasil = ((V * N * 35.5) * (10**-3) * 100) / V_sampel    
            st.success(f"Kadar Cl = {round(hasil,2)} %")
            st.session_state.riwayat_pencarian.append(f"Kadar Cl Argentometri ➔ V: {V} mL, N: {N} | Hasil: {round(hasil,2)} %")

    elif pilihan == "Kesadahan Air":
        st.latex(r"\text{Kesadahan CaCO}_3 = \frac{V \times M \times 100}{V_{\text{sampel}}}")
        
        V = st.number_input("Volume titrasi / V (mL)")    
        M = st.number_input("Molaritas / M (mmol/mL)")    
        V_sampel = st.number_input("Volume sampel (L)")    

        if st.button("Hitung Kadar"):    
            hasil = ((V * M * 100)) / V_sampel    
            st.success(f"Kadar CaCO3 = {round(hasil,2)} mg/L (ppm)")
            st.session_state.riwayat_pencarian.append(f"Kesadahan Air ➔ V: {V} mL, M: {M} | Hasil: {round(hasil,2)} ppm")

# =====================================================
# MENU pH
# =====================================================
elif menu == "Kalkulator pH":
    st.header("KALKULATOR pH")

    st.warning("""
    ⚠️ **Catatan Keterbatasan Fitur yang Disediakan:**
    1. Hanya mendukung komputasi larutan **Asam Kuat Monovalen** langsung tanpa tetapan kesetimbangan.
    2. Belum memfasilitasi peninjauan nilai tetapan konstanta ionisasi derajat asam lemah ($K_a$) atau nilai derajat ionisasi ($\alpha$).
    3. Output operasional skala logaritma dinormalisasi kaku di antara parameter interval standar **0 hingga 14**.
    """)

    h_input = st.text_input("Masukkan konsentrasi H+ (contoh: 10^-4 atau 0.0001)")

    if st.button("Hitung pH"):
        try:    
            h_input = h_input.replace(",", ".")    
            if "^" in h_input:    
                base, exp = h_input.split("^")    
                if base.strip() == "10":    
                    h = 10 ** float(exp)    
                else:    
                    h = float(h_input)    
            else:    
                h = float(h_input)    

            if h <= 0:    
                st.error("Konsentrasi H+ harus lebih dari 0!")    
            else:    
                hasil = -math.log10(h)    
                ph = round(hasil, 2)    

                if ph < 0:    
                    ph = 0    
                elif ph > 14:    
                    ph = 14    

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

                if ph < 7:    
                    st.error(f"pH = {ph} ({sifat})")    
                elif ph == 7:    
                    st.info(f"pH = {ph} ({sifat})")    
                else:    
                    st.success(f"pH = {ph} ({sifat})")    
                
                st.session_state.riwayat_pencarian.append(f"Kalkulator pH ➔ Input H+: {h_input} | Hasil pH: {ph} ({sifat})")
        except:    
            st.error("Masukkan angka yang valid! (contoh: 10^-4 atau 0.0001)")

# =====================================================
# MENU RIWAYAT
# =====================================================
elif menu == "Riwayat":
    st.header("⏳ RIWAYAT AKTIVITAS & PERHITUNGAN")
    st.write("Semua aktivitas pencarian inventaris dan perhitungan kalkulator kimia Anda tersimpan otomatis.")
    
    if st.session_state.riwayat_pencarian:
        if st.button("Bersihkan Riwayat"):
            st.session_state.riwayat_pencarian = []
            st.rerun()
            
        for i, item in enumerate(reversed(st.session_state.riwayat_pencarian), 1):
            st.info(f"**{i}.** {item}")
    else:
        st.write("Belum ada data aktivitas riwayat saat ini.")

# =====================================================
# MENU CREATOR (DENGAN TAMPILAN FOTO TIM KELOMPOK)
# =====================================================
elif menu == "Creator":
    st.header("👤 INFORMASI CREATOR")
    
    col_foto, col_data = st.columns([1, 1])
    
    with col_foto:
        # Menampilkan foto bersama tim kelompok 12 yang dikirimkan
        st.image("https://share.google/284363.jpg", use_container_width=True, caption="Tim Kelompok 12_1D Politeknik AKA Bogor")
        
    with col_data:
        st.markdown("""
        <div class="card" style="text-align: left; padding: 30px; height: 100%;">
            <h2 style="color: #023e8a; margin-bottom: 10px;">🚀 Kelompok 12_1D</h2>
            <h4 style="color: #0077b6; margin-bottom: 25px;">Politeknik AKA Bogor</h4>
            <hr style="border: 0; border-top: 1px solid #edf6ff; margin-bottom: 20px;">
            <p style="font-size: 16px; margin-bottom: 12px;"><strong>• Aufa Freshika Aryani</strong> (NIM : 2560588)</p>
            <p style="font-size: 16px; margin-bottom: 12px;"><strong>• Aura Halimah Natanegoro</strong> (NIM : 2560589)</p>
            <p style="font-size: 16px; margin-bottom: 12px;"><strong>• Ayu Asyfa Mei Asyhari</strong> (NIM : 2560593)</p>
            <p style="font-size: 16px; margin-bottom: 12px;"><strong>• Oscar Tirta Sugema</strong> (NIM : 2560735)</p>
        </div>
        """, unsafe_allow_html=True)
