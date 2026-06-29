def add(a, b):
    return a + b

# add = lambda a, b: a + b

result = add(5, 3)
print(result)

def add(a, b):
    """
    두 숫자를 더하는 함수

    Parameters:
    a (int, float): 첫 번째 숫자
    b (int, float): 두 번째 숫자

    Returns:
    int, float: 두 숫자의 합
    """
    return a + b

# 독스트링 확인하기
print(add.__doc__)

print(print.__doc__)