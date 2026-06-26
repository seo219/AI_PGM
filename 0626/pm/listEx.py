# list
# list는 변경 가능하다. 즉, list에 저장된 값을 변경할 수 있다.

list1 = list()
list2 = []

str1 = "abcd"
str2 = ['a', 'b', 'c', 'd']

# [start:stop:step] 슬라이싱 ex : [1:4:2] -> 1부터 4까지 2씩 증가하면서 슬라이싱
print(str2[1:4:2])  # ['b', 'd']

# append(x)	맨 뒤에 요소 추가	lst.append(10)
# extend(iterable)	여러 요소 한 번에 추가	lst.extend([1,2,3])
# insert(i, x)	원하는 위치에 삽입	lst.insert(0, 100)
# remove(x)	값으로 삭제 (첫 번째만)	lst.remove(5)
# pop([i])	인덱스로 삭제 후 반환	lst.pop()
# clear()	모든 요소 삭제	lst.clear()
# index(x)	값의 위치 반환	lst.index(20)
# count(x)	값의 개수 반환	lst.count(3)
# sort()	리스트 정렬	lst.sort()
# reverse()	리스트 뒤집기	lst.reverse()
# copy()	얕은 복사	new_lst = lst.copy()

# CRUD = Create, Read, Update, Delete

# tuple
# list와 거의 동일하지만, tuple은 변경 불가하다. 즉, tuple은 한 번 정의하면 값을 변경할 수 없다.

tuple1 = tuple()
tuple2 = ()

tup1 = (1) # int tup1 = 1 // tuple이 아니라 int형으로 인식
tup2 = (1,) # tuple
tup3 = (1,2,3)
tup4 = 1,2,3

# https://docs.python.org/3 공식 설명서
# https://w3schools.com/python 초보자용
# https://roadmap.sh 종류별 로드맵

# set // 집합 자료형
# set은 중복을 허용하지 않는다. 즉, set에 저장된 값은 모두 유일해야 한다.
# set은 순서가 없다. 즉, set에 저장된 값은 순서가 없기 때문에 인덱스로 접근할 수 없다.

# & 교집합 intersection
# | 합집합 union
# add()	요소 추가	s.add(4)
# update()	여러 요소 한 번에 추가	s.update([4,5,6])
#remove()	값으로 삭제 (없으면 오류)	s.remove(3)
# discard()	값으로 삭제 (없어도 오류 없음)	s.discard(3)
#clear()	모든 요소 삭제	s.clear()

# dictionary // 사전 자료형
# dictionary는 key와 value를 한 쌍으로 저장하는 자료형이다.

dic = {"key1": "value1", "key2": "value2", "key3": "value3"}

dict1 = {1:"apple", "ba":"banana"}
print(dict1[1]) # apple
print(dict1["ba"]) # banana
# print(dict1[2]) # KeyError // 존재하지 않는 key(현재는 2)를 사용했을 때 발생

stud1 = {"name": "홍길동", "age": 20, "dept": "소프트웨어"}

# 컨테이너 자료형은 list, tuple, set, dictionary가 있다. 이들은 모두 반복 가능한 자료형이다. 즉, for문을 사용하여 반복할 수 있다.

# 딕셔너리 추가하기
stud1["score"] = 85  # 새로운 key-value 쌍 추가
print(stud1)  # {'name': '홍길동', 'age': 20, 'dept': '소프트웨어', 'score': 85}
# 주의점
# 딕셔너리에서 key는 중복될 수 없다. 즉, 같은 key를 사용하면 기존의 value가 새로운 value로 덮어쓰여진다.
# 딕셔너리에서 key는 변경할 수 없다. 즉, key는 변경 불가해야 한다. 따라서 list는 key로 사용할 수 없다. tuple은 key로 사용할 수 있다.
# 딕셔너리에서 value는 중복될 수 있다. 즉, 같은 value를 여러 key에 사용할 수 있다.

# get() 함수는 key를 사용하여 value를 가져오는 함수이다. 만약 존재하지 않는 key를 사용하면 None을 반환한다.
print(stud1.get("name"))  # 홍길동
# items() 함수는 key와 value를 튜플로 반환하는 함수이다.
print(stud1.items())  # dict_items([('name', '홍길동'), ('age', 20), ('dept', '소프트웨어'), ('score', 85)])
