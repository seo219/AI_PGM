# Python Container 정리

## 1. Container란?

**Container(컨테이너)**는 여러 개의 데이터를 하나의 객체에 저장하는 자료형입니다.

파이썬에서 가장 많이 사용하는 컨테이너는 다음 네 가지입니다.

| 자료형 | 특징 | 순서 | 중복 | 수정 가능 |
|--------|------|------|------|----------|
| List | 순서가 있는 데이터 | O | O | O |
| Tuple | 변경 불가능한 데이터 | O | O | X |
| Set | 중복 없는 데이터 | X | X | O |
| Dictionary | Key-Value 저장 | O(3.7+) | Key X | O |

---

# 2. List (리스트)

여러 개의 데이터를 **순서대로 저장**하는 가장 기본적인 컨테이너입니다.

```python
nums = [10, 20, 30]
```

## 특징

- 순서가 있다.
- 중복을 허용한다.
- 수정 가능(Mutable)

```python
nums.append(40)
nums[0] = 100
```

결과

```python
[100, 20, 30, 40]
```

### 자주 사용하는 메서드

| 메서드 | 설명 |
|---------|------|
| append() | 맨 뒤 추가 |
| extend() | 여러 개 추가 |
| insert() | 원하는 위치 삽입 |
| remove() | 값 삭제 |
| pop() | 삭제 후 반환 |
| sort() | 정렬 |
| reverse() | 뒤집기 |
| copy() | 복사 |

---

# 3. Tuple (튜플)

튜플은 **수정할 수 없는 리스트**입니다.

```python
point = (3, 5)
```

## 특징

- 순서가 있다.
- 중복 허용
- 수정 불가능(Immutable)

```python
point[0]
```

가능하지만

```python
point[0] = 10
```

오류 발생

```
TypeError
```

### 자주 사용하는 메서드

| 메서드 | 설명 |
|---------|------|
| count() | 개수 |
| index() | 위치 |

### 언패킹

```python
point = (3, 5)

x, y = point

print(x)
print(y)
```

---

# 4. Set (집합)

중복을 허용하지 않는 컨테이너입니다.

```python
numbers = {1, 2, 3}
```

## 특징

- 순서 없음
- 중복 없음
- 수정 가능

```python
numbers.add(4)
numbers.remove(2)
```

### 중복 제거

```python
nums = [1, 2, 2, 3, 3, 4]

result = set(nums)

print(result)
```

출력

```
{1, 2, 3, 4}
```

### 집합 연산

합집합

```python
A = {1,2,3}
B = {3,4,5}

print(A | B)
```

교집합

```python
print(A & B)
```

차집합

```python
print(A - B)
```

### 자주 사용하는 메서드

| 메서드 | 설명 |
|---------|------|
| add() | 추가 |
| remove() | 삭제 |
| discard() | 삭제(없어도 오류 X) |
| pop() | 임의의 값 제거 |
| clear() | 전체 삭제 |

---

# 5. Dictionary (딕셔너리)

Key와 Value를 저장하는 자료형입니다.

```python
student = {
    "name": "Alice",
    "age": 20
}
```

## 특징

- Key를 이용하여 검색
- Key는 중복 불가
- Value는 중복 가능
- 수정 가능

### 조회

```python
student["name"]
```

또는

```python
student.get("name")
```

### 추가

```python
student["major"] = "Computer"
```

### 수정

```python
student["age"] = 21
```

### 삭제

```python
del student["age"]
```

### 자주 사용하는 메서드

| 메서드 | 설명 |
|---------|------|
| get() | 조회 |
| keys() | Key 목록 |
| values() | Value 목록 |
| items() | Key-Value |
| pop() | 삭제 |
| update() | 여러 값 수정 |
| clear() | 전체 삭제 |

---

# 6. 자료형 비교

| 특징 | List | Tuple | Set | Dictionary |
|------|------|-------|-----|------------|
| 순서 | O | O | X | O |
| 중복 | O | O | X | Key X |
| 수정 가능 | O | X | O | O |
| 인덱싱 | O | O | X | X |
| Key 사용 | X | X | X | O |

---

# 7. 언제 사용할까?

### List

순서가 중요하고 수정이 필요한 데이터

```python
scores = [90, 80, 100]
```

---

### Tuple

변경되면 안 되는 데이터

```python
point = (100, 200)
```

---

### Set

중복 제거

```python
nums = [1,1,2,2,3]

unique = set(nums)
```

---

### Dictionary

검색이 빠른 데이터

```python
phone = {
    "Tom": "010-1111-1111",
    "Jane": "010-2222-2222"
}
```

---

# 8. 코딩 테스트에서 가장 많이 사용하는 Container

| 자료형 | 사용 빈도 |
|---------|----------|
| List | ⭐⭐⭐⭐⭐ |
| Dictionary | ⭐⭐⭐⭐⭐ |
| Set | ⭐⭐⭐⭐ |
| Tuple | ⭐⭐⭐ |

---

# 9. 핵심 요약

- **List** : 순서 O, 중복 O, 수정 O
- **Tuple** : 순서 O, 중복 O, 수정 X
- **Set** : 순서 X, 중복 X, 수정 O
- **Dictionary** : Key-Value 저장, 검색 속도가 빠름

## 암기 공식

```
List        = []  → 수정 가능
Tuple       = ()  → 수정 불가
Set         = {}  → 중복 제거
Dictionary  = {}  → Key : Value
```

> **Tip**
>
> - 순서대로 저장 → **List**
> - 변경하면 안 되는 데이터 → **Tuple**
> - 중복 제거 → **Set**
> - 빠른 검색 및 매핑 → **Dictionary**
```

# Python 제어문(Control Statement)

## 1. 제어문이란?

**제어문(Control Statement)**은 프로그램의 **실행 순서**를 제어하는 문법입니다.

기본적으로 파이썬은 **위에서 아래로 순차적으로 실행**됩니다.

```python
print("첫 번째")
print("두 번째")
print("세 번째")
```

출력

```
첫 번째
두 번째
세 번째
```

하지만 조건에 따라 실행하거나 여러 번 반복해야 하는 경우에는 **제어문**을 사용합니다.

---

# 2. 제어문의 종류

| 종류         | 설명                      |
| ---------- | ----------------------- |
| if         | 조건에 따라 실행               |
| match-case | 여러 경우를 선택(Python 3.10+) |
| for        | 반복                      |
| while      | 조건 반복                   |
| break      | 반복 종료                   |
| continue   | 현재 반복 건너뛰기              |
| return     | 함수 종료 및 값 반환            |

---

# 3. if문

조건이 **참(True)**이면 실행됩니다.

## 기본 문법

```python
if 조건식:
    실행문
```

예제

```python
money = 30000

if money >= 20000:
    print("택시를 타고 가라.")
```

출력

```
택시를 타고 가라.
```

---

# 4. if ~ else

조건이 참이면 `if`를 실행하고,

거짓이면 `else`를 실행합니다.

```python
money = int(input("현재 보유 금액 입력 : "))

if money >= 20000:
    print("택시를 타고 가라.")
else:
    print("걸어가라.")

print("Good night!!!")
```

예시

입력

```
25000
```

출력

```
택시를 타고 가라.
Good night!!!
```

---

# 5. if문으로 값 변경하기

조건을 만족하면 값을 변경할 수 있습니다.

```python
ent = 10000

age = int(input("나이 입력 : "))

if age >= 20:
    ent = ent + ent * 0.1

print(f"입장료 = {ent}")
```

입력

```
25
```

출력

```
입장료 = 11000.0
```

> **Tip**
>
> `ent += ent * 0.1`처럼 축약해서 작성할 수도 있습니다.

---

# 6. if ~ elif ~ else

여러 조건을 검사할 때 사용합니다.

```python
if 조건1:
    실행문
elif 조건2:
    실행문
elif 조건3:
    실행문
else:
    실행문
```

예제

```python
score = int(input("점수 입력 : "))

if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
elif score >= 60:
    print("D학점")
else:
    print("F학점")
```

입력

```
85
```

출력

```
B학점
```

> **주의**
>
> `elif`는 위에서부터 차례대로 검사하므로, **처음 만족하는 조건만 실행**됩니다.

---

# 7. 논리 연산자

여러 조건을 함께 사용할 수 있습니다.

| 연산자 | 의미      |
| --- | ------- |
| and | 모두 참    |
| or  | 하나라도 참  |
| not | 참/거짓 반전 |

예제

```python
age = 25

if age >= 20 and age < 30:
    print("20대입니다.")
```

---

# 8. 윤년 판별 예제

윤년은 다음 조건을 만족합니다.

* 4의 배수
* 100의 배수가 아니거나
* 400의 배수

```python
year = int(input("년도 입력 : "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year}년은 윤년(leap year)입니다.")
else:
    print(f"{year}년은 평년(common year)입니다.")
```

예시

입력

```
2024
```

출력

```
2024년은 윤년(leap year)입니다.
```

---

# 9. 들여쓰기(Indentation)

파이썬은 **들여쓰기**로 코드의 범위를 구분합니다.

올바른 예

```python
if True:
    print("Hello")
```

잘못된 예

```python
if True:
print("Hello")
```

```
IndentationError
```

> **Tip**
>
> 일반적으로 공백 4칸을 사용합니다.

---

# 10. 비교 연산자

| 연산자 | 의미     |
| --- | ------ |
| ==  | 같다     |
| !=  | 다르다    |
| >   | 크다     |
| <   | 작다     |
| >=  | 크거나 같다 |
| <=  | 작거나 같다 |

예제

```python
x = 10

if x == 10:
    print("같다")
```

---

# 11. 핵심 요약

* 제어문은 프로그램의 실행 순서를 제어한다.
* `if`는 조건이 참일 때 실행된다.
* `if ~ else`는 참/거짓을 구분한다.
* `if ~ elif ~ else`는 여러 조건을 처리한다.
* `and`, `or`, `not`으로 여러 조건을 조합할 수 있다.
* 파이썬은 **들여쓰기**가 매우 중요하다.

## 암기 공식

```
if 조건:
    실행문

if 조건:
    실행문
else:
    실행문

if 조건1:
    실행문
elif 조건2:
    실행문
else:
    실행문
```
