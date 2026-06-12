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
# MENAMPILKAN PENGERTIAN & RUMUS DI SIDEBAR (REVISI POIN 2)
# =====================================================
if menu == "Kalkulator Molaritas":
    st.sidebar.markdown("""
    <div class="penjelasan-sidebar">
        <strong>📚 Pengertian:</strong><br>
        Digunakan untuk menghitung konsentrasi larutan secara otomatis berdasarkan jumlah mol dan volume larutan.<br><br>
        <strong>🧪 Rumus Kimia:</strong><br>
        <span style="font-size:16px; color:#ffffff; font-weight:bold; background: rgba(0,0,0,0.2); padding:2px 8px; border-radius:5px;">M = n / V</span><br><br>
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
        <strong>🧪 Rumus Kimia:</strong><br>
        <span style="font-size:15px; color:#ffffff; font-weight:bold; background: rgba(0,0,0,0.2); padding:2px 8px; border-radius:5px;">M1 × V1 = M2 × V2</span><br><br>
        <strong>Unit Satuan:</strong><br>
        • M1/M2: Molaritas (M)<br>
        • V1/V2: Volume (mL)
    </div>
    """, unsafe_allow_html=True)

elif menu == "Kalkulator Kadar":
    st.sidebar.markdown("""
    <div class="penjelasan-sidebar">
        <strong>📚 Pengertian:</strong><br>
        Digunakan untuk mengukur persentase kandungan fraksi zat analit tertentu di dalam sampel melalui teknik volumetri.<br><br>
        <strong>🧪 Rumus Umum:</strong><br>
        <span style="font-size:12px; color:#ffffff; font-weight:bold; background: rgba(0,0,0,0.2); padding:2px 5px; border-radius:5px;">% Kadar = ((V×N×BE)×10⁻³×FP×100)/V_sampel</span>
    </div>
    """, unsafe_allow_html=True)

elif menu == "Kalkulator pH":
    st.sidebar.markdown("""
    <div class="penjelasan-sidebar">
        <strong>📚 Pengertian:</strong><br>
        Digunakan untuk mendeteksi derajat kekuatan keasaman zat senyawa cair berbasis aktivitas konsentrasi logaritma ion hidrogen.<br><br>
        <strong>🧪 Rumus Kimia:</strong><br>
        <span style="font-size:16px; color:#ffffff; font-weight:bold; background: rgba(0,0,0,0.2); padding:2px 8px; border-radius:5px;">pH = -log₁₀[H⁺]</span>
    </div>
    """, unsafe_allow_html=True)


# =====================================================
# DATABASE inventaris ALAT LAB (GAMBAR RELEVAN & AKURAT)
# =====================================================
database_alat = {
    "Alu dan Mortar": {"fungsi": "Menghancurkan atau menghaluskan sampel padat laboratorium.", "stok": 15, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Mortar_and_pestle_grinding.jpg/400px-Mortar_and_pestle_grinding.jpg"},
    "Batang Pengaduk": {"fungsi": "Mengaduk larutan kimia agar komponen zat terlarut dapat tercampur homogen.", "stok": 40, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Glass_stirring_rods.jpg/400px-Glass_stirring_rods.jpg"},
    "Beaker Glass": {"fungsi": "Wadah penampung, pengaduk, pencampur, dan pemanas cairan kimia.", "stok": 60, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Beakers_and_liquid.jpg/400px-Beakers_and_liquid.jpg"},
    "Botol Reagen": {"fungsi": "Tempat penyimpanan larutan reagen kimia agar terhindar dari kontaminasi udara luar.", "stok": 35, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Reagent_bottles.jpg/400px-Reagent_bottles.jpg"},
    "Botol Timbang": {"fungsi": "Menimbang zat padat atau sampel cair yang bersifat higroskopis.", "stok": 20, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Weighing_bottle.jpg/400px-Weighing_bottle.jpg"},
    "Botol Semprot": {"fungsi": "Menyimpan akuades yang digunakan untuk membersihkan atau membilas sisa larutan.", "stok": 25, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Wash_bottle.jpg/400px-Wash_bottle.jpg"},
    "Buret": {"fungsi": "Mengeluarkan larutan dengan volume spesifik dan akurat pada analisis titrasi.", "stok": 30, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Burette_vertical.jpg/300px-Burette_vertical.jpg"},
    "Bunsen": {"fungsi": "Alat pemanas lab dengan sistem pembakaran gas untuk sterilisasi dan pemanasan zat.", "stok": 15, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Bunsen_burner_with_flame.jpg/400px-Bunsen_burner_with_flame.jpg"},
    "Cawan Petri": {"fungsi": "Wadah sirkular jernih untuk membiakkan media mikroorganisme dan bakteri.", "stok": 50, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Petri_dish_with_agar.jpg/400px-Petri_dish_with_agar.jpg"},
    "Corong Kaca": {"fungsi": "Mempermudah pemindahan cairan ke wadah bermulut kecil dan menopang kertas saring.", "stok": 30, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Laboratory_funnel.jpg/400px-Laboratory_funnel.jpg"},
    "Cawan Porselen": {"fungsi": "Mereaksikan atau menguapkan larutan pada suhu tinggi di atas kaki tiga.", "stok": 25, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Porcelain_crucible.jpg/400px-Porcelain_crucible.jpg"},
    "Corong Pisah": {"fungsi": "Memisahkan komponen fraksi dari dua cairan fase berbeda berdasarkan berat jenis.", "stok": 10, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Separatory_funnel.jpg/350px-Separatory_funnel.jpg"},
    "Desikator": {"fungsi": "Menjaga kelembapan dan mengeringkan sampel padat yang sensitif terhadap air.", "stok": 6, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Desiccator.JPG/400px-Desiccator.JPG"},
    "Erlenmeyer": {"fungsi": "Wadah mencampur larutan analit, menampung hasil titrasi, dan memanaskan cairan.", "stok": 55, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Erlenmeyer_flask_full_of_liquid.jpg/400px-Erlenmeyer_flask_full_of_liquid.jpg"},
    "Gelas Ukur": {"fungsi": "Mengukur volume larutan kimia secara makro dengan kepatuhan akurasi menengah.", "stok": 45, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Graduated_cylinder.jpg/350px-Graduated_cylinder.jpg"},
    "Gegep Besi": {"fungsi": "Menjepit buret, labu alas bulat, atau peralatan gelas lain pada tiang statif.", "stok": 25, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Retort_clamp.jpg/400px-Retort_clamp.jpg"},
    "Gegep Kayu": {"fungsi": "Menjepit tabung reaksi ketika dalam proses pemanasan di atas api.", "stok": 30, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Wooden_test_tube_holder.jpg/400px-Wooden_test_tube_holder.jpg"},
    "Hot Plate": {"fungsi": "Alat elektronik pemanas datar sekaligus mengaduk sampel secara otomatis.", "stok": 8, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Laboratory_hot_plate_stirrer.jpg/400px-Laboratory_hot_plate_stirrer.jpg"},
    "Inkubator": {"fungsi": "Menginkubasi kultur sel mikrobiologi pada kondisi suhu konstan.", "stok": 4, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Laboratory_incubator.jpg/400px-Laboratory_incubator.jpg"},
    "Jarum Ose": {"fungsi": "Mengambil mikroba atau melakukan inokulasi bakteri secara aseptik.", "stok": 20, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Inoculation_loops.jpg/400px-Inoculation_loops.jpg"},
    "Kaca Arloji": {"fungsi": "Wadah penimbangan sampel kristal padat atau penutup gelas beaker.", "stok": 35, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Watch_glass.jpg/400px-Watch_glass.jpg"},
    "Kaki Tiga": {"fungsi": "Penyangga besi melingkar tiga kaki untuk menopang wadah sampel saat pemanasan.", "stok": 20, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Laboratory_tripod.jpg/400px-Laboratory_tripod.jpg"},
    "Kasa Asbes": {"fungsi": "Meratakan rambatan panas api dari bunsen agar wadah kaca tidak pecah.", "stok": 25, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Wire_gauze.jpg/400px-Wire_gauze.jpg"},
    "Kertas Saring": {"fungsi": "Menyaring partikel residu padatan terlarut dari cairan filtrat.", "stok": 100, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Filter_paper_folded.jpg/400px-Filter_paper_folded.jpg"},
    "Labu Takar": {"fungsi": "Membuat larutan standar primer atau sekunder dengan ketelitian volume sangat tinggi.", "stok": 35, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Volumetric_flask_100ml.jpg/300px-Volumetric_flask_100ml.jpg"},
    "Mikropipet": {"fungsi": "Memindahkan cairan bervolume ultra kecil (skala mikroliter) secara akurat.", "stok": 12, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Pippete_1.jpg/400px-Pippete_1.jpg"},
    "Neraca Analitik": {"fungsi": "Mengukur berat massa substansi kimia berpresisi mikro tinggi.", "stok": 6, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Analytical_balance_mettler_ae200.jpg/400px-Analytical_balance_mettler_ae200.jpg"},
    "Oven Laboratorium": {"fungsi": "Mengeringkan peralatan gelas pasca cuci atau menghilangkan kadar air sampel.", "stok": 4, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Laboratory_drying_oven.jpg/400px-Laboratory_drying_oven.jpg"},
    "pH meter": {"fungsi": "Mengukur nilai derajat keasaman atau nilai konsentrasi ion hidrogen secara digital.", "stok": 10, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/PH_meter_01.jpg/400px-PH_meter_01.jpg"},
    "Pipet Volume": {"fungsi": "Mengambil larutan cair dengan volume tunggal spesifik berakurasi tinggi.", "stok": 40, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Volumetric_pipette_matrix.jpg/400px-Volumetric_pipette_matrix.jpg"},
    "Pipet Tetes": {"fungsi": "Memindahkan cairan reagen dalam volume sangat kecil secara tetes demi tetes.", "stok": 80, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Dropper_01.jpg/400px-Dropper_01.jpg"},
    "Pipet Mohr / Ukur": {"fungsi": "Mengambil larutan dengan rentang volume bervariasi sesuai garis tanda skala.", "stok": 30, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Graduated_pipettes.jpg/400px-Graduated_pipettes.jpg"},
    "Rak Tabung Reaksi": {"fungsi": "Tempat menata dan menegakkan posisi tabung reaksi agar tidak tumpah.", "stok": 25, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Test_tube_rack.jpg/400px-Test_tube_rack.jpg"},
    "Spatula Logam": {"fungsi": "Sendok kecil logam untuk mengambil sampel berwujud padat atau serbuk.", "stok": 40, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Lab_spatulas.jpg/400px-Lab_spatulas.jpg"},
    "Statif dan Klem": {"fungsi": "Tiang logam vertikal dasar kokoh yang menyangga dudukan klem buret.", "stok": 30, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Retort_stand.jpg/300px-Retort_stand.jpg"},
    "Tabung Reaksi": {"fungsi": "Wadah silindris kaca kecil untuk uji reaksi kualitatif zat kimia.", "stok": 120, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Test_tubes_in_rack.jpg/400px-Test_tubes_in_rack.jpg"},
    "Termometer Laboratorium": {"fungsi": "Mengukur tingkat suhu lingkungan larutan reaksi kimia.", "stok": 25, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Laboratory_thermometer.jpg/400px-Laboratory_thermometer.jpg"},
    "Water bath": {"fungsi": "Pemanas lab tidak langsung dengan media air untuk menjaga stabilitas suhu sampel.", "stok": 4, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Water_bath_laboratory.jpg/400px-Water_bath_laboratory.jpg"}
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
# MENU CEK ALAT (REVISI POIN 1: DROP-DOWN & GAMBAR ASLI)
# =====================================================
elif menu == "Cek Stok Alat Laboratorium":
    st.header("CEK STOK ALAT LABORATORIUM")
    
    # Perubahan: Menggunakan Selectbox Drop-down sesuai catatan revisi dosen
    pilihan_alat = st.selectbox("Pilih alat yang ingin dicek:", ["-- Pilih Alat --"] + alat_lab)
    
    if st.button("Cek Detail Alat"):
        if pilihan_alat != "-- Pilih Alat--":
            st.success(f"Alat '{pilihan_alat}' TERSEDIA di Laboratorium Terintegrasi")    
            
            c_img, c_fng = st.columns([1, 2])
            with c_img:
                st.image(database_alat[pilihan_alat]["img"], use_container_width=True, caption=pilihan_alat)
            with c_fng:
                st.info(f"**Fungsi Utama:** {database_alat[pilihan_alat]['fungsi']}")
                st.metric(label="Jumlah Stok Tersedia (Qty)", value=f"{database_alat[pilihan_alat]['stok']} unit")
                
            st.session_state.riwayat_pencarian.append(f"Cek Stok ➔ Alat: '{pilihan_alat}' ditemukan. Stok: {database_alat[pilihan_alat]['stok']} unit.")
        else:
            st.warning("Silakan pilih salah satu alat pada menu drop-down terlebih dahulu.")

    st.write("---")
    st.subheader("Katalog Inventaris Lengkap")
    
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
# MENU KADAR
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
# MENU pH (REVISI POIN 3: CATATAN KETERBATASAN FITUR)
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
    st.write("Semua aktivitas pencarian inventaris dan perhitungan kalkulator kimia Anda tersimpan otomatis di bawah ini.")
    
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
