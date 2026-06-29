def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def divi(a, b):
    if b == 0 :
        raise ValueError("Cannot divide by zero")
    return a / b

choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", sub(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", mul(num1, num2))
elif choice == '4':
    try:
        result = divi(num1, num2)
        print(num1, "/", num2, "=", divi(num1, num2))
    except ValueError as e:
        print(e)
else :
    print("Invalid choice value")