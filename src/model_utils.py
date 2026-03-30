from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os
from src.config import MODEL_NAME, MODEL_CACHE_DIR

_tokenizer = None
_model = None

def get_model_and_tokenizer():
    global _tokenizer, _model
    
    if _model is None:
        print(f"Loading model: {MODEL_NAME}...")
        try:
            _tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
            _model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise e
            
    return _tokenizer, _model
