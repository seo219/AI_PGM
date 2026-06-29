#while
def whileEx():
    treeHit = 0
    while treeHit < 10:
        treeHit += 1
        print(f"You hit the tree {treeHit} times.")
        if treeHit == 10:
            print("The tree has fallen down.")


# break
def whileBreak():
    coffee = 10
    while True:
        money = int(input("돈을 넣어 주세요: "))
        if money == 300:
            print("커피를 줍니다.")
            coffee = coffee -1
        elif money > 300:
            print(f"거스름돈 {money - 300}를 주고 커피를 줍니다.")
            coffee = coffee -1
        else:
            print("돈을 다시 돌려주고 커피를 주지 않습니다.")
            print(f"남은 커피의 양은 {coffee}개입니다.")
        if coffee == 0:
            print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
            break

# continue
def whileContinue():
    a = 0
    while a < 10:
        a = a + 1
        if a % 2 == 0: continue
        print(a)

# while else
def whileElse():
    count = 0
    while count < 3:
        print(f"카운트: {count}")
        count += 1
    else:
        print("while 문이 정상 종료되었습니다.")

# while else break
def whileElseBreak():
    count = 0
    while count < 5:
        if count == 2:
            break
        print(f"카운트: {count}")
        count += 1
    else:
        print("while 문이 정상 종료되었습니다.")

# while in while
def whileInWhile():
    i = 2
    while i <= 3:
        j = 1
        while j <= 9:
            print(f"{i} x {j} = {i*j}")
            j += 1
        i += 1

whileInWhile()