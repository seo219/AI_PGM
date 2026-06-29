# 1. 1~100까지의 수의 합을 출력하는 프로그램
sum = 0
for i in range(1, 101):
    sum += i
print(f"1~100까지의 수의 합: {sum}")

# 2. 1~100까지의 수 중 홀수의 합을 출력하는 프로그램
sum = 0
for i in range(1, 101):
    if i % 2 != 0:
        sum += i
print(f"1~100까지 중 홀수의 합: {sum}")

# 3. 1~100까지의 수 중 6의 배수들의 합을 출력하는 프로그램
sum = 0
for i in range(1, 101):
    if i % 6 == 0:
        sum += i
print(f"1~100까지 중 6의 배수의 합: {sum}")

sum = 0
for i in range(6, 101, 6):
    sum += i

print(f"1~100까지 중 6의 배수의 합: {sum}")

