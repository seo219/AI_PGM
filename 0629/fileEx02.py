# write_data.py
f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()

# readline_all.py
f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

with open("test.txt", "w") as f:
    content = "Hello, Python!"
    f.write(content)

print(content)  # "Hello, Python!" 출력

# 한글 파일 쓰기
with open("한글파일.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요, 파이썬!")

# 한글 파일 읽기
with open("한글파일.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
