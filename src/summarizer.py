from src.model_utils import get_model_and_tokenizer
from src.config import MAX_INPUT_LENGTH, MAX_OUTPUT_LENGTH, MIN_OUTPUT_LENGTH

def summarize_text(text: str) -> str:
    if not text or not text.strip():
        return ""

    tokenizer, model = get_model_and_tokenizer()
    
    try:
        # Tokenize and run generation
        inputs = tokenizer(
            text, 
            max_length=MAX_INPUT_LENGTH, 
            truncation=True, 
            return_tensors="pt"
        )
        
        summary_ids = model.generate(
            inputs["input_ids"], 
            max_length=MAX_OUTPUT_LENGTH, 
            min_length=MIN_OUTPUT_LENGTH, 
            length_penalty=2.0, 
            num_beams=4, 
            early_stopping=True
        )
        
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    except Exception as e:
        print(f"Summarization error: {e}")
        return "Error generating summary."

if __name__ == "__main__":
    # Test
    sample_text = """
    The fast-food chain, which has more than 1,200 locations in the UK, said it was introducing the changes to "evolve" its customer experience. 
    It will be rolling out the new design to 800 restaurants over the next four years. 
    The revamp will include a new counter layout, which will see specific areas for different orders, with a dedicated collection area for delivery drivers.
    The company said this would reduce congestion and make the process faster and more efficient for customers and couriers.
    """
    print("Summary:", summarize_text(sample_text))
