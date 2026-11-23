from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7",
)

labels = ["내과", "정형외과", "피부과", "이비인후과"]

samples = [
    ("무릎이 아프고 계단 오르기가 힘들어요", "정형외과"),
    ("피부에 붉은 발진이 생기고 가려워요", "피부과"),
    ("목이 따갑고 콧물이 계속 나요", "이비인후과"),
    ("소화가 안 되고 속이 자주 쓰려요", "내과"),
]

for text, answer in samples:
    result = classifier(text, labels, hypothesis_template="이 증상은 {} 진료가 필요하다.")
    top = result["labels"][0]
    print(text, "->", top, "(정답:", answer, ")")