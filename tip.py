
cost = input("얼마 나왔나요? : ")
person = input("몇명이죠? : ")
percent = input("팁은 얼마나 내실껀가요? (10 or 15 or 20) : ")

tip = round(int(cost) * (int(percent) / 100 + 1), 2)

result = tip / int(person)

print(f"총 금액은 {tip}이며 {person}명이서 각각 내셔야 금액은 {result}입니다")