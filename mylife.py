# 남은 생 주로 계산하기
# 1년은 대략 365일 52주 12개월

age = input("나이를 알려주세요!")

end_of_years = input("언제까지 살고 싶습니까?")

age_of_days = int(age) * 365
end_of_days = int(end_of_years) * 365

age_of_weeks = int(age) * 52
end_of_weeks = int(end_of_years) * 52


result_days = end_of_days - age_of_days
result_weeks = end_of_weeks - age_of_weeks
result_years = int(end_of_years) - int(age)

print(
    f"앞으로 살 날은 {result_years}년 \n {result_weeks}주 \n {result_days}일 남았습니다."
)
print(int("5") / int(2.7))