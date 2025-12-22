import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Konfigurasi Halaman
st.set_page_config(page_title="Alzheimer Classification", layout="centered")

# --- FUNGSI LOAD MODEL ---
@st.cache_resource
def load_all_models(model_choice):
    # Tambahkan path folder 'models/' sebelum nama file
    if model_choice == "Base CNN (Custom)":
        return tf.keras.models.load_model('models/model_alzheimer_base.h5')
    elif model_choice == "MobileNetV2 (Pretrained)":
        return tf.keras.models.load_model('models/model_alzheimer_mobilenet.keras')
    elif model_choice == "ResNet50 (Pretrained)":
        return tf.keras.models.load_model('models/model_alzheimer_resnet_optimized.keras')

# Daftar Kelas (Pastikan urutan sesuai dengan alfabet folder dataset Anda)
class_names = ['Mild Demented', 'Moderate Demented', 'Non Demented', 'Very Mild Demented']

# --- UI STREAMLIT ---
st.title("🧠 Deteksi Stadium Alzheimer")
st.write("Aplikasi ini menggunakan Deep Learning untuk mengklasifikasi citra MRI otak ke dalam 4 stadium Alzheimer.")

# Sidebar untuk memilih model
st.sidebar.header("Pengaturan Model")
selected_model_name = st.sidebar.selectbox(
    "Pilih Arsitektur Model:",
    ("Base CNN (Custom)", "MobileNetV2 (Pretrained)", "ResNet50 (Pretrained)")
)

# Load model yang dipilih
model = load_all_models(selected_model_name)

# Upload File
uploaded_file = st.file_uploader("Unggah gambar MRI otak (Format: JPG, PNG, JPEG)", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Tampilkan Gambar
    col1, col2 = st.columns(2)
    
    with col1:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption="Gambar Terunggah", use_container_width=True)

    # Preprocessing
    with st.spinner('Sedang menganalisis...'):
        # Resize sesuai input model saat training (224x224)
        img = image.resize((224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        
        # Prediksi
        predictions = model.predict(img_array)
        
        # Karena kita menggunakan softmax di layer terakhir, ambil probabilitas tertinggi
        result_index = np.argmax(predictions[0])
        confidence = np.max(predictions[0]) * 100

    with col2:
        st.subheader("Hasil Analisis")
        st.info(f"**Model:** {selected_model_name}")
        st.success(f"**Prediksi:** {class_names[result_index]}")
        st.metric(label="Tingkat Keyakinan", value=f"{confidence:.2f}%")

# Footer
st.markdown("---")
st.caption("Catatan: Aplikasi ini hanya untuk keperluan edukasi/UAP dan bukan alat diagnosa medis resmi.")