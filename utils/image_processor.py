import numpy as np
from PIL import Image
from tensorflow.keras.applications.vgg16 import preprocess_input
from config import Config

class ImageProcessor:
    @staticmethod
    def preprocess_image(image: Image.Image) -> np.ndarray:
        """Preprocess image for VGG16"""
        # Resize image
        image = image.resize(Config.IMG_SIZE)
        image = np.array(image)
        
        # Handle alpha channel
        if image.shape[-1] == 4:
            image = image[..., :3]
        
        # Preprocess
        image = image.astype('float32')
        image = np.expand_dims(image, axis=0)
        image = preprocess_input(image)
        
        return image