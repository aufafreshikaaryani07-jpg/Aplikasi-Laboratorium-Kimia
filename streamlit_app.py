import streamlit as st
import math

# Set konfigurasi halaman utama Streamlit
st.set_page_config(page_title="Aplikasi Laboratorium Kimia", layout="wide")

# --- NAVIGASI MENU UTAMA (SIDEBAR) ---
menu = st.sidebar.radio(
    "MENU UTAMA",
    ["Katalog & Cek Stok Alat", "Kalkulator Kadar", "Kalkulator pH", "Informasi Creator"]
)

# ==============================================================================
# 1. MENU: KATALOG & CEK STOK ALAT LABORATORIUM
# ==============================================================================
if menu == "Katalog & Cek Stok Alat":
    st.header("📋 Katalog Inventaris Lengkap (Urutan Abjad A-Z)")
    st.write("Silakan cek detail fungsi dan status ketersediaan alat laboratorium di bawah ini.")

    # Data Inventaris Alat (Silakan sesuaikan nilai stoknya jika diperlukan)
    inventaris_alat = {
        "Alu dan Mortar": {"stok": 15, "deskripsi": "Menghancurkan atau menghaluskan sampel padat laboratorium."},
        "Batang Pengaduk": {"stok": 40, "deskripsi": "Mengaduk larutan kimia agar komponen zat terlarut dapat tercampur homogen."},
        "Buret": {"stok": 0, "deskripsi": "Digunakan untuk titrasi dengan presisi tinggi."},
        "Cawan Petri": {"stok": 0, "deskripsi": "Wadah untuk membiakkan sel atau mikroba."}
    }

    # Menampilkan data secara berurutan abjad A-Z
    for alat, info in sorted(inventaris_alat.items()):
        with st.expander(f"📦 {alat} (Stok: {info['stok']} Unit)"):
            st.write(f"**Deskripsi Fungsi:** {info['deskripsi']}")
            
            # --- JANGAN DIHAPUS: Logika Pengecekan Stok & Status Ketersediaan ---
            if info['stok'] > 0:
                st.success(f"✔️ Status Ketersediaan: {info['stok']} unit siap digunakan praktikum.")
            else:
                # Mengembalikan pernyataan "TIDAK TERSEDIA" jika stok habis / bernilai 0
                st.error("❌ Status Ketersediaan: Gambar tidak ditemukan / Alat TIDAK TERSEDIA (Stok Habis).")


# ==============================================================================
# 2. MENU: KALKULATOR KADAR ANALISIS VOLUMETRI
# ==============================================================================
elif menu == "Kalkulator Kadar":
    st.header("🧮 Kalkulator Kadar Analisis Volumetri")
    
    # Dropdown pilihan jenis kadar di halaman utama
    jenis_kadar = st.selectbox(
        "Pilih Jenis Kadar:",
        ["Kadar Asam Asetat", "Kadar NaOH", "Kadar HCl"]
    )

    # --- PERBAIKAN DINAMIS: Kotak biru di sidebar menyesuaikan pilihan ---
    with st.sidebar:
        # Membuat kotak visual berwarna biru
        st.markdown("""
        <div style='background-color: #e8f0fe; padding: 15px; border-radius: 10px; border-left: 5px solid #1a73e8;'>
            <h4 style='color: #1a73e8; margin-top:0;'>ℹ️ Pengertian:</h4>
            <p style='color: #333; font-size: 14px;'>Digunakan untuk mengukur persentase kandungan fraksi zat analit tertentu di dalam sampel melalui teknik volumetri.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("") # Jarak komponen
        
        # Menampilkan Rumus Utama Konten yang BERUBAH OTOMATIS (Sama dengan di sampingnya)
        st.info("📝 **Rumus Kadar (Menyesuaikan Pilihan):**")
        if jenis_kadar == "Kadar Asam Asetat":
            st.latex(r"\%Kadar\ Asam\ Asetat = \frac{V \times N \times 60 \times 10^{-3} \times FP \times 100}{V_{sampel}}")
        elif jenis_kadar == "Kadar NaOH":
            st.latex(r"\%Kadar\ NaOH = \frac{V \times N \times 40 \times 10^{-3} \times FP \times 100}{V_{sampel}}")
        elif jenis_kadar == "Kadar HCl":
            st.latex(r"\%Kadar\ HCl = \frac{V \times N \times 36.5 \times 10^{-3} \times FP \times 100}{V_{sampel}}")

    # Konten Input Data di Halaman Utama
    st.subheader(f"Form Input Perhitungan: {jenis_kadar}")
    col1, col2 = st.columns(2)
    with col1:
        V_titrasi = st.number_input("Volume titrasi / V (mL):", min_value=0.0, step=0.1, format="%.2f")
        N_titran = st.number_input("Normalitas / N (mgrek/mL):", min_value=0.0, step=0.0001, format="%.4f")
    with col2:
        FP = st.number_input("Faktor pengenceran (FP):", min_value=1.0, step=1.0, value=1.0)
        V_sampel = st.number_input("Volume sampel (mL):", min_value=0.1, step=0.1, value=1.0, format="%.2f")

    # Tombol Hitung
    if st.button("Hitung Kadar Sekarang"):
        # Menentukan nilai Berat Ekuivalen (BE) secara otomatis berdasarkan pilihan
        be_zat = 60 if jenis_kadar == "Kadar Asam Asetat" else (40 if jenis_kadar == "Kadar NaOH" else 36.5)
        if V_sampel > 0:
            hasil_kadar = (V_titrasi * N_titran * be_zat * 10**-3 * FP * 100) / V_sampel
            st.success(f"🎉 Hasil Perhitungan {jenis_kadar} = {hasil_kadar:.4f} %")
        else:
            st.error("Volume sampel tidak boleh nol!")


# ==============================================================================
# 3. MENU: KALKULATOR pH (MENGEMBALIKAN PERNYATAAN & SINGKAT CATATAN)
# ==============================================================================
elif menu == "Kalkulator pH":
    st.header("🧪 Kalkulator pH Larutan")
    
    # --- MENGEMBALIKAN PERNYATAAN: Dropdown pilihan karakteristik lengkap kembali ---
    jenis_larutan = st.selectbox(
        "Pilih Karakteristik Larutan:",
        ["Asam Kuat", "Asam Lemah", "Basa Kuat", "Basa Lemah"]
    )

    # Input Konsentrasi (Molaritas) Umum
    M = st.number_input("Konsentrasi Larutan / M (mol/L):", min_value=0.0, step=0.0001, format="%.4f")

    # Logika Perhitungan per Jenis Larutan beserta Penyederhanaan Catatan
    if jenis_larutan == "Asam Kuat":
        valensi = st.number_input("Valensi Asam (Jumlah H+):", min_value=1, step=1, value=1)
        if M > 0:
            H_plus = M * valensi
            pH = -math.log10(H_plus)
            st.success(f"🔹 **Pernyataan Sifat: Asam Kuat** | Nilai pH = {pH:.2f}")
            
            # Catatan kalimat disingkat, diperbaiki penyusunannya agar mudah dipahami
            st.info("**Catatan Pengguna:**\n* Asam Kuat terionisasi sempurna dalam air.\n* Semakin tinggi konsentrasi ion $H^+$, nilai pH akan semakin kecil (mendekati 0).")

    elif jenis_larutan == "Asam Lemah":
        Ka = st.number_input("Konstanta Asam (Ka):", min_value=0.0, step=1e-6, format="%.2e")
        if M > 0 and Ka > 0:
            H_plus = math.sqrt(Ka * M)
            pH = -math.log10(H_plus)
            st.success(f"🔹 **Pernyataan Sifat: Asam Lemah** | Nilai pH = {pH:.2f}")
            
            st.info("**Catatan Pengguna:**\n* Asam Lemah hanya terionisasi sebagian.\n* Nilai pH ditentukan oleh besarnya tetapan ionisasi ($K_a$) dan konsentrasi larutan.")

    elif jenis_larutan == "Basa Kuat":
        valensi = st.number_input("Valensi Basa (Jumlah OH-):", min_value=1, step=1, value=1)
        if M > 0:
            OH_minus = M * valensi
            pOH = -math.log10(OH_minus)
            pH = 14 - pOH
            st.success(f"🔹 **Pernyataan Sifat: Basa Kuat** | Nilai pH = {pH:.2f}")
            
            st.info("**Catatan Pengguna:**\n* Basa Kuat terionisasi sempurna dalam air.\n* Semakin besar konsentrasi ion $OH^-$, nilai pH akan semakin tinggi (mendekati 14).")

    elif jenis_larutan == "Basa Lemah":
        Kb = st.number_input("Konstanta Basa (Kb):", min_value=0.0, step=1e-6, format="%.2e")
        if M > 0 and Kb > 0:
            OH_minus = math.sqrt(Kb * M)
            pOH = -math.log10(OH_minus)
            pH = 14 - pOH
            st.success(f"🔹 **Pernyataan Sifat: Basa Lemah** | Nilai pH = {pH:.2f}")
            
            st.info("**Catatan Pengguna:**\n* Basa Lemah hanya terionisasi sebagian.\n* Nilai pH dipengaruhi oleh kekuatan tetapan ionisasi ($K_b$) dan kadar konsentrasinya.")


# ==============================================================================
# 4. MENU: INFORMASI CREATOR
# ==============================================================================
elif menu == "Informasi Creator":
    st.header("👤 INFORMASI CREATOR")
    
    col_foto, col_data = st.columns([1, 2])
    
    with col_foto:
        try:
            st.image("foto kelompok.jpg", use_container_width=True, caption="Kelompok 12_1D Politeknik AKA Bogor")
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
