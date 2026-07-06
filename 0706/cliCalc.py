print("=== 계산기 ===")
print("1. 덧셈")
print("2. 뺄셈")
print("3. 곱셈")
print("4. 나눗셈")

choice = input("메뉴 선택(1~4): ")

a = float(input("첫 번째 숫자: "))
b = float(input("두 번째 숫자: "))

if choice == "1":
    print("결과:", a + b)
elif choice == "2":
    print("결과:", a - b)
elif choice == "3":
    print("결과:", a * b)
elif choice == "4":
    if b == 0:
        print("0으로 나눌 수 없습니다.")
    else:
        print("결과:", a / b)
else:
    print("잘못된 메뉴입니다.")