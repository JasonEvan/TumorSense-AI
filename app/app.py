import streamlit as st
from PIL import Image
from load_model import load_model
from model_inference import predict

model = load_model()

st.set_page_config(
    page_title="TumorSense AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def home_page():
    st.markdown("""
        <div style="text-align: center;">
            <h2>TumorSense AI</h2>
            <h5>Sistem deteksi tumor otak cerdas berbasis CNN</h5>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    **TumorSense** hadir untuk membantu radiolog dan tenaga medis dalam melakukan screening awal citra MRI otak. Sistem ini dilatih menggunakan ribuan data citra medis untuk mengenali pola tumor.
    
    **Fitur Utama:**
    - ✅ **Klasifikasi Otomatis**: Membedakan glioma, meningioma, pituitari, dan non-tumor.
    - ⚡️ **Proses Cepat**: Hasil analisis dalam hitungan detik.
    - 🔑 **Keamanan Data**: Data diproses secara lokal
    """)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    col1.metric("Akurasi Model", "98.2%", "+18%")
    col2.metric("Waktu Respon", "2 detik", "-1.5 detik")
    col3.metric("Total Dataset", "6000+", "+1200")

def detect_tumor_page():
    st.markdown("""
    # Deteksi Tumor Otak
    Unggah citra MRI otak Anda untuk analisis cepat dan akurat.
    """)

    f = st.file_uploader('Unggah MRI Anda di sini', ['jpg', 'png', 'jpeg'], accept_multiple_files=False)

    if f is not None:
        img = Image.open(f)

        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            analyze_button = st.button("🔍 Analisis MRI Sekarang", type='primary')

        if analyze_button:
            predicted_class = predict(model, img)
            st.success("Analisis berhasil!")

            res_col1, res_col2 = st.columns(2, gap="large")
            with res_col1:
                st.markdown("### Citra Asli")
                st.image(img, width="stretch", caption="Input MRI")

            with res_col2:
                st.markdown("### Prediksi")
                st.info(predicted_class)

    st.markdown("---")

def tumor_info_page():
    st.markdown("""
    # 📚 Informasi Tumor Otak
    Pelajari lebih lanjut tentang berbagai jenis tumor otak, gejala, dan opsi pengobatan.
    """)

    tab1, tab2, tab3 = st.tabs(["Glioma", "Meningioma", "Pituitary"])
    with tab1:
        st.markdown("""
        ### Glioma
        Glioma adalah jenis tumor otak yang berasal dari sel glial. Tumor ini dapat bersifat jinak atau ganas.
        
        **Gejala Umum:**
        - Sakit kepala
        - Mual dan muntah
        - Perubahan kepribadian
        
        **Opsi Pengobatan:**
        - Pembedahan
        - Radioterapi
        - Kemoterapi
        """)

    with tab2:
        st.markdown("""
        ### Meningioma
        Meningioma adalah tumor yang berkembang dari meninges, lapisan pelindung otak dan sumsum tulang belakang.
        
        **Gejala Umum:**
        - Sakit kepala
        - Gangguan penglihatan
        - Kelemahan otot
        
        **Opsi Pengobatan:**
        - Pembedahan
        - Radioterapi
        """)
    
    with tab3:
        st.markdown("""
        ### Pituitary
        Tumor pituitari berkembang di kelenjar pituitari yang mengatur hormon dalam tubuh.
        
        **Gejala Umum:**
        - Gangguan penglihatan
        - Perubahan menstruasi
        - Kelelahan
        
        **Opsi Pengobatan:**
        - Pembedahan
        - Terapi hormon
        - Radioterapi
        """)

def about_us_page():
    st.markdown("""
    ## ℹ️ Tentang TumorSense
    ### 🎯 Tujuan
    - Memberikan alat bantu deteksi dini tumor otak yang cepat dan akurat, mendukung tenaga medis dalam pengambilan keputusan klinis
    - Meningkatkan kesadaran tentang pentingnya deteksi dini tumor otak melalui teknologi AI
    - Mendorong penelitian lebih lanjut dalam aplikasi AI untuk diagnosis medis
                
    ### 👨‍💻 Teknologi
    - Model: Convolutional Neural Networks (YOLOv8 Pretrained models)
    - Framework: Streamlit untuk antarmuka pengguna yang interaktif
    - Bahasa Pemrograman: Python

    ### 📊 Dataset
    - Sumber: Kaggle Brain Tumor MRI Dataset
    - Jumlah Data: 6000+ citra MRI otak dengan berbagai kelas tumor
    - Pra-pemrosesan: Normalisasi, augmentasi data untuk meningkatkan performa model
    """)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=80)
    st.title("Navigasi Halaman")

    selected = st.radio(
        "Pilih halaman:",
        ("🏠 Beranda", "🧠 Deteksi Tumor", "📊 Informasi Tumor", "ℹ️ Tentang Kami")
    )

    st.markdown("---")
    st.caption("Powered by YOLOv8 & Streamlit")

if selected == "🏠 Beranda":
    home_page()
elif selected == "🧠 Deteksi Tumor":
    detect_tumor_page()
elif selected == "📊 Informasi Tumor":
    tumor_info_page()
elif selected == "ℹ️ Tentang Kami":
    about_us_page()