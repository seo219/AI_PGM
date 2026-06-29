# for
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    if i < 10:
        print(i, end=" ")
    else:
        print(i)

for i in ["고", "저", "장", "단", "쉼"]:
    print(i, end=" ")

# marks1.py
marks = [90, 25, 67, 45, 80]   # 학생들의 시험 점수 리스트

number = 0   # 학생에게 붙여 줄 번호
for mark in marks:   # 90, 25, 67, 45, 80을 순서대로 mark에 대입
    number = number + 1 
    if mark >= 60: 
        print(f"{number}번 학생은 합격입니다.")
    else: 
        print(f"{number}번 학생은 불합격입니다.")

# marks2.py
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number + 1 
    if mark < 60:
        continue 
    print(f"{number}번 학생 축하합니다. 합격입니다.")
