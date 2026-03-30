from rouge_score import rouge_scorer
import matplotlib.pyplot as plt
import os
from src.config import PROJECT_ROOT

def calculate_rouge(reference: str, hypothesis: str):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, hypothesis)
    return scores

def plot_scores(scores):
    metrics = ['rouge1', 'rouge2', 'rougeL']
    values = [scores[m].fmeasure for m in metrics]
    
    plt.figure(figsize=(8, 5))
    plt.bar(metrics, values, color=['skyblue', 'lightgreen', 'salmon'])
    plt.ylim(0, 1.0)
    plt.title('ROUGE Scores (F-Measure)')
    plt.ylabel('Score')
    
    plot_path = os.path.join(PROJECT_ROOT, "rouge_scores.png")
    plt.savefig(plot_path)
    print(f"Saved plot to {plot_path}")

if __name__ == "__main__":
    # Dummy Test
    ref = "The fast-food chain is redesigning 800 UK stores to improve efficiency."
    hyp = "McDonalds is redesigning 800 stores in the UK to make it faster for drivers."
    
    scores = calculate_rouge(ref, hyp)
    print("Scores:", scores)
    plot_scores(scores)
