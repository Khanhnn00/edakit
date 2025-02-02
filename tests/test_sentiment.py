from pathlib import Path
import os
import sys

os.getcwd()

EDAKIT_PATH = os.path.join(Path(__file__).parent.parent, "src")
print(EDAKIT_PATH)
sys.path.append(EDAKIT_PATH)

from eda.sentiment_analysis import SentimentAnalyzer

def test_sentiment():
    # from ..eda.sentiment_analysis import SentimentAnalyzer
    sentiment_analyzer = SentimentAnalyzer()
    texts = [
        "This movie sucks",
        "This one is great",
        "The world is about to end",
    ]  # Example texts
    pred_results = sentiment_analyzer.get_list_sentiment(texts=texts)
    true_results = ["negative", "positive", "negative"]
    assert (
        pred_results == true_results
    ), f"expected {true_results}, but got {pred_results}"
    # print(pred_results, true_results)


if __name__ == "__main__":
    # EDAKIT_PATH = os.path.join(Path(__file__).parent.parent, "src")
    # print(EDAKIT_PATH)
    test_sentiment()
    import pdb

    pdb.set_trace()