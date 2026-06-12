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

st.markdown("""
<style>    
.main{    
    background: linear-gradient(135deg,#f8fbff,#edf6ff);    
}    
[data-testid="stSidebar"]{    
    background: linear-gradient(180deg,#001845,#023e8a,#0077b6);    
}    
[data-testid="stSidebar"] p, [data-testid="stSidebar"] label {    
    color: white !important;    
}    
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
        "Creator"
    ]
)

# =====================================================
# MENAMPILKAN RUMUS DI SIDEBAR
# =====================================================
if menu == "Kalkulator Molaritas":
    st.sidebar.markdown('<div class="penjelasan-sidebar"><strong>🧪 Rumus Molaritas:</strong></div>', unsafe_allow_html=True)
    st.sidebar.latex(r"M = \frac{n}{V}")

elif menu == "Kalkulator Pengenceran":
    st.sidebar.markdown('<div class="penjelasan-sidebar"><strong>🧪 Rumus Pengenceran:</strong></div>', unsafe_allow_html=True)
    st.sidebar.latex(r"M_1 \times V_1 = M_2 \times V_2")

elif menu == "Kalkulator Kadar":
    st.sidebar.markdown('<div class="penjelasan-sidebar"><strong>🧪 Rumus Kadar Umum:</strong></div>', unsafe_allow_html=True)
    st.sidebar.latex(r"\% \text{Kadar} = \frac{(V \times N \times BE) \times 10^{-3} \times FP \times 100}{V_{\text{sampel}}}")

elif menu == "Kalkulator pH":
    st.sidebar.markdown('<div class="penjelasan-sidebar"><strong>🧪 Rumus pH:</strong></div>', unsafe_allow_html=True)
    st.sidebar.latex(r"\text{pH} = -\log_{10}[H^+]")

# =====================================================
# DATABASE INVENTARIS ALAT LAB
# =====================================================
img_placeholder = "https://cdn-icons-png.flaticon.com/512/3655/3655581.png"
alat_lab = ["Alu dan Mortar", "Batang Pengaduk", "Beaker Glass", "Buret", "Erlenmeyer", "Gelas Ukur", "Tabung Reaksi"]

# =====================================================
# HOME
# =====================================================
if menu == "Home":
    st.markdown("""
    <div class="hero">    
    <h1>🧪 MOLEVIA</h1>    
    <h3>The Pathway Through Chemistry</h3>    
    </div>    
    """, unsafe_allow_html=True)    
    st.image("https://images.unsplash.com/photo-1579165466741-7f35e4755660", use_container_width=True)

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
                st.image(img_placeholder, use_container_width=True)
            with c_fng:
                st.info(f"Peralatan gelas laboratorium siap digunakan untuk keperluan praktikum mahasiswa.")

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
    st.header("KALKULATOR KADAR")
    pilihan = st.selectbox("Pilih Jenis Kadar", ["Kadar Asam Asetat", "Kadar Besi(Fe)"])

    if pilihan == "Kadar Asam Asetat":
        V = st.number_input("Volume titrasi / V (mL)")    
        N = st.number_input("Normalitas / N (mgrek/mL)")    
        FP = st.number_input("Faktor pengenceran (FP)", min_value=1.0, value=1.0)    
        V_sampel = st.number_input("Volume sampel (mL)", min_value=0.1, value=1.0)    
        if st.button("Hitung Kadar"):    
            hasil = ((V * N * 60) * (10**-3) * FP * 100) / V_sampel    
            st.success(f"Kadar CH3COOH = {round(hasil,2)} %")

    elif pilihan == "Kadar Besi(Fe)":
        V = st.number_input("Volume titrasi / V (mL)")    
        N = st.number_input("Normalitas / N (mgrek/mL)")    
        V_sampel = st.number_input("Volume sampel (mL)", min_value=0.1, value=1.0)    
        if st.button("Hitung Kadar"):    
            hasil = ((V * N * 56) * (10**-3) * 100) / V_sampel    
            st.success(f"Kadar Fe = {round(hasil,2)} %")

# =====================================================
# MENU pH
# =====================================================
elif menu == "Kalkulator pH":
    st.header("KALKULATOR pH")
    h_input = st.text_input("Masukkan konsentrasi H+ (contoh: 0.0001)", value="0.0001")
    if st.button("Hitung pH"):
        try:    
            h = float(h_input)    
            ph = round(-math.log10(h), 2)    
            st.success(f"pH = {ph}")    
        except:    
            st.error("Masukkan angka desimal yang valid!")

# =====================================================
# MENU CREATOR (MEMANGGIL FOTO ASLI KELOMPOK DARI GITHUB)
# =====================================================
elif menu == "Creator":
    st.header("👤 INFORMASI CREATOR")
    col_foto, col_data = st.columns([1, 1])
    
    with col_foto:
        try:
            # Memanggil file foto_kelompok.jpg yang telah Anda unggah
            st.image("foto_kelompok.jpg", use_container_width=True, caption="Tim Kelompok 12_1D Politeknik AKA Bogor")
        except:
            st.error("File 'foto_kelompok.jpg' belum terdeteksi. Silakan upload fotonya terlebih dahulu ke GitHub.")
        
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
