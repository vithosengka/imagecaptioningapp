import os

class Config:
    # App configuration
    APP_TITLE = "Image Captioning"
    
    # Model paths
    MODEL_PATH = os.path.join('saved_models', 'model17Des.h5')
    TOKENIZER_PATH = os.path.join('saved_models', 'tokenizer17des.pkl')
    
    # Model parameters
    MAX_LENGTH = 36
    IMG_SIZE = (224, 224)
    
    # Special tokens
    START_TOKEN = 'startseq'
    END_TOKEN = 'endseq'

    # Custom CSS
    CUSTOM_CSS = """
        <style>
        .main {
            padding: 2rem;
        }
        .stButton>button {
            width: 100%;
            background-color: #FF4B4B;
            color: white;
        }
        .stButton>button:hover {
            background-color: #FF6B6B;
        }
        .sidebar .sidebar-content {
            background-color: #f5f5f5;
        }
        h1, h2, h3 {
            color: #1E1E1E;
        }
        .caption-result {
            padding: 1rem;
            background-color: #f0f2f6;
            border-radius: 10px;
            margin: 1rem 0;
        }
        </style>
    """

    # Content
    ABOUT_TEXT = """
    ### Apa itu Image Caption?
    
    Image captioning adalah proses menghasilkan deskripsi tekstual yang alami dan informatif dari sebuah gambar. Teknologi ini menggabungkan bidang computer vision dan natural language processing (NLP) untuk menjembatani informasi visual dan tekstual 

    ###  Teknik dasar
    Dalam image captioning melibatkan pengenalan objek penting, atributnya, dan hubungan antar objek dalam gambar, serta menghasilkan kalimat yang sintaksis dan semantiknya benar

    ### Konsep Encoder-Decoder dalam Model Image Captioning Menggunakan CNN dan LSTM

    Model image captioning berbasis CNN-LSTM menggunakan pendekatan encoder-decoder untuk menghasilkan deskripsi teks dari gambar masukan. Pada model ini, CNN berfungsi sebagai encoder, sementara LSTM digunakan sebagai decoder. Encoder menggunakan arsitektur **VGG16**, yang terkenal dengan kemampuannya mengekstraksi fitur visual dari gambar dengan baik. Gambar masukan diproses melalui beberapa lapisan konvolusi dan pooling pada VGG16, menghasilkan vektor fitur berdimensi tinggi yang merepresentasikan informasi visual gambar secara keseluruhan. Vektor ini kemudian digunakan sebagai masukan awal untuk decoder. Decoder, yang menggunakan Long Short-Term Memory (LSTM), memanfaatkan vektor fitur tersebut untuk menghasilkan deskripsi teks secara bertahap, dimulai dari token awal `startseq` hingga token akhir `endseq`. Pada setiap langkah waktu, LSTM menghasilkan kata berdasarkan konteks visual dari encoder dan kata yang dihasilkan sebelumnya. Proses pelatihan model bertujuan untuk meminimalkan perbedaan antara deskripsi yang dihasilkan model dan deskripsi sebenarnya dengan menggunakan fungsi loss seperti cross-entropy. Kombinasi VGG16 dan LSTM ini memungkinkan model untuk memahami konteks visual gambar dan menerjemahkannya ke dalam deskripsi teks yang gramatikal dan bermakna. Arsitektur ini cocok untuk tugas image captioning karena VGG16 memberikan representasi visual yang kuat, sedangkan LSTM unggul dalam menangani data sekuensial.
    """

    TECH_TEXT = """
    ### Teknologi yang Digunakan
    1. **Convolutional Neural Networks (CNN) - VGG16**
        - VGG16 adalah model deep learning berbasis CNN yang digunakan untuk ekstraksi fitur visual dari gambar.
        - Model ini dilatih sebelumnya pada dataset ImageNet untuk mengenali pola visual seperti bentuk, tekstur, dan warna.
        - Dalam sistem ini, layer terakhir VGG16 dihapus agar menghasilkan vektor fitur 4096 dimensi yang mewakili karakteristik gambar.

    2. **Long Short-Term Memory (LSTM)**
        - LSTM adalah jenis Recurrent Neural Network (RNN) yang digunakan untuk memproses data sekuensial, seperti teks.
        - LSTM digunakan untuk menghasilkan caption secara bertahap, kata demi kata, berdasarkan fitur gambar dan konteks kata sebelumnya.
        - Dengan memanfaatkan mekanisme memori, LSTM dapat menangkap hubungan temporal antara kata-kata dalam kalimat.

    3. **Transfer Learning**
        - Model VGG16 menggunakan pendekatan transfer learning, di mana model yang telah dilatih sebelumnya digunakan sebagai dasar untuk ekstraksi fitur, sehingga mempercepat pengembangan dan meningkatkan akurasi.

    4. **Natural Language Processing (NLP)**
        - Teknik NLP digunakan untuk memproses teks caption:
            - Tokenisasi: Membagi teks menjadi token individu (kata-kata).
            - Vocabulary Building: Membatasi kata-kata yang digunakan berdasarkan dataset.
            - Embedding Layer: Mengubah token kata menjadi representasi vektor untuk dimasukkan ke dalam model.

    5. **TensorFlow/Keras**
        - Framework deep learning TensorFlow dan Keras digunakan untuk membangun, melatih, dan menguji model CNN (VGG16) dan LSTM.
        - Fitur seperti pre-trained VGG16 dan layer embedding mempermudah pengimplementasian sistem.

    6. **Python**
        - Bahasa pemrograman utama yang digunakan untuk membangun sistem.
        - Python menyediakan pustaka seperti:
            - NumPy untuk manipulasi array.
            - Pandas untuk pengelolaan data.

    7. **Dataset  Flickr8k**
        Dataset Gambar Flickr8k mencakup 8.092 gambar, di mana setiap gambar dilengkapi dengan hingga lima deskripsi teks yang mendetail. Dataset ini berfungsi sebagai sumber daya penting bagi para pembelajar di bidang machine learning dan kecerdasan buatan (AI), sekaligus menyediakan tolok ukur dasar (foundational benchmark) untuk proyek-proyek yang berfokus pada deskripsi gambar berbasis kalimat.
    
    """

    EVAL_TEXT = """
    ### Metode Evaluasi yang Digunakan

    1. **BLEU (Bilingual Evaluation Understudy) Score**
    - **Fungsi**: Mengukur kesamaan antara caption yang dihasilkan oleh model dengan caption referensi (ground truth).
    - **Cara Kerja**:
        - BLEU membandingkan n-gram (uni-gram, bi-gram, tri-gram, dll.) dari caption model dengan caption referensi.
        - Skor dihitung berdasarkan jumlah n-gram yang cocok, dengan mempertimbangkan penalti jika caption model terlalu pendek.
    - **Kelebihan**:
        - Cocok untuk evaluasi kesamaan kata atau frasa pendek.
    - **Kelemahan**:
        - Kurang efektif menangkap struktur sintaksis atau konteks yang lebih luas.

    2. **METEOR (Metric for Evaluation of Translation with Explicit ORdering) Score**
    - **Fungsi**: Menilai kesamaan semantik antara caption yang dihasilkan dan caption referensi.
    - **Cara Kerja**:
        - METEOR mempertimbangkan kesamaan kata berbasis sinonim dan fleksibilitas morfologi (seperti kata dasar).
        - Menggunakan precision, recall, dan penalti berbasis urutan kata untuk menghitung skor.
    - **Kelebihan**:
        - Lebih akurat dibanding BLEU dalam menangkap kesamaan semantik.
    - **Kelemahan**:
        - Relatif lebih lambat karena melibatkan proses pencocokan yang lebih kompleks.

    3. **ROUGE (Recall-Oriented Understudy for Gisting Evaluation) Score**
    - **Fungsi**: Mengukur tingkat kemiripan antara caption model dan referensi dengan fokus pada recall.
    - **Cara Kerja**:
        - ROUGE menghitung jumlah n-gram, kata, atau urutan kata yang cocok.
        - Beberapa varian ROUGE yang sering digunakan:
        - ROUGE-N: Berdasarkan n-gram.
        - ROUGE-L: Berdasarkan urutan kata terpanjang yang cocok (longest common subsequence).
    - **Kelebihan**:
        - Efektif untuk mengevaluasi kecocokan frasa panjang.
    - **Kelemahan**:
        - Tidak mempertimbangkan kesamaan semantik antar kata.

    4. **CIDEr (Consensus-based Image Description Evaluation) Score**
    - **Fungsi**: Mengukur kesamaan antara caption model dan caption referensi berdasarkan konsensus.
    - **Cara Kerja**:
        - CIDEr menghitung kemiripan n-gram, tetapi dengan penyesuaian berbasis frekuensi kata pada seluruh dataset (mengurangi bobot kata umum).
        - Skor akhir adalah rata-rata kesamaan n-gram antara caption model dan referensi.
    - **Kelebihan**:
        - Dirancang khusus untuk tugas image captioning.
        - Lebih mencerminkan relevansi deskripsi dalam konteks dataset tertentu.
    - **Kelemahan**:
        - Bergantung pada variasi caption referensi dalam dataset.

    
    
    """

    PROCESS_TEXT = """
    ### Cara Kerja Sistem
    
    1. **Preprocessing Gambar**
       - Gambar diubah ukurannya menjadi {}x{}
       - Nilai piksel dinormalisasi untuk memastikan skala input sesuai dengan model.
       
    2. **Ekstraksi Fitur**
       - Gambar melewati proses ekstraksi fitur menggunakan model VGG16:
         - Blok convolutional memproses gambar untuk mengekstrak fitur visual utama seperti pola, bentuk, dan warna.
         - Gambar melewati beberapa conv layers, diikuti dengan pooling untuk mengurangi dimensi.
         - Setelah layer convolutional terakhir, output diratakan menggunakan operasi flatten.
         - Vektor fitur akhir (dengan dimensi 4096) dihasilkan melalui layer Dense.
       - Fitur ini digunakan sebagai representasi visual gambar.

    3. **Caption Processing**
       - Proses teks deskripsi dilakukan sebelum pelatihan model:
           - Caption dimulai dengan token khusus start="starseq", dan diakhiri dengan token end="endseq".
           - Teks caption dibersihkan, di-tokenize, dan dikonversi ke urutan bilangan bulat.
           - Vocabulary dibuat berdasarkan dataset caption untuk memastikan kata-kata yang relevan dapat dikenali oleh model.
           - Caption diubah menjadi sekuens dengan panjang maksimal {} token.

    4. **Generasi Caption dengan LSTM**
        - Fitur gambar dan caption sequence digunakan sebagai input ke model LSTM:
            - Fitur gambar (4096-dimensi) dilewatkan melalui layer Dropout, Dense, dan Batch Normalization untuk stabilisasi.
            - Caption sequence diubah menjadi representasi embedding (vocabulary size x embedding size).
            - Proses LSTM berlangsung dalam beberapa tahap:
                - Layer LSTM pertama (dengan 128 unit) memproses input secara berurutan.
                - Output LSTM diteruskan ke layer LSTM kedua (dengan 256 unit).
            - Output akhir diteruskan ke layer Dense dengan fungsi aktivasi softmax untuk memprediksi probabilitas kata berikutnya.
        - Model menghasilkan kata demi kata hingga token endseq terdeteksi atau panjang maksimal tercapai.
    
    5. **Proses Generasi Caption**
        - Caption dihasilkan secara iteratif:
            - Proses dimulai dengan token startseq.
            - Model memprediksi kata berikutnya berdasarkan kata-kata yang telah dihasilkan dan fitur gambar.
            - Kata baru ditambahkan ke caption hingga token endseq ditemukan atau batas maksimal 36 kata tercapai.
        - Caption akhir dikembalikan sebagai output.
       
    """.format(IMG_SIZE[0], IMG_SIZE[1], MAX_LENGTH, START_TOKEN, END_TOKEN)