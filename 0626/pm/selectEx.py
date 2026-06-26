# 제어문

# 실행 순서를 제어한다.
# 순서는 먼저 기술된 순서대로 실행된다. 즉, 위에서 아래로 순차적으로 실행된다.

# 선택문 : if, match~case
# 반복문 : for, while (do~while은 없음)
# 무시문 : break, continue
# 복귀문 : return

# 다른 언어들
# if (조건식){
# 문장
# 문장
#}
# if (조건식):
#   문장
#   문장

money = int(input("현재 보유 금액 입력 : "))

if money >= 20000:
    print("택시를 타고 가라.")
else:
    print("걸어가라")

print("Good night!!!")