import streamlit as st
import os

# Set environment agar Keras menggunakan backend TensorFlow
os.environ["KERAS_BACKEND"] = "tensorflow"

import keras
import numpy as np
import pandas as pd
from PIL import Image
import json
import plotly.express as px

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Neuro-Diagnostic Lab | Alzheimer Analysis",
    layout="wide",
    page_icon="🧠"
)

# --- STYLE CSS (Professional Academic Look) ---
st.markdown("""
    <style>
    .stMainContainer { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; border: 1px solid #e0e0e0; padding: 20px; border-radius: 12px; }
    .stSidebar { background-color: #ffffff; border-right: 1px solid #eee; }
    h1 { color: #1e3a8a; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

# --- KONFIGURASI JALUR MODEL ---
MODEL_DIR = "models"
MODEL_PATHS = {
    "Base CNN (Custom)": f"{MODEL_DIR}/model_alzheimer_base.keras",
    "MobileNetV2 (Pretrained)": f"{MODEL_DIR}/model_alzheimer_mobilenet.keras",
    "VGG16 (Pretrained)": f"{MODEL_DIR}/vgg16_best_model.keras"
}

STADIUM_DESC = {
    'Non Demented': 'Kognisi Normal: Tidak ada indikasi atrofi serebral yang signifikan.',
    'Very Mild Demented': 'Sangat Ringan: Kerusakan kognitif minimal (MCI).',
    'Mild Demented': 'Ringan: Gangguan memori mulai mengganggu rutinitas harian.',
    'Moderate Demented': 'Sedang: Penurunan fungsi otak signifikan, butuh pendampingan.'
}

# --- FUNGSI CORE (Keras 3 Compatible) ---
@st.cache_resource
def load_alz_model(model_key):
    try:
        # Tambahkan safe_mode=False untuk mengizinkan layer Lambda
        return keras.models.load_model(
            MODEL_PATHS[model_key], 
            compile=False, 
            safe_mode=False
        )
    except Exception as e:
        st.error(f"Gagal memuat {model_key}: {str(e)}")
        return None

def preprocess_image_keras3(image, model_name):
    # Menggunakan utility Keras 3 untuk konversi array
    img = image.convert('RGB').resize((224, 224))
    img_array = keras.utils.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    
    if "MobileNetV2" in model_name:
        return keras.applications.mobilenet_v2.preprocess_input(img_array)
    elif "VGG16" in model_name:
        return keras.applications.vgg16.preprocess_input(img_array)
    else:
        # Normalisasi manual 0-1 untuk Base CNN
        return img_array / 255.0

# Load Label Kelas
try:
    with open(f'{MODEL_DIR}/class_names', 'r') as f:
        class_names = json.load(f)
except:
    class_names = ['Mild Demented', 'Moderate Demented', 'Non Demented', 'Very Mild Demented']

# --- SIDEBAR & NAVIGASI ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2491/2491314.png", width=80)
    st.title("Sistem Diagnosa")
    st.markdown("---")
    
    analysis_mode = st.radio("Metode Analisis", ["Analisis Tunggal", "Analisis Batch (Banyak)"])
    model_option = st.selectbox("Arsitektur Model", ["Bandingkan Semua Model"] + list(MODEL_PATHS.keys()))
    
    st.markdown("---")
    st.caption("Backend: Keras 3.10.0 + TF 2.19.0")

# --- KONTEN UTAMA ---
st.title("🧠 Alzheimer Disease Stage Diagnostics")
st.write("Interpretasi citra MRI untuk klasifikasi stadium patologis neurodegeneratif.")

if analysis_mode == "Analisis Tunggal":
    uploaded_file = st.file_uploader("Pilih file gambar MRI (JPG/PNG)", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        col1, col2 = st.columns([1, 1], gap="large")
        image = Image.open(uploaded_file)
        
        with col1:
            st.image(image, caption="Citra MRI Pasien", use_container_width=True)
            
        with col2:
            st.subheader("📝 Resume Diagnosa")
            
            models_to_process = list(MODEL_PATHS.keys()) if model_option == "Bandingkan Semua Model" else [model_option]
            all_results = []
            
            with st.spinner('Memproses inferensi...'):
                for m_name in models_to_process:
                    model = load_alz_model(m_name)
                    if model:
                        proc_img = preprocess_image_keras3(image, m_name)
                        # Keras 3 predict return
                        predictions = model.predict(proc_img, verbose=0)[0]
                        idx = np.argmax(predictions)
                        all_results.append({
                            "Model": m_name,
                            "Prediksi Stadium": class_names[idx],
                            "Akurasi": predictions[idx]
                        })
            
            if model_option == "Bandingkan Semua Model":
                df = pd.DataFrame(all_results)
                st.dataframe(df.style.format({"Akurasi": "{:.2%}"}), hide_index=True)
                
                # Visualisasi dengan Plotly
                fig = px.bar(df, x='Model', y='Akurasi', color='Prediksi Stadium', 
                             text_auto='.2%', title="Konsistensi Prediksi Lintas Model")
                st.plotly_chart(fig, use_container_width=True)
            else:
                res = all_results[0]
                st.metric("Stadium Terdeteksi", res["Prediksi Stadium"])
                st.progress(float(res["Akurasi"]))
                st.write(f"**Tingkat Keyakinan:** `{res['Akurasi']:.2%}`")
                
                # Deskripsi Akademik
                st.info(f"**Catatan Klinis:** {STADIUM_DESC.get(res['Prediksi Stadium'], 'Informasi tidak tersedia.')}")

elif analysis_mode == "Analisis Batch (Banyak)":
    files = st.file_uploader("Unggah koleksi MRI", type=["jpg", "png"], accept_multiple_files=True)
    
    if files:
        if model_option == "Bandingkan Semua Model":
            st.warning("Silakan pilih satu model spesifik di sidebar untuk Analisis Batch.")
        else:
            model = load_alz_model(model_option)
            batch_list = []
            
            with st.spinner(f'Menganalisis {len(files)} citra...'):
                for f in files:
                    img = Image.open(f)
                    proc = preprocess_image_keras3(img, model_option)
                    pred = model.predict(proc, verbose=0)[0]
                    idx = np.argmax(pred)
                    batch_list.append({
                        "Nama File": f.name,
                        "Stadium": class_names[idx],
                        "Confidence": f"{pred[idx]:.2%}"
                    })
            
            st.subheader(f"Hasil Batch - {model_option}")
            st.dataframe(pd.DataFrame(batch_list), use_container_width=True)

# --- FOOTER ---
st.markdown("---")
f_col1, f_col2, f_col3 = st.columns(3)
with f_col1:
    st.caption("© 2025 Academic Research Tool")
with f_col2:
    st.caption("Data Source: MRI Dataset")
with f_col3:
    st.caption("Final Project / UAP Edition")