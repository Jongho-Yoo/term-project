from classifier import classify

LOW_CONFIDENCE = 0.4

text = input("증상을 입력하세요: ")
ranking = classify(text)

print("추천 진료과 (상위 2개)")
for department, score in ranking[:2]:
    print("-", department, "(점수:", round(score, 2), ")")

if ranking[0][1] < LOW_CONFIDENCE:
    print("※ 확신도가 낮아요. 증상을 더 자세히 적어 보세요.")

print("※ 의학적 진단이 아니며 참고용입니다. 응급 증상이 있으면 119 또는 가까운 응급실로 가세요.")