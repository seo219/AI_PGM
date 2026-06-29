# # sys1.py
# import sys

# args = sys.argv[1:]
# for i in args:
#     print(i)

# # cmd
# # cd C:\Users\user\Documents\intel\0629

# # python sysArgvEx01.py
# # 출력 :
# # 아무것도  안 나옴

# # python sysArgvEx01.py 123 456 789
# # 출력 :
# # 123
# # 456
# # 789


import sys

if len(sys.argv) != 3:
    print("사용법: python test.py 이름 나이")
    sys.exit()

name = sys.argv[1]
age = sys.argv[2]

print(f"이름: {name}")
print(f"나이: {age}")