from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7",
)

text = "무릎이 아프고 계단 오르기가 힘들어요"
labels = ["내과", "정형외과", "피부과", "이비인후과"]

result = classifier(text, labels, hypothesis_template="이 증상은 {} 진료가 필요하다.")
print(result)