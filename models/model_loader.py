import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.models import load_model
import pickle
from config import Config
import os

class ModelLoader:
    def __init__(self):
        self.caption_model = None
        self.vgg_model = None
        self.tokenizer = None
        
    def load_models(self):
        # Load VGG16
        base_model = VGG16()
        self.vgg_model = tf.keras.Model(inputs=base_model.inputs, 
                                      outputs=base_model.layers[-2].output)
        
        # Load caption model
        self.caption_model = load_model(Config.MODEL_PATH)
        
        # Load tokenizer
        with open(Config.TOKENIZER_PATH, 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        
        return self.caption_model, self.vgg_model, self.tokenizer