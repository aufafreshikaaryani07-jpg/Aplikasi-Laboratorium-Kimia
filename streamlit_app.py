import streamlit as st
import math
import random

# =====================================================
# MOLEVIA LANDING PAGE & CONFIG
# =====================================================
st.set_page_config(
    page_title="Molevia",
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
# MENAMPILKAN KEGUNAAN & RUMUS DI SIDEBAR
# =====================================================
if menu == "Kalkulator Molaritas":
    st.sidebar.markdown("""
    <div class="penjelasan-sidebar">
        <strong>📚 Kegunaan:</strong><br>
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
        <strong>📚 Kegunaan:</strong><br>
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
    pass

elif menu == "Kalkulator pH":
    st.sidebar.markdown("""
    <div class="penjelasan-sidebar">
        <strong>📚 Kegunaan:</strong><br>
        Digunakan untuk mendeteksi derajat kekuatan keasaman zat senyawa cair berbasis aktivitas konsentrasi logaritma ion hidrogen.<br><br>
        <strong>🧪 Rumus Kimia:</strong>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.latex(r"\text{pH} = -\log_{10}[H^+]")


# =====================================================
# DATABASE INVENTARIS ALAT LAB LENGKAP (55 ALAT)
# =====================================================
database_alat = {
    "Alu": {"fungsi": "Menghancurkan atau menghaluskan sampel padat laboratorium bersama mortar.", "stok": 15, "img": "Alu.jpg.jpeg"},
    "Batang Pengaduk": {"fungsi": "Mengaduk larutan kimia agar komponen zat terlarut dapat tercampur homogen.", "stok": 40, "img": "Batang Pengaduk.jpg.jpeg"},
    "Beaker Glass": {"fungsi": "Wadah penampung, pengaduk, pencampur, dan pemanas cairan kimia.", "stok": 60, "img": "Beaker Glass.jpg.jpeg"},
    "Botol Reagen": {"fungsi": "Tempat penyimpanan larutan reagen kimia agar terhindar dari kontaminasi udara luar.", "stok": 35, "img": "Botol Reagen.jpg.jpeg"},
    "Botol Timbang": {"fungsi": "Menimbang zat padat atau sampel cair yang bersifat higroskopis.", "stok": 20, "img": "Botol Timbang.jpg.jpeg"},
    "Botol Semprot": {"fungsi": "Menyimpan akuades yang digunakan untuk membersihkan atau membilas sisa larutan.", "stok": 25, "img": "Botol Semprot.jpg.jpeg"},
    "Buret": {"fungsi": "Mengeluarkan larutan dengan volume spesifik dan akurat pada analisis titrasi.", "stok": 20, "img": "Buret.jpg.jpeg"},
    "Bunsen": {"fungsi": "Alat pemanas lab dengan sistem pembakaran gas untuk sterilisasi dan pemanasan zat.", "stok": 15, "img": "Bunsen.jpg.jpeg"},
    "Cawan Petri": {"fungsi": "Wadah sirkular jernih untuk membiakkan media mikroorganisme dan bakteri.", "stok": 50, "img": "Cawan Petri.jpg.jpeg"},
    "Cawan Krusibel": {"fungsi": "Wadah untuk memanaskan spesimen atau sampel padat hingga suhu sangat tinggi.", "stok": 15, "img": "Cawan Krusibel.jpg.jpeg"},
    "Corong Kaca": {"fungsi": "Mempermudah pemindahan cairan ke wadah bermulut kecil dan menopang kertas saring.", "stok": 30, "img": "Corong Kaca.jpg.jpeg"},
    "Cawan Porselen": {"fungsi": "Mereaksikan atau menguapkan larutan pada suhu tinggi di atas kaki tiga.", "stok": 25, "img": "Cawan Porselen.jpg.jpeg"},
    "Corong Pisah": {"fungsi": "Memisahkan komponen fraksi dari dua cairan fase berbeda berdasarkan berat jenis.", "stok": 10, "img": "Corong Pisah.jpg.jpeg"},
    "Desikator": {"fungsi": "Menjaga kelembapan dan mengeringkan sampel padat yang sensitif terhadap air.", "stok": 6, "img": "Desikator.jpg.jpeg"},
    "Erlenmeyer": {"fungsi": "Wadah mencampur larutan analit, menampung hasil titrasi, dan memanaskan cairan.", "stok": 55, "img": "Erlenmeyer.jpg.jpeg"},
    "Gelas Ukur": {"fungsi": "Mengukur volume larutan kimia secara makro dengan kepatuhan akurasi menengah.", "stok": 45, "img": "Gelas Ukur.jpg.jpeg"},
    "Gegep Besi": {"fungsi": "Menjepit buret, labu alas bulat, atau peralatan gelas lain pada tiang statif.", "stok": 25, "img": "Gegep Besi.jpg.jpeg"},
    "Gegep Kayu": {"fungsi": "Menjepit tabung reaksi ketika dalam proses pemanasan di atas api.", "stok": 30, "img": "Gegep Kayu.jpg.jpeg"},
    "Hot Plate": {"fungsi": "Alat elektronik pemanas datar sekaligus mengaduk sampel secara otomatis.", "stok": 8, "img": "Hot Plate.jpg.jpeg"},
    "Inkubator": {"fungsi": "Menginkubasi kultur sel mikrobiologi pada kondisi suhu konstan.", "stok": 4, "img": "Inkubator.jpg.jpeg"},
    "Jarum Ose": {"fungsi": "Mengambil mikroba atau melakukan inokulasi bakteri secara aseptik.", "stok": 20, "img": "Jarum Ose.jpg.jpeg"},
    "Kaca Arloji": {"fungsi": "Wadah penimbangan sampel kristal padat atau penutup gelas beaker.", "stok": 35, "img": "Kaca Arloji.jpg.jpeg"},
    "Kaki Tiga": {"fungsi": "Penyanngga besi melingkar tiga kaki untuk menopang wadah sampel saat pemanasan.", "stok": 20, "img": "Kaki Tiga.jpg.jpeg"},
    "Kasa Asbes": {"fungsi": "Meratakan rambatan panas api dari bunsen agar wadah kaca tidak pecah.", "stok": 25, "img": "Kasa Asbes.jpg.jpeg"},
    "Kertas Saring": {"fungsi": "Menyaring partikel residu padatan terlarut dari cairan filtrat.", "stok": 100, "img": "Kertas Saring.jpg.jpeg"},
    "Klem Buret": {"fungsi": "Menjepit buret pada statif agar posisinya tegak lurus saat titrasi.", "stok": 15, "img": "Klem Buret.jpg.jpeg"},
    "Kuvet": {"fungsi": "Wadah sampel cair untuk analisis menggunakan spektrofotometer.", "stok": 40, "img": "Kuvet.jpg.jpeg"},
    "Labu Alas Bulat": {"fungsi": "Wadah memanaskan cairan atau destilasi larutan kimia.", "stok": 12, "img": "Labu Alas Bulat.jpg.jpeg"},
    "Labu Takar": {"fungsi": "Membuat larutan standar primer atau sekunder dengan ketelitian volume sangat tinggi.", "stok": 35, "img": "Labu Takar.jpg.jpeg"},
    "Laminar Air Flow": {"fungsi": "Meja kerja steril untuk melakukan penanaman mikroba terhindar kontaminasi.", "stok": 2, "img": "Laminar Air Flow.jpg.jpeg"},
    "Mikropipet": {"fungsi": "Memindahkan cairan bervolume ultra kecil (skala mikroliter) secara akurat.", "stok": 12, "img": "Mikropipet.jpg.jpeg"},
    "Mortar": {"fungsi": "Wadah lumpang penumbuk sampel bersama alu.", "stok": 15, "img": "Mortar.jpg.jpeg"},
    "Mekker": {"fungsi": "Pemanas gas yang menghasilkan api lebih besar dan panas dibanding bunsen standar.", "stok": 10, "img": "Mekker.jpg.jpeg"},
    "Neraca Analitik": {"fungsi": "Mengukur berat massa substansi kimia berpresisi mikro tinggi.", "stok": 6, "img": "Neraca Analitik.jpg.jpeg"},
    "Oven Laboratorium": {"fungsi": "Mengeringkan peralatan gelas pasca cuci atau menghilangkan kadar air sampel.", "stok": 4, "img": "Oven Laboratorium.jpg.jpeg"},
    "pH meter": {"fungsi": "Mengukur nilai derajat keasaman atau nilai konsentrasi ion hidrogen secara digital.", "stok": 10, "img": "pH meter.jpg.jpeg"},
    "Pipet Volume": {"fungsi": "Mengambil larutan cair dengan volume tunggal spesifik berakurasi tinggi.", "stok": 40, "img": "Pipet Volume.jpg.jpeg"},
    "Pipet Tetes": {"fungsi": "Memindahkan cairan reagen dalam volume sangat kecil secara tetes demi tetes.", "stok": 80, "img": "Pipet Tetes.jpg.jpeg"},
    "Pipet Mohr": {"fungsi": "Mengambil larutan dengan rentang volume bervariasi sesuai garis tanda skala.", "stok": 30, "img": "Pipet Mohr.jpg.jpeg"},
    "Piknometer": {"fungsi": "Mengukur nilai masa jenis atau densitas dari suatu cairan sampel.", "stok": 15, "img": "Piknometer.jpg.jpeg"},
    "Polismen": {"fungsi": "Alat bantu untuk membersihkan dinding wadah gelas dari endapan pereaksi.", "stok": 20, "img": "Polismen.jpg.jpeg"},
    "Rak Tabung Reaksi": {"fungsi": "Tempat menata dan menegakkan posisi tabung reaksi agar tidak tumpah.", "stok": 25, "img": "Rak Tabung Reaksi.jpg.jpeg"},
    "Sentrifus": {"fungsi": "Memisahkan endapan dan organel komponen cair berbasis gaya sentrifugal.", "stok": 5, "img": "Sentrifus.jpg.jpeg"},
    "Segitiga Porselen": {"fungsi": "Penyangga cawan porselen saat dipanaskan di atas kaki tiga.", "stok": 15, "img": "Segitiga Porselen.jpg.jpeg"},
    "Spatula Logam": {"fungsi": "Sendok kecil untuk mengambil sampel berwujud padat atau serbuk.", "stok": 40, "img": "Spatula Logam.jpg.jpeg"},
    "Spektrofotometer": {"fungsi": "Mengukur nilai absorbansi dan transmitansi gelombang cahaya sampel larutan.", "stok": 3, "img": "Spektrofotometer.jpg.jpeg"},
    "Statif": {"fungsi": "Tiang logam vertikal dasar kokoh yang menyangga dudukan klem buret.", "stok": 30, "img": "Statif.jpg.jpeg"},
    "Pembakar Spiritus": {"fungsi": "Lampu pembakar portable bermedia bahan bakar spirtus cair.", "stok": 20, "img": "Pembakar Spiritus.jpg.jpeg"},
    "Soxhlet": {"fungsi": "Ekstraksi komponen zat aktif padat menggunakan pelarut cair berulang kali.", "stok": 4, "
