import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from config import Config

class CaptionGenerator:
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer
        
    def generate_caption(self, image_features):
        """Generate caption from image features"""
        # Initialize with start token
        start_token_idx = self.tokenizer.word_index[Config.START_TOKEN]
        end_token_idx = self.tokenizer.word_index[Config.END_TOKEN]
        input_sequence = [start_token_idx]
        
        # Generate caption word by word
        for i in range(Config.MAX_LENGTH):
            sequence = pad_sequences([input_sequence], maxlen=Config.MAX_LENGTH)
            pred = self.model.predict([image_features, sequence], verbose=0)
            pred_idx = np.argmax(pred[0])
            
            if pred_idx == end_token_idx:
                break
                
            input_sequence.append(pred_idx)
        
        # Convert indices to words
        words = []
        for idx in input_sequence[1:]:
            if idx == end_token_idx:
                break
            word = next((word for word, index in self.tokenizer.word_index.items() 
                        if index == idx), None)
            if word is not None:
                words.append(word)
        
        return ' '.join(words)