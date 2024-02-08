import random

answer = random.randint(1,100)
chance = 7

while chance > 0:
    inputnum = int(input("기회는 7번, 1~100까지 숫자를 적으시오: "))
    if inputnum == answer:
        print('정답입니다.')
        chance = -1
    elif inputnum > answer:
        print('down')
        chance = chance -1
    else:
        print('up')
        chance = chance -1
if chance == 0:
    print(f'실패, 정답은 {answer}입니다.')