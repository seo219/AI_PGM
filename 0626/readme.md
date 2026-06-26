# Python 리스트(List)

## 1. 리스트란?
파이썬 리스트는 여러 값을 하나의 변수에 저장할 수 있는 자료형입니다.  
대괄호 `[]`로 만들며, 순서가 있고 수정할 수 있습니다. [web:1][web:10]

## 2. 특징
- 순서가 있습니다.
- 수정할 수 있습니다.
- 중복 값을 허용합니다.
- 서로 다른 데이터 타입을 함께 저장할 수 있습니다. [web:1]

## 3. 리스트 생성
```python
fruits = ["apple", "banana", "cherry"]
numbers =[3][4][5][6][1]
mixed = ["text", 10, True]
```

## 4. 기본 사용법
### 길이 확인
```python
print(len(fruits))
```

### 인덱스 접근
```python
print(fruits)   # apple
print(fruits[-1])  # cherry
```

### 슬라이싱
```python
print(numbers[1:4])  #[4][5][3]
```

## 5. 값 추가
### append()
리스트 끝에 값을 추가합니다. [web:1][web:10]

```python
fruits.append("orange")
```

### insert()
원하는 위치에 값을 추가합니다.

```python
fruits.insert(1, "grape")
```

### extend()
여러 값을 한 번에 추가합니다.

```python
fruits.extend(["melon", "pear"])
```

## 6. 값 수정
인덱스를 이용해 값을 바꿀 수 있습니다.

```python
fruits = "mango"
```

## 7. 값 삭제
### remove()
특정 값을 삭제합니다. [web:10]

```python
fruits.remove("banana")
```

### pop()
인덱스로 삭제하며, 삭제한 값을 반환합니다. [web:10]

```python
fruits.pop()
fruits.pop(1)
```

### del
인덱스나 구간을 삭제합니다.

```python
del fruits
del fruits[1:3]
```

### clear()
리스트의 모든 값을 삭제합니다.

```python
fruits.clear()
```

## 8. 자주 쓰는 메서드
- `append()`: 끝에 추가
- `insert()`: 특정 위치에 추가
- `extend()`: 여러 값 추가
- `remove()`: 값 삭제
- `pop()`: 인덱스 삭제
- `clear()`: 전체 삭제
- `sort()`: 정렬
- `reverse()`: 역순 정렬 [web:10]

## 9. 정렬
```python
nums =[6][1][3][4]
nums.sort()
print(nums)  #[1][3][4][6]
```

## 10. 반복문과 함께 사용
```python
for item in fruits:
    print(item)
```

## 11. 예제
```python
students = ["Alice", "Bob", "Charlie"]

students.append("David")
students = "Bobby"[1]
students.remove("Charlie")

print(students)
```

## 12. 정리
리스트는 Python에서 가장 많이 쓰이는 자료구조 중 하나입니다.  
데이터를 저장, 수정, 삭제, 정렬할 때 매우 유용합니다. [web:1][web:10]
