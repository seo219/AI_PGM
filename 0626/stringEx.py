#위키독스 점프 투 파이썬 참고 https://wikidocs.net/12

def print_hello():
    print("hello Python!")
    print('hello\tPython!')
    print("""h\ne\nl\nl\no
Python!\n""") # """ 사용하면 여러 줄을 출력할 수 있다.

def string_indexing():
    a = "Life is too short, You need Python"

    print(f"Life is too short, You need Python의 index 3 = {a[3]}")
    print(f"Life is too short, You need Python의 index -1 = {a[-1]}\n")

    print(f"Life is too short, You need Python의 index 0~3 = {a[0:4]}")
    print(f"Life is too short, You need Python의 index 처음~3 = {a[:4]}\n") # a[:4]은 a[0:4]와 같다.

    print(f"Life is too short, You need Python의 index -6~34 = {a[-6:34]}")
    print(f"Life is too short, You need Python의 index -6~문자열 길이 = {a[-6:len(a)]}")
    print(f"Life is too short, You need Python의 index -6~끝 = {a[-6:]}\n") # a[-6:]은 a[-6:len(a)]와 같다.

def numtype_example():
    b = 3
    c = 5
    print("I ate %d apples." % b)
    print("I ate %d apples. and %d oranges. So I ate a total of %d fruits.\n" % (b, c, b + c))

    d = 3.1415926535
    print("I ate %d apples." % d) # 정수형으로 출력되므로 소수점 이하가 버려진다.
    print("I ate %f apples." % d) # 소수점 이하 6자리까지 출력된다.
    print("I ate %.2f apples.\n" % d) # 소수점 이하 2자리까지 출력된다.

def string_formatting():
    str1 = "Sample Python String"
    print("example string: %s" % str1) # 문자열 그대로 출력된다.
    print("%-10s %10s\n" % (str1, str1)) # 왼쪽 정렬과 오른쪽 정렬을 할 수 있다. %-10s는 왼쪽 정렬, %10s는 오른쪽 정렬이다.

    print("I ate {}apples.".format(7)) # format() 함수를 사용하면 문자열 안에 {}를 넣고, format() 함수 안에 값을 넣어 출력할 수 있다.
    print("I ate {0}apples. and {1}oranges.\n".format(3, 5)) # {0}은 format() 함수 안의 첫 번째 값, {1}은 두 번째 값을 의미한다.
    
    name = "John"
    age = 30
    print(f"My name is {name}. I am {age} years old.\n") # f-string을 사용하면 문자열 안에 변수를 넣어 출력할 수 있다.

def comp():
    print("I ate 3 apples. and 5 oranges.")
    print(f"I ate 3 apples. and 5 oranges.")
    print(f"I ate %d apples. and %d oranges." % (3, 5))
    print("I ate {} apples. and {} oranges.".format(3, 5))
    print("I ate {0} apples. and {1} oranges.".format(3, 5))
    print(f"I ate {3} apples. and {5} oranges.")
    print("I ate 3+2 apples. and 5+3 oranges.") # 수식 계산이 아닌 문자열 그대로 출력된다.
    print(f"I ate {3+2} apples. and {5+3} oranges.") # f-string을 사용하면 수식 계산이 가능하다.


# 문자열 관련 함수 종류가 많으니까 나중에 필요할 때 찾아서 사용하기.
def string_function():
    a = "Python is the best choice"
    # count() 함수는 문자열 안에 특정 문자열이 몇 번 나오는지 세어준다.
    print(f"Python is the best choice에서 't'의 개수 = {a.count('t')}")
    # find() 함수는 문자열 안에 특정 문자열이 몇 번째 인덱스에 있는지 알려준다. 만약 찾는 문자열이 없으면 -1을 반환한다.
    print(f"Python is the best choice에서 't'의 인덱스 = {a.find('t')}")
    # index() 함수는 find() 함수와 동일하지만, 찾는 문자열이 없으면 오류를 발생시킨다.
    print(f"Python is the best choice에서 't'의 인덱스 = {a.index('t')}")
    # join() 함수는 문자열을 합쳐준다.
    print(f"Python is the best choice에서 ' '를 기준으로 합치기 = {' '.join(a)}")
    # upper() 함수는 문자열을 모두 대문자로 바꿔준다.
    print(f"Python is the best choice에서 모두 대문자로 바꾸기 = {a.upper()}")
    # lower() 함수는 문자열을 모두 소문자로 바꿔준다.
    print(f"Python is the best choice에서 모두 소문자로 바꾸기 = {a.lower()}")
    # strip() 함수는 문자열의 양쪽 공백을 제거해준다. lstrip() 함수는 문자열의 왼쪽 공백을, rstrip() 함수는 문자열의 오른쪽 공백을 제거해준다.
    b = "   Python is the best choice   "
    print(f"   Python is the best choice   에서 양쪽 공백 제거 = {b.strip()}")
    print(f"   Python is the best choice   에서 왼쪽 공백 제거 = {b.lstrip()}")
    print(f"   Python is the best choice   에서 오른쪽 공백 제거 = {b.rstrip()}")
    # replace() 함수는 문자열 안의 특정 문자열을 다른 문자열로 바꿔준다.
    print(f"Python is the best choice에서 'Python'을 'Java'로 바꾸기 = {a.replace('Python', 'Java')}")
    # split() 함수는 문자열을 특정 문자열을 기준으로 나눠준다.
    print(f"Python is the best choice에서 ' '를 기준으로 나누기 = {a.split(' ')}")
    # isalpha() 함수는 문자열이 알파벳으로만 이루어져 있는지 확인해준다. 만약 문자열이 알파벳으로만 이루어져 있으면 True를, 그렇지 않으면 False를 반환한다.
    print(f"Python is the best choice가 알파벳으로만 이루어져 있는지 확인 = {a.isalpha()}")
    # isdigit() 함수는 문자열이 숫자로만 이루어져 있는지 확인해준다. 만약 문자열이 숫자로만 이루어져 있으면 True를, 그렇지 않으면 False를 반환한다.
    print(f"Python is the best choice가 숫자로만 이루어져 있는지 확인 = {a.isdigit()}")
    #startswith() 함수는 문자열이 특정 문자열로 시작하는지 확인해준다. 만약 문자열이 특정 문자열로 시작하면 True를, 그렇지 않으면 False를 반환한다.
    print(f"Python is the best choice가 'Python'으로 시작하는지 확인 = {a.startswith('Python')}")
    #endswith() 함수는 문자열이 특정 문자열로 끝나는지 확인해준다. 만약 문자열이 특정 문자열로 끝나면 True를, 그렇지 않으면 False를 반환한다.
    print(f"Python is the best choice가 'choice'로 끝나는지 확인 = {a.endswith('choice')}\n")

def input_example():
    a = int(input("Enter first number: ")) # input() 함수는 문자열을 반환하므로, int() 함수를 사용하여 정수형으로 변환해야 한다.
    b = int(input("Enter second number: "))
    
    print(f"\nYou entered: {a} and {b}.\n")
    
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}\n")

def list_example():
    a = [1, 2, 3, 4, 5]
    b = ["a", "b", "c", "d", "e"]
    c = [1, 2, "a", "b", True, False]
    d = [1, 2, ["a", "b", "c"], 3, 4]
    # 위에서 설명한 문자열 인덱스 관련 내용과 거의 같다. 따로 찾아보기. 다른 함수들도 많으니 필요할 때 찾아서 사용하기.
