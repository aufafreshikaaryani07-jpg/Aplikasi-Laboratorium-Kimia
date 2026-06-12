import streamlit as st
import math

# Set konfigurasi halaman streamlit
st.set_page_config(page_title="Aplikasi Laboratorium Kimia", layout="wide")

# --- NAVIGASI MENU UTAMA ---
menu = st.sidebar.radio(
    "MENU UTAMA",
    ["Katalog & Stok Alat", "Kalkulator Kadar Volumetri", "Kalkulator pH", "Informasi Creator"]
)

# ==============================================================================
# 1. MENU: KATALOG & STOK ALAT LABORATORIUM
# ==============================================================================
if menu == "Katalog & Stok Alat":
    st.header("📋 Katalog Inventaris Lengkap & Cek Stok")
    st.write("Berikut adalah daftar alat laboratorium beserta status ketersediaannya.")

    # Data contoh inventaris alat (Sesuaikan dengan data asli Anda)
    inventaris_alat = {
        "Alu dan Mortar": {"stok": 15, "deskripsi": "Menghancurkan atau menghaluskan sampel padat laboratorium."},
        "Batang Pengaduk": {"stok": 40, "deskripsi": "Mengaduk larutan kimia agar komponen zat terlarut dapat tercampur homogen."},
        "Buret": {"stok": 0, "deskripsi": "Digunakan untuk titrasi dengan presisi tinggi."},
        "Cawan Petri": {"stok": 10, "deskripsi": "Wadah untuk membiakkan sel atau mikroba."}
    }

    # Tampilan katalog urutan abjad A-Z
    for alat, info in sorted(inventaris_alat.items()):
        with st.expander(f"📦 {alat} (Stok: {info['stok']} Unit)"):
            st.write(f"**Deskripsi Fungsi:** {info['deskripsi']}")
            
            # --- PERBAIKAN: Mengembalikan pernyataan ketersediaan & stok ---
            if info['stok'] > 0:
                st.success(f"✔️ Status Ketersediaan: {info['stok']} unit siap digunakan praktikum.")
            else:
                # Menampilkan peringatan jika stok habis / 0
                st.error("❌ Status Ketersediaan: Maaf, alat ini TIDAK TERSEDIA (Stok Habis).")


# ==============================================================================
# 2. MENU: KALKULATOR KADAR ANALISIS VOLUMETRI
# ==============================================================================
elif menu == "Kalkulator Kadar Volumetri":
    st.header("🧮 Kalkulator Kadar Analisis Volumetri")
    
    # Pilih Jenis Kadar di Halaman Utama
    jenis_kadar = st.selectbox(
        "Pilih Jenis Analisis Kadar:",
        ["Kadar Asam Asetat", "Kadar NaOH", "Kadar HCl"]
    )

    # --- PERBAIKAN: Rumus di bagian biru (sidebar) dinamis mengikuti pilihan ---
    with st.sidebar:
        st.markdown("<div style='background-color: #e8f0fe; padding: 15px; border-radius: 10px; border-left: 5px solid #1a73e8;'>", unsafe_allow_html=True)
        st.subheader("🔷 info Pengertian")
        st.write("Mengukur persentase kandungan fraksi zat analit tertentu dalam sampel melalui teknik volumetri.")
        
        st.subheader("📝 Rumus Utama Konten:")
        if jenis_kadar == "Kadar Asam Asetat":
            st.latex(r"\%Kadar = \frac{V \times N \times 60 \times 10^{-3} \times FP \times 100}{V_{sampel}}")
        elif jenis_kadar == "Kadar NaOH":
            st.latex(r"\%Kadar = \frac{V \times N \times 40 \times 10^{-3} \times FP \times 100}{V_{sampel}}")
        elif jenis_kadar == "Kadar HCl":
            st.latex(r"\%Kadar = \frac{V \times N \times 36.5 \times 10^{-3} \times FP \times 100}{V_{sampel}}")
        st.markdown("</div>", unsafe_allow_html=True)

    # Input form parameter perhitungan di halaman utama
    col1, col2 = st.columns(2)
    with col1:
        V_titrasi = st.number_input("Volume titrasi / V (mL):", min_value=0.0, step=0.1, format="%.2f")
        N_titran = st.number_input("Normalitas / N (mgrek/mL):", min_value=0.0, step=0.0001, format="%.4f")
    with col2:
        FP = st.number_input("Faktor pengenceran (FP):", min_value=1.0, step=1.0, value=1.0)
        V_sampel = st.number_input("Volume sampel (mL):", min_value=0.1, step=0.1, value=1.0, format="%.2f")

    # Proses Hitung Rumus
    if st.button("Hitung Kadar"):
        be_zat = 60 if jenis_kadar == "Kadar Asam Asetat" else (40 if jenis_kadar == "Kadar NaOH" else 36.5)
        if V_sampel > 0:
            kadar = (V_titrasi * N_titran * be_zat * 10**-3 * FP * 100) / V_sampel
            st.success(f"Hasil Perhitungan {jenis_kadar} = {kadar:.4f} %")
        else:
            st.error("Volume sampel harus lebih besar dari 0!")


# ==============================================================================
# 3. MENU: KALKULATOR pH (PERBAIKAN PERNYATAAN & CATATAN)
# ==============================================================================
elif menu == "Kalkulator pH":
    st.header("🧪 Kalkulator pH Larutan")
    
    # --- PERBAIKAN: Pernyataan jenis larutan lengkap kembali ---
    jenis_larutan = st.selectbox(
        "Pilih Jenis Karakteristik Larutan:",
        ["Asam Kuat", "Asam Lemah", "Basa Kuat", "Basa Lemah"]
    )

    # Input konsentrasi umum
    M = st.number_input("Konsentrasi Larutan / M (mol/L):", min_value=0.0, step=0.0001, format="%.4f")

    if jenis_larutan == "Asam Kuat":
        valensi = st.number_input("Valensi Asam (Jumlah H+):", min_value=1, step=1, value=1)
        if M > 0:
            H_plus = M * valensi
            pH = -math.log10(H_plus)
            st.success(f"**Sifat: Asam Kuat** | Nilai pH = {pH:.2f}")
            
            # Catatan disingkat & diperbaiki susunannya agar mudah dipahami
            st.info("**Catatan Pengguna:**\n* Asam Kuat terionisasi sempurna dalam air.\n* Semakin tinggi kadar konsentrasi $H^+$, nilai pH akan semakin kecil mendekati 0.")

    elif jenis_larutan == "Asam Lemah":
        Ka = st.number_input("Konstanta Asam (Ka):", min_value=0.0, step=1e-6, format="%.2e")
        if M > 0 and Ka > 0:
            H_plus = math.sqrt(Ka * M)
            pH = -math.log10(H_plus)
            st.success(f"**Sifat: Asam Lemah** | Nilai pH = {pH:.2f}")
            
            st.info("**Catatan Pengguna:**\n* Asam Lemah hanya terionisasi sebagian di dalam air.\n* Nilai pH sangat bergantung pada nilai tetapan ionisasi ($K_a$) besarnya konsentrasi zat.")

    elif jenis_larutan == "Basa Kuat":
        valensi = st.number_input("Valensi Basa (Jumlah OH-):", min_value=1, step=1, value=1)
        if M > 0:
            OH_minus = M * valensi
            pOH = -math.log10(OH_minus)
            pH = 14 - pOH
            st.success(f"**Sifat: Basa Kuat** | Nilai pH = {pH:.2f}")
            
            st.info("**Catatan Pengguna:**\n* Basa Kuat terionisasi sempurna dalam air.\n* Semakin tinggi konsentrasi ion $OH^-$, pH akan semakin besar mendekati nilai 14.")

    elif jenis_larutan == "Basa Lemah":
        Kb = st.number_input("Konstanta Basa (Kb):", min_value=0.0, step=1e-6, format="%.2e")
        if M > 0 and Kb > 0:
            OH_minus = math.sqrt(Kb * M)
            pOH = -math.log10(OH_minus)
            pH = 14 - pOH
            st.success(f"**Sifat: Basa Lemah** | Nilai pH = {pH:.2f}")
            
            st.info("**Catatan Pengguna:**\n* Basa Lemah hanya terionisasi sebagian di dalam air.\n* Nilai pH dipengaruhi oleh kekuatan tetapan ionisasi ($K_b$) larutan tersebut.")


# ==============================================================================
# 4. MENU: INFORMASI CREATOR
# ==============================================================================
elif menu == "Informasi Creator":
    st.header("👤 INFORMASI CREATOR")
    
    col_foto, col_data = st.columns([1, 2])
    
    with col_foto:
        # Menggunakan blok try-except sesuai dengan skrip dasar Anda untuk menghindari error gambar hancur
        try:
            st.image("foto kelompok.jpg", use_container_width=True, caption="Tim Kelompok 12_1D Politeknik AKA Bogor")
        except:
            st.error("File 'foto kelompok.jpg' belum terdeteksi di repositori Anda.")
            
    with col_data:
        st.markdown("""
        <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; border: 1px solid #ddd;'>
            <h3 style='color: #1a73e8; margin-top:0;'>🚀 Kelompok 12_1D</h3>
            <h4 style='color: #5f6368;'>Politeknik AKA Bogor</h4>
            <hr style='border: 0; border-top: 1px solid #eee;'>
            <p><b>Anggota Tim Pengembang:</b></p>
            <ul>
                <li><strong>Aufa Freshika Aryani</strong> (NIM : 2560588)</li>
                <li><strong>Aura Halimah Natanegoro</strong> (NIM : 2560589)</li>
                <li><strong>Ayu Asyfa Mei Asyhari</strong> (NIM : 2560593)</li>
                <li><strong>Oscar Tirta Sugema</strong> (NIM : 2560735)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
