from transformers import pipeline

MODEL_NAME = "MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7"
LABELS = ["내과", "정형외과", "피부과", "이비인후과"]
TEMPLATE = "이 증상은 {} 진료가 필요하다."

_classifier = pipeline("zero-shot-classification", model=MODEL_NAME)


def classify(text):
    result = _classifier(text, LABELS, hypothesis_template=TEMPLATE)
    return result["labels"][0], result["scores"][0]