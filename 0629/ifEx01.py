
# if VS match

def gradeCal():
    grade = input("Enter your grade: ")
    if grade == 'A':
        print("Excellent!")
    elif grade == 'B':
        print("Good job!")
    elif grade == 'C':
        print("You can do better.")
    elif grade == 'D':
        print("You need to work harder.")
    else :
        print("Invalid grade.")

def scoreCal():
    score = int(input("Enter your score: "))

    if score >= 90:
        print("Excellent!")
    elif score >= 80:
        print("Good job!")
    elif score >= 70:
        print("You can do better.")
    elif score >= 60:
        print("You need to work harder.")
    else:
        print("You need to improve your performance.")

def GradeCalMat():
    grade = input("Enter your grade: ")
    match grade:
        case 'A':
            print("Excellent!")
        case 'B':
            print("Good job!")
        case 'C':
            print("You can do better.")
        case 'D':
            print("You need to work harder.")
        case _:
            print("Invalid grade.")

def scoreCalMat():
    score = int(input("Enter your score: "))    
    oneDigit = score // 10

    match oneDigit:
        case 10 | 9:
            print("Excellent!")
        case 8:
            print("Good job!")
        case 7:
            print("You can do better.")
        case 6:
            print("You need to work harder.")
        case _:
            print("You need to improve your performance.")


scoreCalMat()    
print("Thank you for using the grade evaluator.")