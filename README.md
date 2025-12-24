<h1 align="center">Alzheimer Brain MRI Classification</h1>
---
<p align="center">
  <img src="assets/images/Cover.webp" width="70%">
</p>

<p align="center">
  Sumber Image : <a href="https://www.shutterstock.com/image-photo/haze-brain-alzheimer-600nw-2651172251.jpg">Access Here</a>
</p>

---

<h1 align="center">📑 Table of Contents 📑</h1>

- [Deskripsi Proyek](#deskripsi-proyek)
- [Latar Belakang](#latar-belakang)
- [Tujuan Pengembangan](#tujuan-pengembangan)
- [Sumber Dataset](#sumber-dataset)
- [Preprocessing dan Pemodelan](#preprocessing-dan-pemodelan)
  - [Preprocessing Data](#preprocessing-data)
  - [Pemodelan](#pemodelan)
- [Hasil & Evaluasi](#hasil--evaluasi)
- [Dashboard](#dashboard)

---

<h1 id="deskripsi-proyek" align="center">🧠 Klasifikasi Penyakit Alzheimer 🧠</h1>

Proyek ini berfokus pada pengembangan sistem klasifikasi otomatis untuk mendeteksi tingkat keparahan penyakit Alzheimer berdasarkan citra medis MRI (Magnetic Resonance Imaging). Dengan memanfaatkan teknik pemrosesan citra dan kecerdasan buatan, proyek ini bertujuan untuk membantu proses skrining awal dalam membedakan berbagai stadium atrofi otak.

Model ini dilatih untuk mengklasifikasikan citra MRI ke dalam 4 kategori klinis:

- **Non Demented** → Kondisi otak normal tanpa indikasi demensia.
- **Very Mild Demented** → Indikasi awal gejala demensia yang sangat ringan.
- **Mild Demented** → Gejala demensia tingkat ringan dengan perubahan struktural otak yang mulai terlihat.
- **Moderate Demented** → Penurunan fungsi kognitif dan atrofi otak tingkat sedang.

Untuk mendapatkan hasil klasifikasi yang paling akurat, penelitian ini menguji tiga pendekatan arsitektur Deep Learning yang berbeda:

- **1. Custom CNN (Baseline Model)**
- **2. MobileNetV2 (Transfer Learning & Fine-Tuning)**
- **3. VGG16 (Advanced Transfer Learning)**

---

<h1 id="latar-belakang" align="center">🧠 Latar Belakang 🧠</h1>

Penyakit Alzheimer merupakan gangguan neurodegeneratif progresif yang menjadi penyebab paling umum dari demensia di seluruh dunia. Penyakit ini menyebabkan penyusutan sel otak secara bertahap (atrofi), yang berdampak pada penurunan daya ingat, kemampuan berpikir, hingga perubahan perilaku secara drastis.
Tantangan utama dalam penanganan Alzheimer adalah gejalanya yang seringkali dianggap sebagai proses penuaan normal pada tahap awal (Very Mild Demented). Padahal, intervensi medis akan jauh lebih efektif jika dilakukan sebelum kerusakan otak meluas ke stadium lanjut (Moderate Demented).
Penggunaan citra Magnetic Resonance Imaging (MRI) merupakan salah satu standar emas untuk melihat perubahan struktur otak. Namun, menganalisis ratusan scan MRI secara manual memerlukan ketelitian tinggi, waktu yang lama, dan keahlian spesialis radiologi yang terbatas jumlahnya.

Proyek ini hadir untuk menjawab tantangan tersebut dengan memanfaatkan teknologi Deep Learning. Dengan menggunakan model Custom CNN, MobileNetV2, dan VGG16, sistem ini dikembangkan untuk:

- Otomatisasi Skrining: Membantu tenaga medis dalam melakukan klasifikasi stadium Alzheimer secara cepat dan objektif.
- Deteksi Dini: Mengidentifikasi pola halus pada citra MRI yang mungkin terlewatkan dalam observasi visual manual, terutama pada fase Very Mild.
- Akurasi Diagnostik: Memberikan perbandingan performa antara arsitektur model konvensional dan Transfer Learning untuk mendapatkan hasil klasifikasi yang paling reliabel.

Melalui pendekatan ini, diharapkan proses pemantauan kesehatan saraf pasien dapat dilakukan secara lebih efisien, mendukung keputusan klinis yang lebih tepat, dan membantu perencanaan perawatan pasien dengan lebih baik.

---

<h1 id="tujuan-pengembangan" align="center">🎯 Tujuan Pengembangan 🎯</h1>

- **Mengembangkan sistem klasifikasi citra MRI otak untuk mendeteksi penyakit Alzheimer secara otomatis ke dalam 4 kategori: Non Demented, Very Mild Demented, Mild Demented, dan Moderate Demented.**
- **Mengevaluasi dan membandingkan performa tiga arsitektur Deep Learning, meliputi:**
  - **Custom CNN**: Menguji efektivitas model yang dibangun dari awal dengan lapisan konvolusi mandiri.
  - **MobileNetV2**: Menguji performa model pre-trained yang ringan dan efisien menggunakan teknik partial fine-tuning pada 20 layer terakhir.
  - **VGG16**: Menguji kekuatan arsitektur yang lebih dalam dengan melakukan fine-tuning spesifik pada Block 4 dan Block 5 untuk menangkap detail tekstur otak yang kompleks.
- **Mengoptimalkan akurasi model melalui teknik Transfer Learning dan Fine-Tuning, guna mengatasi keterbatasan data medis dan meningkatkan kemampuan generalisasi model terhadap data baru.**
- **Menerapkan strategi pelatihan yang cerdas dengan menggunakan Callbacks seperti Early Stopping dan Learning Rate Reduction untuk mencegah overfitting dan memastikan konvergensi model yang stabil.**
- **Menyediakan alat skrining awal (Decision Support System) yang dapat membantu tenaga medis dalam mendeteksi indikasi Alzheimer secara objektif, cepat, dan konsisten berdasarkan data citra digital.**
- **Menentukan model terbaik (Best Model) berdasarkan metrik evaluasi seperti Akurasi, Loss, dan Confusion Matrix untuk digunakan sebagai standar dalam deteksi dini penyakit neurodegeneratif.**

---

<h1 id="sumber-dataset" align="center">📊 Sumber Dataset 📊</h1>

Dataset yang digunakan dalam proyek ini adalah **Augmented Alzheimer MRI Dataset**, yang diperoleh dari platform Kaggle. Dataset ini terdiri dari citra medis MRI otak yang telah dikumpulkan dan diproses untuk membantu tugas klasifikasi penyakit neurodegeneratif.

Dataset ini mencakup 4 kelas tingkat keparahan Alzheimer:
- **Non Demented**: Citra otak normal tanpa tanda-tanda atrofi yang signifikan.
- **Very Mild Demented**: Tahap awal di mana gejala mulai muncul secara samar.
- **Mild Demented**: Tahap ringan dengan pola penyusutan jaringan otak yang mulai terlihat jelas.
- **Moderate Demented**: Tahap menengah dengan indikasi atrofi yang kuat pada area hipokampus dan korteks.

Detail Pemrosesan Dataset:
- **Keseimbangan Data: Dataset telah melalui proses augmentation (penambahan data buatan) untuk memastikan setiap kelas memiliki jumlah sampel yang seimbang (1.250 citra per kelas dalam folder training), guna menghindari bias pada model.**
- **Pre-processing: Citra diproses ke dalam format $224 \times 224$ piksel dan dilakukan normalisasi nilai pixel sesuai standar masing-masing arsitektur (VGG16 & MobileNetV2).**
- **Pembagian Data: Dataset dibagi secara sistematis ke dalam tiga bagian: Train, Validation, dan Test.**

Link Original Dataset: [Augmented Alzheimer MRI Dataset (Kaggle)](https://www.kaggle.com/datasets/uraninjo/augmented-alzheimer-mri-dataset)

---

<h1 id="preprocessing-dan-pemodelan" align="center">🧼 Preprocessing dan Pemodelan 🧼</h1>

<h2 id="preprocessing-data" align="center">✨ Preprocessing Data ✨</h2>

Tahap preprocessing dimulai dengan memuat dataset wajah anak dari direktori yang telah diatur. Seluruh citra kemudian diproses menggunakan **MTCNN (Multi-Task Cascaded Convolutional Network)** untuk mendeteksi dan memotong area wajah sehingga model hanya mempelajari fitur visual yang relevan dan tidak terdistraksi oleh latar belakang. Setelah wajah berhasil diekstraksi, citra di-*resize* menjadi **224×224 piksel** dan dinormalisasi menggunakan **mean–std normalization** mengikuti standar input model pre-trained seperti EfficientNet dan Vision Transformer.

Untuk meningkatkan keragaman data dan mencegah overfitting, beberapa teknik **data augmentation** diterapkan, yaitu: rotasi acak, horizontal flip, random cropping, serta penyesuaian brightness–contrast. Dataset dibagi menggunakan **stratified split**, yaitu 80% data latih dan 20% data uji, untuk memastikan distribusi kelas **VP-0** dan **VP-1** tetap seimbang.  
Tahap preprocessing ini memastikan bahwa dataset yang digunakan bersih, konsisten, dan siap dipakai untuk seluruh eksperimen model.

---

<h2 id="pemodelan" align="center">🤖 Pemodelan 🤖</h2>

Penelitian ini menggunakan dua pendekatan utama: **(1) Handcrafted Features + Classic ML**, **(2) Deep Learning Modern (CNN, EfficientNet, dan ViT)**.  
Seluruh model dibandingkan untuk menentukan pendekatan paling ideal dalam mendeteksi Visual Proxy pada wajah anak.

---

### 🟦 **A. EfficientNet-B0 (Model Utama)**

EfficientNet-B0 dipilih karena merupakan CNN modern dengan efisiensi tinggi. Teknik **compound scaling** digunakan untuk menyeimbangkan *depth*, *width*, dan *resolution*, sehingga menghasilkan representasi fitur yang kuat pada citra wajah.

Tiga eksperimen dilakukan:

#### **1. Baseline EfficientNet**
- Classification head diubah menjadi Linear (1280 → 2)
- Training selama 10 epoch
- Optimizer Adam, LR = 1e-4  

#### **2. Fine-Tuning Standar**
- 40 layer teratas EfficientNet dibuka untuk dilatih ulang
- Meningkatkan kemampuan model dalam mengenali pola visual halus  

#### **3. Fine-Tuning + LoRA (Low-Rank Adaptation)**  
Pendekatan paling efisien sekaligus paling akurat:
- LoRA ditambahkan pada pointwise convolution
- Hanya parameter ber-rank rendah yang diperbarui
- Komputasi lebih ringan dibanding full fine-tuning  

---

### 🟪 **B. Vision Transformer (ViT-Base Patch16/224)**

Sebagai pembanding, digunakan Vision Transformer model dasar:

- Pre-trained ImageNet
- Classification head diganti menjadi Linear (768 → 2)
- Dilatih sebagai baseline (tanpa LoRA)

---

### 🟩 **C. Model Handcrafted Features + Machine Learning**

Selain deep learning, penelitian juga mengevaluasi kombinasi fitur manual:

- **Landmark**
- **GLCM**
- **CCM**
- **SIFT**
- **LBP**
- **HOG**
- **Gabor**
- **Color Moments**
- **Edge**

Setiap fitur atau kombinasi fitur diuji menggunakan:

- **SVM**
- **Random Forest**
- **K-NN**

---

<h1 id="hasil--evaluasi" align="center">📊 Hasil & Evaluasi 📊</h1>

**Evaluasi Model**

Model dievaluasi menggunakan beberapa metrik, termasuk **classification report** dan **confusion matrix**.

**Classification Report**

Berikut adalah penjelasan tentang metrik yang digunakan dalam classification report:

- **Precision**: Mengukur proporsi prediksi positif yang benar.
- **Recall**: Mengukur proporsi sampel aktual positif yang berhasil diidentifikasi dengan benar.
- **F1-Score**: Rata-rata harmonis dari precision dan recall.
- **Accuracy**: Mengukur keseluruhan performa model.

**Tabel Perbandingan Classification Report**

Berikut adalah perbandingan metrik evaluasi untuk setiap model:

| Model Fitur                        | Algoritma       | Akurasi | Precision | Recall | F1-Score |
|-----------------------------------|------------------|---------|-----------|--------|----------|
| Baseline                          | SVM              | 0.91    | 0.93      | 0.90   | 0.91     |
| Baseline                          | Random Forest    | 0.90    | 0.92      | 0.89   | 0.90     |
| Baseline                          | K-NN             | 0.88    | 0.97      | 0.80   | 0.87     |
| Landmark                          | SVM              | 0.86    | 0.90      | 0.83   | 0.86     |
| Landmark                          | Random Forest    | 0.85    | 0.87      | 0.85   | 0.86     |
| Landmark                          | K-NN             | 0.85    | 0.88      | 0.83   | 0.85     |
| Landmark + GLCM                   | SVM              | 0.86    | 0.91      | 0.82   | 0.86     |
| Landmark + GLCM                   | Random Forest    | 0.87    | 0.91      | 0.84   | 0.87     |
| Landmark + GLCM                   | K-NN             | 0.87    | 0.91      | 0.84   | 0.87     |
| Landmark + GLCM + CCM             | SVM              | 0.87    | 0.90      | 0.85   | 0.87     |
| Landmark + GLCM + CCM             | Random Forest    | 0.86    | 0.89      | 0.84   | 0.86     |
| Landmark + GLCM + CCM             | K-NN             | 0.84    | 0.87      | 0.82   | 0.84     |
| Landmark + GLCM + CCM + SIFT      | SVM              | 0.85    | 0.89      | 0.82   | 0.85     |
| Landmark + GLCM + CCM + SIFT      | Random Forest    | 0.87    | 0.92      | 0.82   | 0.87     |
| Landmark + GLCM + CCM + SIFT      | K-NN             | 0.81    | 0.82      | 0.82   | 0.82     |
| LBP                               | SVM              | 0.80    | 0.82      | 0.79   | 0.80     |
| LBP                               | Random Forest    | 0.76    | 0.76      | 0.79   | 0.77     |
| LBP                               | K-NN             | 0.76    | 0.75      | 0.79   | 0.77     |
| LBP + HOG                         | SVM              | 0.83    | 0.85      | 0.82   | 0.84     |
| LBP + HOG                         | Random Forest    | 0.80    | 0.79      | 0.85   | 0.82     |
| LBP + HOG                         | K-NN             | 0.73    | 0.86      | 0.58   | 0.69     |
| LBP + HOG + GABOR                 | SVM              | 0.83    | 0.85      | 0.82   | 0.84     |
| LBP + HOG + GABOR                 | Random Forest    | 0.82    | 0.81      | 0.87   | 0.84     |
| LBP + HOG + GABOR                 | K-NN             | 0.73    | 0.86      | 0.58   | 0.69     |
| LBP + HOG + GABOR + COLOR         | SVM              | 0.85    | 0.86      | 0.84   | 0.85     |
| LBP + HOG + GABOR + COLOR         | Random Forest    | 0.86    | 0.85      | 0.89   | 0.87     |
| LBP + HOG + GABOR + COLOR         | K-NN             | 0.73    | 0.86      | 0.58   | 0.69     |
| LBP + HOG + GABOR + COLOR + EDGE  | SVM              | 0.85    | 0.86      | 0.84   | 0.85     |
| LBP + HOG + GABOR + COLOR + EDGE  | Random Forest    | 0.85    | 0.85      | 0.87   | 0.86     |
| LBP + HOG + GABOR + COLOR + EDGE  | K-NN             | 0.73    | 0.86      | 0.58   | 0.69     |
| Baseline CNN                      | CNN              | 0.86    | 0.83      | 0.93   | 0.88     |
| CNN + FT Standar                  | CNN              | 0.90    | 0.91      | 0.90   | 0.91     |
| CNN + FT LoRA (Manual)            | CNN              | 0.89    | 0.91      | 0.89   | 0.90     |
| CNN + FT LoRA (Library)           | CNN              | 0.89    | 0.91      | 0.87   | 0.89     |
| Baseline EfficientNet             | EfficientNet     | 0.88    | 0.84      | 0.94   | 0.89     |
| EfficientNet + FT Standar         | EfficientNet     | 0.97    | 0.99      | 0.95   | 0.97     |
| EfficientNet + FT LoRA (Best)     | EfficientNet     | 0.98    | 0.99      | 0.97   | 0.98     |
| Vision Transformer Baseline       | ViT              | 0.95    | 0.95      | 0.95   | 0.95     |

Berikut adalah perbandingan metrik evaluasi terbaik:
| Model Terbaik                              | Algoritma      | Akurasi | Precision | Recall | F1-Score |
|---------------------------------------------|----------------|---------|-----------|--------|----------|
| Baseline                                    | SVM            | 0.91    | 0.93      | 0.90   | 0.91     |
| Landmark + GLCM                             | SVM            | 0.86    | 0.91      | 0.82   | 0.86     |
| Landmark + GLCM + CCM + SIFT                | Random Forest  | 0.87    | 0.92      | 0.82   | 0.87     |
| LBP + HOG + GABOR + COLOR                   | Random Forest  | 0.86    | 0.85      | 0.89   | 0.87     |
| CNN + Fine-Tuning Standar                   | CNN            | 0.90    | 0.91      | 0.90   | 0.91     |
| EfficientNet + Fine-Tuning + LoRA (BEST)    | EfficientNet   | 0.98    | 0.99      | 0.97   | 0.98     |
| Vision Transformer Baseline                 | ViT            | 0.95    | 0.95      | 0.95   | 0.95     |

<h2><b>Confusion Matrix 🔴🟢</b></h2>
<p>Di bawah ini adalah confusion matrix untuk model terbaik.</p>

<table align="center">
  <tr>
    <td align="center">
      <b>SVM Baseline</b><br>
      <img src="assets/images/Confusion_Matrix_Baseline.PNG" width="180px">
    </td>
    <td align="center">
      <b>SVM Landmark + GLCM</b><br>
      <img src="assets/images/Confusion_Matrix_SVM_LG.PNG" width="180px">
    </td>
    <td align="center">
      <b>RF — LMRK + GLCM + CCM + SIFT</b><br>
      <img src="assets/images/Confusion_Matrix_RF_fusion1.PNG" width="180px">
    </td>
  </tr>

  <tr>
    <td align="center">
      <b>RF — LBP + HOG + Gabor + Color</b><br>
      <img src="assets/images/Confusion_Matrix_RF_fusion2.PNG" width="180px">
    </td>
    <td align="center">
      <b>CNN FT Standar</b><br>
      <img src="assets/images/Confusion_Matrix_CNN_FT_Standar.PNG" width="180px">
    </td>
    <td align="center">
      <b>EfficientNet + LoRA</b><br>
      <img src="assets/images/Confusion_Matrix_FT_LoRA.PNG" width="180px">
    </td>
  </tr>

  <tr>
    <td align="center">
      <b>Vision Transformer</b><br>
      <img src="assets/images/Confusion_Matrix_ViT.PNG" width="180px">
    </td>
  </tr>
</table>

<h2><b>Learning Curves 📈</b></h2>
<p>Berikut adalah learning curves untuk model CNN, EfficientNet dan ViT.</p>

<table align="center">
  <tr>
    <td align="center">
      <b>CNN Learning Curve</b><br>
      <img src="assets/images/grafik_cnn.PNG" width="350px">
    </td>
    <td align="center">
      <b>EfficientNet Learning Curve</b><br>
      <img src="assets/images/grafik_efficient.PNG" width="350px">
    </td>
  </tr>

  <tr>
    <td align="center" colspan="2">
      <b>Vision Transformer Learning Curve</b><br>
      <img src="assets/images/grafik_vit.PNG" width="350px">
    </td>
  </tr>
</table>

<h1 id="dashboard" align="center">🔬 GrowthVision AI: Child Growth Classification 🔬</h1>

<p align="center">
  <a href="https://child-growth-classification.streamlit.app/" target="_blank">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Streamlit App">
  </a>
</p>

<p align="center">
  <strong>Live Demo:</strong> 
  <a href="https://child-growth-classification.streamlit.app/">child-growth-classification.streamlit.app</a>
</p>

**GrowthVision AI** adalah sistem berbasis web yang dirancang untuk melakukan klasifikasi morfologi wajah pada anak guna mendukung analisis pertumbuhan pediatrik. Proyek ini memanfaatkan teknologi *Deep Learning* dengan arsitektur **CNN** dan **EfficientNet-B0** yang dioptimalkan menggunakan teknik **LoRA (Low-Rank Adaptation)**.

---

## 🚀 Fitur Utama
- **Batch Processing**: Mampu melakukan analisis hingga 20 subjek secara acak sekaligus.
- **Inference Models**: Pilihan arsitektur model antara EfficientNet + LoRA, CNN Fine-Tuning, atau SVM Klasik.
- **Visualisasi Real-time**: Hasil prediksi dilengkapi dengan *Confidence Score* menggunakan Gauge Chart interaktif.
- **Export Data**: Pengguna dapat mengunduh hasil analisis dalam format CSV untuk keperluan statistik lebih lanjut.

---

## 🛠️ Cara Menggunakan Dashboard

### 1. Memilih Sumber Data
Terdapat dua metode input pada panel kiri (Sidebar):
* **Sampel Acak GitHub**: Sistem akan mengambil 20 gambar secara acak dari dataset penelitian yang tersimpan di folder `samples`.
* **Upload Manual**: Pengguna dapat mengunggah foto subjek sendiri (format .jpg, .png, atau .jpeg).

### 2. Menjalankan Analisis
* Pilih arsitektur model yang diinginkan pada menu drop-down.
* Klik tombol **🚀 RUN INFERENCE**.
* Tunggu hingga progress bar mencapai 100%.

### 3. Membaca Hasil
* **Classification Summary**: Ringkasan total jumlah subjek yang terdeteksi sebagai **VP-0 (Proportional)** dan **VP-1 (Linear)**.
* **Individual Analysis**: Detail hasil per gambar lengkap dengan persentase keyakinan model.
* **Download Report**: Klik tombol unduh di bagian bawah untuk menyimpan tabel hasil.

---

## 📂 Struktur Repositori
- `app.py`: File utama aplikasi Streamlit.
- `samples/`: Folder berisi dataset gambar sampel untuk demo.
- `requirements.txt`: Daftar library Python yang dibutuhkan (PyTorch, Streamlit, Plotly, dll).
- `README.md`: Dokumentasi proyek.

---

## 🔬 Metodologi & Riset
Sistem ini dikembangkan sebagai bagian dari tugas besar mata kuliah **Machine Learning**. Fokus riset ini adalah mengimplementasikan teknik *transfer learning* dan efisiensi model melalui **LoRA** untuk mengenali fitur morfologi wajah yang berkaitan dengan pola pertumbuhan (Visual Proxy) pada anak-anak.

---

## ⚖️ Lisensi
Proyek ini didistribusikan di bawah **MIT License**. Data yang digunakan dalam demo ini bertujuan untuk kepentingan edukasi dan riset teknologi *screening* awal non-medis.

---
**© 2024 | Machine Learning**
