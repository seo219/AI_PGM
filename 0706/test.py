# 파이썬 자료형 관련 초급 예제들

# 1. 정수형 (int)
age = 25
print(f"정수: {age}, 타입: {type(age)}")

# 2. 실수형 (float)
height = 175.5
print(f"실수: {height}, 타입: {type(height)}")

# 3. 문자열 (str)
name = "Kim"
print(f"문자열: {name}, 타입: {type(name)}")

# 4. 불린형 (bool)
is_student = True
print(f"불린: {is_student}, 타입: {type(is_student)}")

# 5. 리스트 (list)
fruits = ["apple", "banana", "cherry"]
print(f"리스트: {fruits}, 타입: {type(fruits)}")

# 6. 튜플 (tuple)
colors = ("red", "green", "blue")
print(f"튜플: {colors}, 타입: {type(colors)}")

# 7. 딕셔너리 (dict)
person = {"name": "John", "age": 30, "city": "Seoul"}
print(f"딕셔너리: {person}, 타입: {type(person)}")

# 8. 집합 (set)
numbers = {1, 2, 3, 4, 5}
print(f"집합: {numbers}, 타입: {type(numbers)}")

# 9. 형 변환 (Type Casting)
num_str = "10"
num_int = int(num_str)
print(f"문자열 '10'을 정수로 변환: {num_int}, 타입: {type(num_int)}")

str_from_int = str(100)
print(f"정수 100을 문자열로 변환: {str_from_int}, 타입: {type(str_from_int)}")
