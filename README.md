# 🖼️ Aplikasi Image Captioning menggunakan VGG16 dan LSTM

## 📌 Deskripsi Proyek
Proyek ini merupakan **aplikasi Image Captioning** yang mampu menghasilkan **deskripsi teks otomatis dari sebuah gambar** menggunakan pendekatan **Deep Learning**.  
Model yang digunakan menggabungkan **VGG16** sebagai ekstraktor fitur gambar dan **LSTM (Long Short-Term Memory)** untuk menghasilkan kalimat deskripsi secara berurutan.

Aplikasi ini dibangun dan dijalankan menggunakan **Streamlit**, sehingga pengguna dapat langsung mengunggah gambar dan melihat hasil caption secara interaktif.

---

## 🎯 Tujuan Proyek
- Mengekstraksi fitur visual gambar menggunakan **VGG16**
- Menghasilkan deskripsi gambar menggunakan **model LSTM**
- Menggabungkan teknik **Computer Vision dan Natural Language Processing**
- Mengembangkan aplikasi web interaktif berbasis **Streamlit**

---

## 🧠 Arsitektur Model
- **VGG16 (Pre-trained ImageNet)**  
  → Ekstraksi fitur gambar  
- **Embedding Layer**  
  → Representasi teks  
- **LSTM**  
  → Pembentukan urutan kata (caption)  
- **Dense + Softmax Layer**  
  → Prediksi kata berikutnya  

---

## 🗂️ Dataset
- **Flickr8k Dataset**
- Terdiri dari **8.000 gambar**
- Setiap gambar memiliki **5 caption buatan manusia**
- Dataset digunakan untuk proses pelatihan dan evaluasi model

---

## 🛠️ Teknologi yang Digunakan
- **Python**
- **TensorFlow / Keras**
- **VGG16**
- **LSTM**
- **NLTK**
- **NumPy & Pandas**
- **Streamlit**
- **Jupyter Notebook**

---


## 🚀 Cara Menjalankan Aplikasi

### Prasyarat
- Python 3.8 atau lebih baru
- pip sudah terpasang

---

### Langkah-langkah Menjalankan Aplikasi

```bash
# 1. Clone repository
git clone https://github.com/username/image-captioning-vgg16-lstm.git
cd image-captioning-vgg16-lstm

# 2. Install dependency
pip install -r requirements.txt

# 3. Jalankan aplikasi Streamlit
streamlit run app.py

# 4. Akses aplikasi melalui browser
# http://localhost:8501
