import streamlit as st
from PIL import Image
import base64
from datetime import datetime
import io
from models.model_loader import ModelLoader
from utils.image_processor import ImageProcessor
from utils.caption_generator import CaptionGenerator
from config import Config

class ImageCaptioningApp:
    def __init__(self):
        self.model_loader = ModelLoader()
        self.caption_model, self.vgg_model, self.tokenizer = self.model_loader.load_models()
        self.caption_generator = CaptionGenerator(self.caption_model, self.tokenizer)
        self.setup_page_config()
        self.initialize_session_state()

    def initialize_session_state(self):
        if 'current_page' not in st.session_state:
            st.session_state.current_page = "Beranda"
        if 'history' not in st.session_state:
            st.session_state.history = []
        if 'history_count' not in st.session_state:
            st.session_state.history_count = 0

    def setup_page_config(self):
        st.set_page_config(
            page_title="Image Captioning",
            page_icon="🖼️",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Styling untuk UI
        st.markdown("""
        <style>
            /* Style Global */
            .stApp {
                background-color: #f9fafb;
            }
            
            /* Section Hero */
            .hero-container {
                background: linear-gradient(135deg, #001f3f 0%, #007bff 100%);
                padding: 4rem 2rem;
                border-radius: 0 0 50px 50px;
                color: white;
                text-align: center;
                margin: -6rem -4rem 2rem -4rem;
                position: relative;
                overflow: hidden;
            }
            
            .wave-bottom {
                position: absolute;
                bottom: 0;
                left: 0;
                width: 100%;
                height: 50px;
            }
            
            .hero-title {
                font-size: 3rem;
                font-weight: bold;
                margin-bottom: 1.5rem;
                color: white; 
            }
            
            .hero-subtitle {
                font-size: 1.2rem;
                opacity: 0.9;
                max-width: 800px;
                margin: 0 auto;
            }
            
            /* Konten Utama */
            .main-section {
                background: white;
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                margin-top: 2rem;
            }
            
            /* Area Upload */
            .upload-container {
                border: 2px dashed #007bff;
                border-radius: 15px;
                padding: 2rem;
                text-align: center;
                margin: 2rem 0;
                transition: all 0.3s ease;
            }
            
            .upload-container:hover {
                border-color: #0056b3;
                background: rgba(0, 123, 255, 0.05);
            }
            
            /* Style Tombol */
            .stButton button {
                background: linear-gradient(135deg, #0056b3 0%, #007bff 100%);
                color: white;
                border: none;
                border-radius: 25px;
                padding: 0.75rem 2rem;
                font-weight: bold;
                width: 100%;
                transition: all 0.3s ease;
            }
            
            .stButton button:hover {
                opacity: 0.9;
                transform: translateY(-2px);
            }
            
            /* Hasil Caption */
            .result-container {
                background: #eef2f7;
                padding: 2rem;
                border-radius: 15px;
                margin-top: 2rem;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            }
            
            /* Riwayat */
            .history-card {
                background: white;
                padding: 1.5rem;
                border-radius: 15px;
                margin: 1rem 0;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                transition: all 0.3s ease;
            }
            
            .history-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
            }
            
            /* Sembunyikan Elemen Streamlit Default */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Responsif */
            @media (max-width: 768px) {
                .hero-container {
                    margin: -2rem -1rem 1rem -1rem;
                    padding: 2rem 1rem;
                }
                
                .hero-title {
                    font-size: 2rem;
                }
            }
        </style>
        """, unsafe_allow_html=True)

    def show_home(self):
        # Section Hero
        st.markdown("""
            <div class="hero-container">
                <h1 class="hero-title">Selamat datang di Aplikasi Image Caption</h1>
                <p class="hero-subtitle">
                    Image captioning adalah tugas lintas disiplin yang bertujuan untuk secara otomatis menghasilkan deskripsi tekstual untuk gambar yang diberikan dengan menggunakan teknik visi komputer dan pemrosesan bahasa alami" (Zhao, 2021). 
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Fitur Utama
        st.markdown("""
            <div class="main-section">
                <h2 style="text-align: center; color: #333;">Fitur Utama</h2>
                <div style="display: flex; justify-content: space-around; flex-wrap: wrap; margin-top: 2rem;">
                    <div style="flex: 1; min-width: 250px; margin: 1rem; padding: 1rem; text-align: center; background: #f9f9f9; border-radius: 10px; border: 1px solid #ddd;">
                        <h3 style="color: #0072ff;">📚 Mendukung Penelitian</h3>
                        <p>Dikembangkan untuk mendukung penelitian tugas akhir dalam bidang image captioning.</p>
                    </div>
                    <div style="flex: 1; min-width: 250px; margin: 1rem; padding: 1rem; text-align: center; background: #f9f9f9; border-radius: 10px; border: 1px solid #ddd;">
                        <h3 style="color: #0072ff;">📸 Eksperimen Model</h3>
                        <p>Memanfaatkan model CNN-LSTM untuk menghasilkan deskripsi gambar secara otomatis.</p>
                    </div>
                    <div style="flex: 1; min-width: 250px; margin: 1rem; padding: 1rem; text-align: center; background: #f9f9f9; border-radius: 10px; border: 1px solid #ddd;">
                        <h3 style="color: #0072ff;">📝 Dokumentasi Hasil</h3>
                        <p>Menyediakan fitur untuk menyimpan hasil caption sebagai bagian dari analisis data.</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Tombol Mulai
        if st.button("✨ Mulai Generate Caption", use_container_width=True):
            st.session_state.current_page = "Generate Caption"
            st.experimental_rerun()

    def generate_caption_ui(self):
        # Section Hero dengan tinggi lebih kecil
        st.markdown("""
            <div class="hero-container" style="padding: 2rem;">
                <h2 class="hero-title">Generate Caption</h2>
            </div>
        """, unsafe_allow_html=True)
        
        # Section Upload
        with st.container():
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                uploaded_file = st.file_uploader("Unggah gambar Anda", type=['jpg', 'jpeg', 'png'])
                
                if uploaded_file is not None:
                    try:
                        image = Image.open(uploaded_file)
                        st.image(image, use_column_width=True)
                        
                        if st.button("🔮 Generate Caption", key="generate_btn"):
                            with st.spinner("Memproses gambar..."):
                                processed_image = ImageProcessor.preprocess_image(image)
                                features = self.vgg_model.predict(processed_image)
                                caption = self.caption_generator.generate_caption(features)
                                
                                st.markdown(f"""
                                    <div class="result-container">
                                        <h3>Hasil Caption:</h3>
                                        <p>{caption}</p>
                                    </div>
                                """, unsafe_allow_html=True)
                                
                                self.save_to_history(image, caption)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

    def show_history_page(self):
        st.markdown("""
            <div class="hero-container" style="padding: 2rem;">
                <h2 class="hero-title">Riwayat Caption</h2>
            </div>
        """, unsafe_allow_html=True)
        
        if not st.session_state.history:
            st.markdown("""
                <div style="text-align: center; padding: 4rem;">
                    <h3>Belum ada riwayat caption</h3>
                    <p>Hasil caption yang Anda buat akan muncul di sini.</p>
                </div>
            """, unsafe_allow_html=True)
            return

        for item in st.session_state.history:
            with st.container():
                st.markdown(f"""
                    <div class="history-card">
                        <p style="color: #666;">📅 {item['timestamp']}</p>
                    </div>
                """, unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    try:
                        image_bytes = base64.b64decode(item['image'])
                        st.image(image_bytes, use_column_width=True)
                    except Exception as e:
                        st.error("Gagal memuat gambar")
                with col2:
                    st.markdown(f"""
                        <div style="padding: 1rem;">
                            <h4>Caption:</h4>
                            <p>{item['caption']}</p>
                        </div>
                    """, unsafe_allow_html=True)

    def show_about(self):
        st.markdown("""
            <div class="hero-container" style="padding: 2rem;">
                <h2 class="hero-title">Tentang Aplikasi</h2>
            </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["Penjelasan", "Teknologi", "Cara Kerja", "Metode Evaluasi"])
        
        with tab1:
            st.markdown(Config.ABOUT_TEXT)
        with tab2:
            st.markdown(Config.TECH_TEXT)
        with tab3:
            st.image('images/flowsistem.png', caption='Diagram Alur Proses', use_column_width=True)
            st.markdown(Config.PROCESS_TEXT)
        with tab4:
            st.markdown(Config.EVAL_TEXT)

    def save_to_history(self, image, caption):
        try:
            buffered = io.BytesIO()
            if image.mode in ('RGBA', 'LA'):
                background = Image.new('RGB', image.size, (255, 255, 255))
                background.paste(image, mask=image.split()[-1])
                image = background
            image.save(buffered, format="JPEG", quality=85, optimize=True)
            img_str = base64.b64encode(buffered.getvalue()).decode()
            history_item = {
                'id': st.session_state.history_count,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'image': img_str,
                'caption': caption
            }
            st.session_state.history.insert(0, history_item)
            st.session_state.history_count += 1
            if len(st.session_state.history) > 10:
                st.session_state.history = st.session_state.history[:10]
            return True
        except Exception as e:
            st.error(f"Gagal menyimpan ke riwayat: {str(e)}")
            return False

    def run(self):
        # Sidebar Navigation
        with st.sidebar:
            st.title("Menu Navigasi")
            selected_page = st.radio(
                "", 
                ["Beranda", "Generate Caption", "Riwayat Caption", "Tentang"],
                index=["Beranda", "Generate Caption", "Riwayat Caption", "Tentang"].index(st.session_state.current_page)
            )
            st.session_state.current_page = selected_page

        # Page Router
        if st.session_state.current_page == "Beranda":
            self.show_home()
        elif st.session_state.current_page == "Generate Caption":
            self.generate_caption_ui()
        elif st.session_state.current_page == "Riwayat Caption":
            self.show_history_page()
        elif st.session_state.current_page == "Tentang":
            self.show_about()

if __name__ == '__main__':
    app = ImageCaptioningApp()
    app.run()