import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Alzheimer Classification", layout="centered", page_icon="🧠")

# --- FIX: DUMMY FUNCTION ---
def dummy_preprocess(x):
    return x

# --- FUNGSI LOAD MODEL ---
@st.cache_resource
def load_all_models(model_choice):
    custom_objects = {
        "Lambda": tf.keras.layers.Lambda,
        "preprocess_input": dummy_preprocess 
    }
    
    try:
        if model_choice == "Base CNN (Custom)":
            return tf.keras.models.load_model('models/model_alzheimer_base.h5')
        elif model_choice == "MobileNetV2 (Pretrained)":
            return tf.keras.models.load_model('models/model_alzheimer_mobilenet.keras', custom_objects=custom_objects)
        elif model_choice == "ResNet50 (Pretrained)":
            return tf.keras.models.load_model('models/model_alzheimer_resnet_optimized.keras', custom_objects=custom_objects)
    except Exception as e:
        st.error(f"Gagal memuat model {model_choice}: {e}")
        return None

# Daftar Kelas
class_names = ['Mild Demented', 'Moderate Demented', 'Non Demented', 'Very Mild Demented']

# --- UI STREAMLIT ---
st.title("🧠 Deteksi Stadium Alzheimer")
st.write("Aplikasi Deep Learning untuk klasifikasi citra MRI otak.")

st.sidebar.header("Pengaturan Model")
selected_model_name = st.sidebar.selectbox(
    "Pilih Arsitektur Model:",
    ("Base CNN (Custom)", "MobileNetV2 (Pretrained)", "ResNet50 (Pretrained)")
)

model = load_all_models(selected_model_name)

uploaded_file = st.file_uploader("Unggah gambar MRI otak (Format: JPG, PNG, JPEG)", type=["jpg", "png", "jpeg"])

if uploaded_file is not None and model is not None:
    col1, col2 = st.columns(2)
    
    with col1:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption="Gambar Terunggah", use_container_width=True)

    # --- PROSES PREPROCESSING & PREDIKSI ---
    with st.spinner('Sedang menganalisis...'):
        # 1. Resize
        img = image.resize((224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        
        # 2. Preprocessing Manual berdasarkan Model
        if selected_model_name == "MobileNetV2 (Pretrained)":
            img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
        elif selected_model_name == "ResNet50 (Pretrained)":
            img_array = tf.keras.applications.resnet50.preprocess_input(img_array)
        else:
            img_array = img_array / 255.0
        
        # 3. Prediksi (MENGGUNAKAN CALL BUKAN PREDICT UNTUK MENGHINDARI BUG TENSOR)
        try:
            # Memanggil model secara langsung lebih stabil untuk Keras 3
            preds_tensor = model(img_array, training=False)
            predictions = preds_tensor.numpy() if hasattr(preds_tensor, 'numpy') else preds_tensor
            
            result_index = np.argmax(predictions[0])
            confidence = np.max(predictions[0]) * 100
            
            with col2:
                st.subheader("Hasil Analisis")
                st.info(f"**Model:** {selected_model_name}")
                st.success(f"**Prediksi:** {class_names[result_index]}")
                st.metric(label="Tingkat Keyakinan", value=f"{confidence:.2f}%")
                
        except Exception as e:
            st.error(f"Terjadi kesalahan saat prediksi: {e}")

# Footer
st.markdown("---")
st.caption("Catatan: Aplikasi ini hanya untuk keperluan edukasi/UAP.")