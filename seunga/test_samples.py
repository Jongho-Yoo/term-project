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
    ("허리가 아프고 다리가 저려요", "정형외과"),
    ("열이 나고 온몸이 쑤시고 기운이 없어요", "내과"),
    ("귀에서 윙 소리가 나고 잘 안 들려요", "이비인후과"),
    ("얼굴에 여드름이 많이 났어요", "피부과"),
]

correct = 0

for text, answer in samples:
    result = classifier(text, labels, hypothesis_template="이 증상은 {} 진료가 필요하다.")
    top = result["labels"][0]
    if top == answer:
        correct += 1
    print(text, "->", top, "(정답:", answer, ")")

print("정확도:", correct, "/", len(samples))