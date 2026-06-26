#1. 두 개의 정수를 입력 받아 사칙 연산의 결과를 출력하세요.
a = int(input("첫 번째 정수를 입력하세요.: "))
b = int(input("두 번째 정수를 입력하세요.: "))

print("\n사칙연산 결과\n")

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}\n")

#2. 5개의 정수를  입력 받아 리스트를 정의하고 그 리스트의 총 합, 평균, 최소 값, 최대 값을 출력하세요.
a = int(input("첫 번째 정수를 입력하세요.: "))
b = int(input("두 번째 정수를 입력하세요.: "))
c = int(input("세 번째 정수를 입력하세요.: "))
d = int(input("네 번째 정수를 입력하세요.: "))
e = int(input("다섯 번째 정수를 입력하세요.: "))

nums = [a, b, c, d, e]

print(f"\n리스트: {nums}\n")

print(f"총 합: {sum(nums)}")
print(f"평균: {sum(nums) / len(nums)}")
print(f"최소 값: {min(nums)}")
print(f"최대 값: {max(nums)}\n")

#3. 과일명이 있는 리스트를 정의하고 그 리스트의 첫 번째와 마지막 문자열을 출력하세요.
fruits = ["apple", "banana", "cherry", "orange", "pear"]

print(f"과일 리스트: {fruits}\n")

print(f"첫 번째 과일: {fruits[0]}")
print(f"마지막 과일: {fruits[-1]}\n")

#4 과일명을 5개 입력 받아 리스트로 정의하고 그 리스트의 첫 번째와 마지막 문자열을 출력하세요.
fruit1 = input("첫 번째 과일을 입력하세요.: ")
fruit2 = input("두 번째 과일을 입력하세요.: ")
fruit3 = input("세 번째 과일을 입력하세요.: ")
fruit4 = input("네 번째 과일을 입력하세요.: ")
fruit5 = input("다섯 번째 과일을 입력하세요.: ")

fruits = [fruit1, fruit2, fruit3, fruit4, fruit5]

print(f"\n과일 리스트: {fruits}\n")

print(f"첫 번째 과일: {fruits[0]}")
print(f"마지막 과일: {fruits[-1]}\n")