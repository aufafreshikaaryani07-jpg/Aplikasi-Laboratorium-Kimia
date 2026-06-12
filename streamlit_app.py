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
[data-testid="stSidebar"] *{    
    color:white;    
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
.penjelasan-box {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #0077b6;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
    margin-bottom: 25px;
    color: #333333;
}
</style>  
""", unsafe_allow_html=True)  

st.divider()

# Menu Utama
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
# DATABASE ALAT LAB (Fungsi, Gambar, & Jumlah Stok Estimasi)
# =====================================================
database_alat = {
    "Alu": {"fungsi": "Menghancurkan atau menghaluskan sampel padat di dalam mortar.", "stok": 15, "img": "https://images.unsplash.com/photo-1614859324967-bdf461fec769?w=400"},
    "Batang Pengaduk": {"fungsi": "Mengaduk larutan agar komponen zat terlarut dapat tercampur homogen.", "stok": 40, "img": "https://images.unsplash.com/photo-1605647540924-852290f6b0d5?w=400"},
    "Beaker Glass": {"fungsi": "Wadah penampung, pengaduk, pencampur, dan pemanas cairan kimia.", "stok": 60, "img": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400"},
    "Botol Reagen": {"fungsi": "Tempat penyimpanan larutan reagen kimia agar terhindar dari kontaminasi udara luar.", "stok": 35, "img": "https://images.unsplash.com/photo-1532187863486-abf9d39d6618?w=400"},
    "Botol Timbang": {"fungsi": "Menimbang zat padat atau sampel cair yang bersifat higroskopis.", "stok": 20, "img": "https://images.unsplash.com/photo-1607613009820-a29f7bb81c04?w=400"},
    "Botol Semprot": {"fungsi": "Menyimpan akuades yang digunakan untuk membersihkan atau membilas sisa sisa larutan.", "stok": 25, "img": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=400"},
    "Buret": {"fungsi": "Mengeluarkan larutan dengan volume spesifik dan akurat pada analisis titrasi.", "stok": 30, "img": "https://images.unsplash.com/photo-1527018601619-a508a2be00cd?w=400"},
    "Bunsen": {"fungsi": "Alat pemanas lab dengan sistem pembakaran gas untuk sterilisasi dan pemanasan zat.", "stok": 15, "img": "https://images.unsplash.com/photo-1576086213369-97a306d36557?w=400"},
    "Cawan Petri": {"fungsi": "Wadah sirkular jernih untuk membiakkan media mikroorganisme dan bakteri.", "stok": 50, "img": "https://images.unsplash.com/photo-1576086212399-f53839be4990?w=400"},
    "Corong Kaca": {"fungsi": "Mempermudah pemindahan cairan ke wadah bermulut kecil dan menopang kertas saring.", "stok": 30, "img": "https://images.unsplash.com/photo-1582719508461-905c673771fd?w=400"},
    "Cawan Porselen": {"fungsi": "Mereaksikan atau menguapkan larutan pada suhu tinggi di atas kaki tiga.", "stok": 25, "img": "https://images.unsplash.com/photo-1576086212170-c750c183cf9c?w=400"},
    "Corong Pisah": {"fungsi": "Memisahkan komponen fraksi dari dua cairan fase berbeda berdasarkan berat jenis.", "stok": 10, "img": "https://images.unsplash.com/photo-1617155093730-a8bf47be792d?w=400"},
    "Desikator": {"fungsi": "Menjaga kelembapan dan mengeringkan sampel padat yang sensitif terhadap air.", "stok": 6, "img": "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=400"},
    "Erlenmeyer": {"fungsi": "Wadah mencampur larutan analit, menampung hasil titrasi, dan memanaskan bahan cair.", "stok": 55, "img": "https://images.unsplash.com/photo-1579165466741-7f35e4755660?w=400"},
    "Gelas Ukur": {"fungsi": "Mengukur volume larutan kimia secara makro dengan kepatuhan akurasi menengah.", "stok": 45, "img": "https://images.unsplash.com/photo-1605647540924-852290f6b0d5?w=400"},
    "Gegep Besi": {"fungsi": "Menjepit buret, labu alas bulat, atau peralatan gelas lain pada tiang statif.", "stok": 25, "img": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400"},
    "Gegep Kayu": {"fungsi": "Menjepit tabung reaksi ketika dalam proses pemanasan di atas api bunsen.", "stok": 30, "img": "https://images.unsplash.com/photo-1514539079130-25950c84af65?w=400"},
    "Hot Plate": {"fungsi": "Alat elektronik pemanas datar sekaligus mengaduk sampel secara otomatis dengan magnet stirer.", "stok": 8, "img": "https://images.unsplash.com/photo-1617155093730-a8bf47be792d?w=400"},
    "Inkubator": {"fungsi": "Menginkubasi kultur sel mikrobiologi pada kondisi suhu dan kelembapan konstan.", "stok": 4, "img": "https://images.unsplash.com/photo-1579154204601-01588f35116f?w=400"},
    "Jarum Ose": {"fungsi": "Mengambil mikroba atau melakukan inokulasi bakteri secara aseptik ke media baru.", "stok": 20, "img": "https://images.unsplash.com/photo-1576328077655-515de3aa67da?w=400"},
    "Kaca Arloji": {"fungsi": "Wadah penimbangan sampel kristal padat atau penutup gelas beaker.", "stok": 35, "img": "https://images.unsplash.com/photo-1607613009820-a29f7bb81c04?w=400"},
    "Kaki Tiga": {"fungsi": "Penyangga besi melingkar tiga kaki untuk menopang wadah sampel saat pemanasan.", "stok": 20, "img": "https://images.unsplash.com/photo-1576086213369-97a306d36557?w=400"},
    "Kasa Asbes": {"fungsi": "Meratakan rambatan panas api dari bunsen agar wadah kaca tidak pecah akibat thermal shock.", "stok": 25, "img": "https://images.unsplash.com/photo-1576086213369-97a306d36557?w=400"},
    "Kertas Saring": {"fungsi": "Menyaring partikel residu padatan terlarut dari cairan filtrat.", "stok": 100, "img": "https://images.unsplash.com/photo-1582719508461-905c673771fd?w=400"},
    "Klem Buret": {"fungsi": "Menjepit buret agar terpasang kokoh tegak lurus pada tiang besi statif.", "stok": 30, "img": "https://images.unsplash.com/photo-1527018601619-a508a2be00cd?w=400"},
    "Kuvet": {"fungsi": "Wadah kecil transparan tempat menaruh larutan uji pada alat spektrofotometer.", "stok": 40, "img": "https://images.unsplash.com/photo-1576328077655-515de3aa67da?w=400"},
    "Labu Alas Bulat": {"fungsi": "Wadah mendidihkan larutan pada apparatus distilasi atau ekstraksi refluks.", "stok": 15, "img": "https://images.unsplash.com/photo-1617155093730-a8bf47be792d?w=400"},
    "Labu Takar": {"fungsi": "Membuat larutan standar primer atau sekunder dengan ketelitian volume sangat tinggi.", "stok": 35, "img": "https://images.unsplash.com/photo-1582719508461-905c673771fd?w=400"},
    "Laminar Air Flow": {"fungsi": "Meja kerja steril dengan aliran udara tersaring untuk mencegah kontaminasi mikroba.", "stok": 3, "img": "https://images.unsplash.com/photo-1579154204601-01588f35116f?w=400"},
    "Mikropipet": {"fungsi": "Memindahkan cairan bervolume ultra kecil (skala mikroliter) secara akurat.", "stok": 12, "img": "https://images.unsplash.com/photo-1601597111158-2fceff292cdc?w=400"},
    "Mortar": {"fungsi": "Wadah cekung batu/porselen padat untuk menghaluskan material sampel padat kasar.", "stok": 15, "img": "https://images.unsplash.com/photo-1614859324967-bdf461fec769?w=400"},
    "Mekker": {"fungsi": "Pembakar gas bersuhu super tinggi dengan kisi distribusi api yang lebar.", "stok": 10, "img": "https://images.unsplash.com/photo-1576086213369-97a306d36557?w=400"},
    "Neraca Analitik": {"fungsi": "Mengukur berat massa substansi kimia berpresisi mikro tinggi (sub miligram).", "stok": 6, "img": "https://images.unsplash.com/photo-1607613009820-a29f7bb81c04?w=400"},
    "Oven": {"fungsi": "Mengeringkan peralatan gelas pasca cuci atau menghilangkan kadar air sampel uji.", "stok": 4, "img": "https://images.unsplash.com/photo-1579154204601-01588f35116f?w=400"},
    "pH meter": {"fungsi": "Mengukur nilai derajat keasaman atau nilai konsentrasi ion hidrogen secara digital.", "stok": 10, "img": "https://images.unsplash.com/photo-1576328077655-515de3aa67da?w=400"},
    "Pipet Volume": {"fungsi": "Mengambil larutan cair dengan volume tunggal spesifik pada akurasi analitis tingkat tinggi.", "stok": 40, "img": "https://images.unsplash.com/photo-1601597111158-2fceff292cdc?w=400"},
    "Pipet Tetes": {"fungsi": "Memindahkan cairan reagen dalam volume sangat kecil secara tak terukur demi tetes demi tetes.", "stok": 80, "img": "https://images.unsplash.com/photo-1559757175-5700dde675bc?w=400"},
    "Pipet Mohr": {"fungsi": "Mengambil larutan dengan rentang volume bervariasi sesuai dengan garis tanda skala ukur.", "stok": 30, "img": "https://images.unsplash.com/photo-1601597111158-2fceff292cdc?w=400"},
    "Piknometer": {"fungsi": "Mengukur nilai densitas massa jenis dari zat cair fluida murni.", "stok": 15, "img": "https://images.unsplash.com/photo-1607613009820-a29f7bb81c04?w=400"},
    "Polismen": {"fungsi": "Batang pengaduk berkepala karet lunak untuk membersihkan sisa endapan di dasar wadah.", "stok": 15, "img": "https://images.unsplash.com/photo-1605647540924-852290f6b0d5?w=400"},
    "Rak Tabung Reaksi": {"fungsi": "Tempat menata dan menegakkan posisi tabung reaksi agar tidak tumpah.", "stok": 25, "img": "https://images.unsplash.com/photo-1532187863486-abf9d39d6618?w=400"},
    "Sentrifus": {"fungsi": "Memutar sampel berkecepatan tinggi untuk mengendapkan fase suspensi padat dari pelarut cairan.", "stok": 5, "img": "https://images.unsplash.com/photo-1579154204601-01588f35116f?w=400"},
    "Segitiga Porselen": {"fungsi": "Penahan krus porselen saat dibakar langsung di atas cincin pemanas besi.", "stok": 20, "img": "https://images.unsplash.com/photo-1576086212170-c750c183cf9c?w=400"},
    "Spatula": {"fungsi": "Sendok kecil logam atau plastik untuk mengambil sampel berwujud padat atau serbuk.", "stok": 40, "img": "https://images.unsplash.com/photo-1607613009820-a29f7bb81c04?w=400"},
    "Spektrofotometer": {"fungsi": "Mengukur nilai absorbansi dan intensitas transmisi cahaya larutan berdasarkan panjang gelombang.", "stok": 4, "img": "https://images.unsplash.com/photo-1576328077655-515de3aa67da?w=400"},
    "Statif": {"fungsi": "Tiang logam vertikal dasar kokoh yang menyangga dudukan klem buret.", "stok": 30, "img": "https://images.unsplash.com/photo-1527018601619-a508a2be00cd?w=400"},
    "Spirtus": {"fungsi": "Pembakar portabel sumbu kain dengan menggunakan bahan bakar cair alkohol.", "stok": 20, "img": "https://images.unsplash.com/photo-1576086213369-97a306d36557?w=400"},
    "Soxhlet": {"fungsi": "Apparatus lab untuk ekstraksi lipid atau zat organik dari sampel padat secara berulang.", "stok": 6, "img": "https://images.unsplash.com/photo-1617155093730-a8bf47be792d?w=400"},
    "Tabung Reaksi": {"fungsi": "Wadah silindris kaca kecil untuk uji reaksi kualitatif zat kimia.", "stok": 120, "img": "https://images.unsplash.com/photo-1532187863486-abf9d39d6618?w=400"},
    "Tanur": {"fungsi": "Tungku pemanas bersuhu super tinggi untuk proses pengabuan gravimetri sampel analitik.", "stok": 2, "img": "https://images.unsplash.com/photo-1579154204601-01588f35116f?w=400"},
    "Tutup Kaca": {"fungsi": "Penutup kedap udara bagi botol reagen berasah atau labu takar.", "stok": 40, "img": "https://images.unsplash.com/photo-1532187863486-abf9d39d6618?w=400"},
    "Termometer": {"fungsi": "Mengukur tingkat suhu lingkungan larutan atau perubahan temperatur reaksi kimia.", "stok": 25, "img": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=400"},
    "Vortex": {"fungsi": "Mengocok tabung reaksi dengan getaran rotasi cepat agar campuran homogen.", "stok": 6, "img": "https://images.unsplash.com/photo-1579154204601-01588f35116f?w=400"},
    "Water bath": {"fungsi": "Pemanas lab tidak langsung dengan media air untuk menjaga stabilitas suhu sampel.", "stok": 4, "img": "https://images.unsplash.com/photo-1579154204601-01588f35116f?w=400"}
}
alat_lab = list(database_alat.keys())

# =====================================================
# HOME (Dengan Efek Balon)
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
# MENU CEK ALAT (Tanpa Checkbox, Stok & Gambar Otomatis)
# =====================================================
elif menu == "Cek Stok Alat Laboratorium":
    st.header("CEK STOK ALAT LABORATORIUM")
    
    cari = st.text_input("Cari alat apa?")
    
    if st.button("Cek Alat"):
        key_alat = cari.title().strip()
        if key_alat in database_alat:    
            st.success(f"Alat '{key_alat}' TERSEDIA di laboratorium")    
            
            c_img, c_fng = st.columns([1, 2])
            with c_img:
                st.image(database_alat[key_alat]["img"], use_container_width=True, caption=key_alat)
            with c_fng:
                st.info(f"**Fungsi Utama:** {database_alat[key_alat]['fungsi']}")
                st.metric(label="Jumlah Stok Tersedia", value=f"{database_alat[key_alat]['stok']} unit")
                
            st.session_state.riwayat_pencarian.append(f"Cek Stok ➔ Alat: '{key_alat}' ditemukan. Stok: {database_alat[key_alat]['stok']} unit.")
        else:    
            st.error(f"Alat '{cari}' TIDAK DITEMUKAN")
            st.session_state.riwayat_pencarian.append(f"Cek Stok ➔ Alat: '{cari}' tidak ditemukan.")

    st.write("---")
    st.subheader("Katalog Inventaris Alat Laboratorium")
    
    # Layout Grid Otomatis Menampilkan Semua Detail Alat & Stok Tanpa Checkbox
    for nama_item, data_item in database_alat.items():
        with st.expander(f"📦 {nama_item} (Stok: {data_item['stok']} Unit)"):
            col_kiri, col_kanan = st.columns([1, 4])
            with col_kiri:
                st.image(data_item["img"], use_container_width=True)
            with col_kanan:
                st.write(f"**Deskripsi Fungsi:** {data_item['fungsi']}")
                st.write(f"**Status Ketersediaan:** {data_item['stok']} unit siap digunakan.")
# =====================================================
# MENU MOLARITAS
# =====================================================
elif menu == "Kalkulator Molaritas":
    st.header("KALKULATOR MOLARITAS")

    st.markdown("""
    <div class="penjelasan-box">
        <strong>Pengertian:</strong><br>
        Kalkulator Molaritas digunakan untuk menghitung konsentrasi larutan secara otomatis berdasarkan jumlah mol dan volume larutan.<br><br>
        <strong>Rumus Kimia:</strong><br>
        <span style="font-size:18px; color:#023e8a; font-weight:bold; background-color:#edf6ff; padding:5px 10px; border-radius:8px;">M = n / V</span><br><br>
        <strong>Keterangan Satuan:</strong><br>
        • M = Molaritas larutan (mol/L)<br>
        • n = Jumlah mol zat terlarut (mol)<br>
        • V = Volume larutan (L)
    </div>
    """, unsafe_allow_html=True)

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

    st.markdown("""
    <div class="penjelasan-box">
        <strong>Pengertian:</strong><br>
        Kalkulator Pengenceran digunakan untuk menghitung volume larutan akhir setelah proses penambahan pelarut murni tanpa merubah massa zat kimia terlarut.<br><br>
        <strong>Rumus Kimia:</strong><br>
        <span style="font-size:18px; color:#023e8a; font-weight:bold; background-color:#edf6ff; padding:5px 10px; border-radius:8px;">M1 × V1 = M2 × V2</span><br><br>
        <strong>Keterangan Satuan:</strong><br>
        • M1 = Molaritas mula-mula pekat (M)<br>
        • V1 = Volume mula-mula pekat (mL)<br>
        • M2 = Molaritas larutan encer yang diinginkan (M)<br>
        • V2 = Volume larutan encer hasil pengenceran (mL)
    </div>
    """, unsafe_allow_html=True)

    M1 = st.number_input("Masukkan M1 (M):", min_value=0.0)
    V1 = st.number_input("Masukkan V1 (mL):", min_value=0.0)
    M2 = st.number_input("Masukkan M2 (M):", min_value=0.0001)

    if st.button("Hitung Pengenceran"):
        V2 = (M1 * V1) / M2    
        st.success(f"V2 = {round(V2, 2)} mL")
        st.session_state.riwayat_pencarian.append(f"Kalkulator Pengenceran ➔ M1: {M1} M, V1: {V1} mL, M2: {M2} M | V2 Hasil: {round(V2, 2)} mL")

# =====================================================
# MENU KADAR
# =====================================================
elif menu == "Kalkulator Kadar":
    st.header("KALKULATOR KADAR")

    st.markdown("""
    <div class="penjelasan-box">
        <strong>Pengertian:</strong><br>
        Kalkulator Kadar digunakan untuk mengukur persentase kandungan fraksi zat analit tertentu di dalam contoh sampel kimia melalui pengujian teknik volumetri.<br><br>
        <strong>Rumus Umum Volumetri:</strong><br>
        <span style="font-size:16px; color:#023e8a; font-weight:bold; background-color:#edf6ff; padding:5px 10px; border-radius:8px;">% Kadar = ((V × N × BE) × 10⁻³ × FP × 100) / V_sampel</span>
    </div>
    """, unsafe_allow_html=True)

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
        V = st.number_input("Volume titrasi/V(mL)")    
        N = st.number_input("Normalitas/N(mgrek/mL)")    
        FP = st.number_input("Faktor pengenceran")    
        V_sampel = st.number_input("Volume sampel (mL)")    

        if st.button("Hitung Kadar"):    
            hasil = ((V * N * 60) * (10**-3) * FP * 100) / V_sampel    
            st.success(f"Kadar CH3COOH = {round(hasil,2)} %")
            st.session_state.riwayat_pencarian.append(f"Kadar CH3COOH ➔ V: {V} mL, N: {N}, FP: {FP}, V_sampel: {V_sampel} mL | Hasil: {round(hasil,2)} %")

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
            st.session_state.riwayat_pencarian.append(f"Kadar Warder ➔ a: {a} mL, b: {b} mL, N: {N} | NaOH: {round(NaOH,2)}%, Na2CO3: {round(Na2CO3,2)}%")

    elif pilihan == "Kadar Besi(Fe)":
        V = st.number_input("Volume titrasi/V(mL)")    
        N = st.number_input("Normalitas/N(mgrek/mL)")    
        V_sampel = st.number_input("Volume sampel (mL)")    

        if st.button("Hitung Kadar"):    
            hasil = ((V * N * 56) * (10**-3) * 100) / V_sampel    
            st.success(f"Kadar Fe = {round(hasil,2)} %")
            st.session_state.riwayat_pencarian.append(f"Kadar Fe ➔ V: {V} mL, N: {N}, V_sampel: {V_sampel} mL | Hasil: {round(hasil,2)} %")

    elif pilihan == "Kadar Klorida(Cl) Iodometri":
        V = st.number_input("Volume titrasi/V(mL)")    
        N = st.number_input("Normalitas/N(mgrek/mL)")    
        V_sampel = st.number_input("Volume sampel (mL)")    

        if st.button("Hitung Kadar"):    
            hasil = ((V * N * 17.75) * (10**-3) * 100/5 * 100) / V_sampel    
            st.success(f"Kadar Cl = {round(hasil,2)} %")
            st.session_state.riwayat_pencarian.append(f"Kadar Cl Iodometri ➔ V: {V} mL, N: {N}, V_sampel: {V_sampel} mL | Hasil: {round(hasil,2)} %")

    elif pilihan == "Kadar Klorida(Cl) Argentometri":
        V = st.number_input("Volume titrasi/V(mL)")    
        N = st.number_input("Normalitas/N(mgrek/mL)")    
        V_sampel = st.number_input("Volume sampel (mL)")    

        if st.button("Hitung Kadar"):    
            hasil = ((V * N * 35.5) * (10**-3) * 100) / V_sampel    
            st.success(f"Kadar Cl = {round(hasil,2)} %")
            st.session_state.riwayat_pencarian.append(f"Kadar Cl Argentometri ➔ V: {V} mL, N: {N}, V_sampel: {V_sampel} mL | Hasil: {round(hasil,2)} %")

    elif pilihan == "Kesadahan Air":
        V = st.number_input("Volume titrasi/V(mL)")    
        M = st.number_input("Molaritas/M(mmol/mL)")    
        V_sampel = st.number_input("Volume sampel (L)")    

        if st.button("Hitung Kadar"):    
            hasil = ((V * M * 100)) / V_sampel    
            st.success(f"Kadar CaCO3 = {round(hasil,2)} %")
            st.session_state.riwayat_pencarian.append(f"Kesadahan Air ➔ V: {V} mL, M: {M}, V_sampel: {V_sampel} L | Hasil: {round(hasil,2)} %")

# =====================================================
# MENU pH
# =====================================================
elif menu == "Kalkulator pH":
    st.header("KALKULATOR pH")

    st.markdown("""
    <div class="penjelasan-box">
        <strong>Pengertian:</strong><br>
        Kalkulator pH digunakan untuk mendeteksi derajat kekuatan keasaman zat senyawa cair berbasis aktivitas konsentrasi logaritma ion hidrogen negatif.<br><br>
        <strong>Rumus Kimia:</strong><br>
        <span style="font-size:18px; color:#023e8a; font-weight:bold; background-color:#edf6ff; padding:5px 10px; border-radius:8px;">pH = -log₁₀[H⁺]</span>
    </div>
    """, unsafe_allow_html=True)

    st.warning("""
    ⚠️ **Catatan Keterbatasan Fitur Aplikasi:**
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
    st.write("Semua aktivitas pencarian inventaris dan perhitungan kalkulator kimia Anda tersimpan otomatis di bawah ini selama aplikasi berjalan.")
    
    if st.session_state.riwayat_pencarian:
        if st.button("Bersihkan Riwayat"):
            st.session_state.riwayat_pencarian = []
            st.rerun()
            
        for i, item in enumerate(reversed(st.session_state.riwayat_pencarian), 1):
            st.info(f"**{i}.** {item}")
    else:
        st.write("Belum ada data aktivitas riwayat saat ini.")

# =====================================================
# MENU CREATOR
# =====================================================
elif menu == "Creator":
    st.header("👤 INFORMASI CREATOR")
    st.markdown("""
    <div class="card" style="text-align: left; padding: 30px;">
        <h2 style="color: #023e8a; margin-bottom: 20px;">🚀 Kelompok 12_1D</h2>
        <h4 style="color: #0077b6; margin-bottom: 25px;">Politeknik AKA Bogor</h4>
        <hr style="border: 0; border-top: 1px solid #edf6ff; margin-bottom: 20px;">
        <p style="font-size: 16px; margin-bottom: 12px;"><strong>• Aufa Freshika Aryani</strong> (NIM : 2560588)</p>
        <p style="font-size: 16px; margin-bottom: 12px;"><strong>• Aura Halimah Natanegoro</strong> (NIM : 2560589)</p>
        <p style="font-size: 16px; margin-bottom: 12px;"><strong>• Ayu Asyfa Mei Asyhari</strong> (NIM : 2560593)</p>
        <p style="font-size: 16px; margin-bottom: 12px;"><strong>• Oscar Tirta Sugema</strong> (NIM : 2560735)</p>
    </div>
    """, unsafe_allow_html=True)
