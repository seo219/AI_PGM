for i in range(1, 5):
    print("*" * i)

# ==============================================================

# 정방향
for i in range(1, 5):
    for j in range(1, i + 1):
        print("*", end="")
    print()

# 좌우 반전
for i in range(1, 5):
    for j in range(4 - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# 좌우 대칭
for i in range(1, 5):
    for j in range(4 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# 마름모
for i in range(1, 5):
    for j in range(4 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(3, 0, -1):
    for j in range(4 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# ==============================================================

# 숫자 입력 받기

# 정방향
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

# 좌우 반전
for i in range(1, num + 1):
    for j in range(num - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# 좌우 대칭
for i in range(1, num + 1):
    for j in range(num - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# 마름모
for i in range(1, num + 1):
    for j in range(num - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(num - 1, 0, -1):
    for j in range(num - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

