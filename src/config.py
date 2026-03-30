import os

# Model Settings
MODEL_NAME = "facebook/bart-large-cnn" # Pretrained on CNN/Daily Mail
MAX_INPUT_LENGTH = 1024
MAX_OUTPUT_LENGTH = 150
MIN_OUTPUT_LENGTH = 50

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
MODEL_CACHE_DIR = os.path.join(PROJECT_ROOT, "models")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
