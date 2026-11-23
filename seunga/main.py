from classifier import classify

text = input("증상을 입력하세요: ")
department, score = classify(text)

print("추천 진료과:", department, "(점수:", round(score, 2), ")")
print("※ 의학적 진단이 아니며 참고용입니다. 응급 증상이 있으면 119 또는 가까운 응급실로 가세요.")