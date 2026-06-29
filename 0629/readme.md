# Python 기초 문법 요약

## 1. 대입(assignment)과 표현식(expression)

대입은 **오른쪽 수식의 결과를 왼쪽 변수에 저장**하는 것이다 [web:1].

```python
a = 1
a = b
a = b + 1
a = sum(1, 2) * a + 1
```

- `literal` 또는 `constant`: `a = 1`
- `variable`: `a = b`
- `operator`: `a = b + 1`
- `function`: `a = sum(1, 2) * a + 1`

---

## 2. 비교 연산자와 논리 연산자

### 비교 연산자
```python
<, <=, >, >=, ==, !=, in, not in, is, is not
```

### 논리 연산자
```python
not, and, or
```

- `==` 는 값 비교
- `is` 는 객체 동일성 비교
- `in`, `not in` 은 포함 여부 확인

---

## 3. 조건문

파이썬에서는 `if`, `if-else`, `if-elif-else`를 사용한다 [web:3].

```python
if 조건식:
    pass
else:
    print(" ")
```

### 조건문 종류
1. `if`
2. `if else`
3. `if elif else`

---

## 4. match-case

`match-case`는 값 패턴에 따라 분기할 때 사용한다 [web:3].

```python
match 수식:
    case 값1:
        ...
    case 값2:
        ...
    case _:
        ...
```

- `case _` 는 기본값 역할을 한다.

---

## 5. 삼항 연산자

일반적인 삼항 연산자는 다음 형태이다.

```python
(조건식) ? "A" : "B"
```

파이썬에서는 다음처럼 쓴다.

```python
"A" if 조건식 else "B"
```

예시:

```python
"합격" if score >= 80 else "불합격"
```

- 짧게 쓰기 좋지만, 가독성이 떨어질 수 있어 자주 쓰지는 않는다.

---

## 6. 프로그래밍 에러 종류

프로그래밍 에러는 보통 3가지로 나눈다.

1. `syntax error`  
   - 문법 오류
2. `runtime error` (`exception`)  
   - 실행 중 발생하는 오류
3. `semantic error`  
   - 문법은 맞지만 의미가 잘못된 오류

---

## 7. 반복문

C언어 스타일의 반복문은 다음과 같다.

```python
for(초기식; 조건식; 증감식)
```

파이썬에서는 `for-in` 구조를 사용한다 [web:3].

```python
for 변수 in 리스트(또는 튜플, 문자열):
    실행문
```

### range 사용
```python
range(start, stop, step)
```

예시:

```python
for i in range(1, 10, 2):
    print(i)
```

---

## 8. 함수

함수는 특정 작업을 묶어 재사용할 수 있게 해준다 [web:3].

```python
def 함수_이름(매개변수):
    수행할 문장
```

예시:

```python
def add(a, b):
    return a + b
```

---

## 9. 파일의 구성

파일은 크게 두 가지 정보로 볼 수 있다.

1. 파일에 대한 정보  
   - 파일 이름과 확장자
   - 파일 소유자
   - 파일 생성일 등
2. 파일 내용

---

## 10. 파일 경로와 슬래시

파이썬 코드에서 파일 경로는 `/`를 사용할 수 있다.

```python
"C:/doit/새파일.txt"
```

역슬래시 `\`를 쓸 경우에는 이스케이프 문자 때문에 주의해야 한다.

```python
"C:\\doit\\새파일.txt"
r"C:\doit\새파일.txt"
```

예를 들어 `"C:\note\test.txt"`처럼 쓰면 `\n`이 줄바꿈으로 해석될 수 있다.

---

## 11. 인코딩과 UTF-8

인코딩은 문자를 숫자로 바꿔 저장하는 규칙이다 [web:3].

- 예: `'A' -> 65`
- UTF-8은 현재 널리 쓰이는 인코딩 방식
- 영어, 한글, 중국어, 일본어, 이모지 등을 표현할 수 있다

파일 저장/읽기에서 UTF-8을 쓰면 한글이 깨질 가능성이 줄어든다.

---

## 12. 파일 열기와 닫기

파일은 보통 `open -> use -> close` 순서로 다룬다.

```python
f = open("새파일.txt", "w")
f.close()
```

예시:

```python
f = open("C:/doit/새파일.txt", "w")
f.close()
```

---

## 13. 폴더 만들기

존재하지 않는 경로에 파일을 만들기 전에 폴더를 먼저 생성해야 한다.

```python
import os

os.makedirs("C:/doit", exist_ok=True)

f = open("C:/doit/새파일.txt", "w")
f.close()
```

- `exist_ok=True` 를 쓰면 폴더가 이미 있어도 오류가 나지 않는다.

---

## 14. sys.argv 사용

`sys.argv`는 명령줄 인자를 받을 때 사용한다 [web:9].

```python
import sys

args = sys.argv[1:]
for i in args:
    print(i)
```

### 실행 예시
```bash
python sysArgvEx01.py
```

- 출력: 없음

```bash
python sysArgvEx01.py 123 456 789
```

- 출력:
```text
123
456
789
```

---

## 15. 한눈에 보는 핵심

- 대입은 `변수 = 표현식` 형태이다.
- 조건문은 `if`, `elif`, `else`를 사용한다.
- 반복문은 파이썬에서 `for-in`과 `range()`를 자주 사용한다.
- 함수는 `def`로 정의한다.
- 파일 경로는 `/`를 쓰거나 `\`를 이스케이프 처리해야 한다.
- UTF-8은 가장 널리 쓰이는 인코딩이다.
- `sys.argv`는 명령줄 인자를 처리할 때 사용한다.
