# News Article Summarizer

AI-powered text summarization using Transformer models (BART).

## Features
- **Transformer Model**: Uses `facebook/bart-large-cnn` for state-of-the-art abstractive summarization.
- **Evaluation**: ROUGE metrics implementation.
- **API**: FastAPI backend for integration.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run Summarizer (CLI):
   ```bash
   python src/summarizer.py
   ```

3. Run Evaluation:
   ```bash
   python src/evaluate.py
   ```

4. Run API:
   ```bash
   uvicorn src.app:app --reload
   ```

## API Usage
POST `/summarize`
```json
{
    "text": "Your long article text here..."
}
```
