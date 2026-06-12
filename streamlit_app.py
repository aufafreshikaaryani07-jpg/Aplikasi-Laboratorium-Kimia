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
# DATABASE INVENTARIS ALAT LAB (NAMA FILE DISESUAIKAN GITHUB)
# =====================================================
database_alat = {
    "Alu dan Mortar": {"fungsi": "Menghancurkan atau menghaluskan sampel padat laboratorium.", "stok": 15, "img": "Alu dan Mortar.jpg.jpeg"},
    "Batang Pengaduk": {"fungsi": "Mengaduk larutan kimia agar komponen zat terlarut dapat tercampur homogen.", "stok": 40, "img": "Batang Pengaduk.jpg.jpeg"},
    "Beaker Glass": {"fungsi": "Wadah penampung, pengaduk, pencampur, dan pemanas cairan kimia.", "stok": 60, "img": "Beaker Glass.jpg.jpeg"},
    "Botol Reagen": {"fungsi": "Tempat penyimpanan larutan reagen kimia agar terhindar dari kontaminasi udara luar.", "stok": 35, "img": "Botol Reagen.jpg.jpeg"},
    "Botol Semprot": {"fungsi": "Menyimpan akuades yang digunakan untuk membersihkan atau membilas sisa larutan.", "stok": 25, "img": "Botol Semprot.jpg.jpeg"},
    "Botol Timbang": {"fungsi": "Menimbang zat padat atau sampel cair yang bersifat higroskopis.", "stok": 20, "img": "Botol Timbang.jpg.jpeg"},
    "Bunsen": {"fungsi": "Alat pemanas lab dengan sistem pembakaran gas untuk sterilisasi dan pemanasan zat.", "stok": 15, "img": "Bunsen.jpg.jpeg"},
    "Buret": {"fungsi": "Mengeluarkan larutan dengan volume spesifik dan akurat pada analisis titrasi.", "stok": 30, "img": "Buret.jpg.jpeg"},
    "Cawan Petri": {"fungsi": "Wadah sirkular jernih untuk membiakkan media mikroorganisme dan bakteri.", "stok": 50, "img": "Cawan Petri.jpg.jpeg"},
    "Cawan Porselen": {"fungsi": "Mereaksikan atau menguapkan larutan pada suhu tinggi di atas kaki tiga.", "stok": 25, "img": "Cawan Porselen.jpg.jpeg"},
    "Corong Kaca": {"fungsi": "Mempermudah pemindahan cairan ke wadah bermulut kecil dan menopang kertas saring.", "stok": 30, "img": "Corong Kaca.jpg.jpeg"},
    "Corong Pisah": {"fungsi": "Memisahkan komponen fraksi dari dua cairan fase berbeda berdasarkan berat jenis.", "stok": 10, "img": "Corong Pisah.jpg.jpeg"},
    "Desikator": {"fungsi": "Menjaging kelembapan dan mengeringkan sampel padat yang sensitif terhadap air.", "stok": 6, "img": "Desikator.jpg.jpeg"},
    "Erlenmeyer": {"fungsi": "Wadah mencampur larutan analit, menampung hasil titrasi, dan memanaskan cairan.", "stok": 55, "img": "Erlenmeyer.jpg.jpeg"},
    "Gelas Ukur": {"fungsi": "Mengukur volume larutan kimia secara makro dengan kepatuhan akurasi menengah.", "stok": 45, "img": "Gelas Ukur.jpg.jpeg"},
    "Gegep Besi": {"fungsi": "Menjepit buret, labu alas bulat, atau peralatan gelas lain pada tiang statif.", "stok": 25, "img": "Gegep Besi.jpg.jpeg"},
    "Gegep Kayu": {"fungsi": "Menjepit tabung reaksi ketika dalam proses pemanasan di atas api.", "stok": 30, "img": "Gegep Kayu.jpg.jpeg"},
    "Hot Plate": {"fungsi": "Alat elektronik pemanas datar sekaligus mengaduk sampel secara otomatis.", "stok": 8, "img": "Hot Plate.jpg.jpeg"},
    "Inkubator": {"fungsi": "Menginkubasi kultur sel mikrobiologi pada kondisi suhu konstan.", "stok": 4, "img": "Inkubator.jpg.jpeg"},
    "Jarum Ose": {"fungsi": "Mengambil mikroba atau
