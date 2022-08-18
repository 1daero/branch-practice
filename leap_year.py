num = input("1~3000 사이의 정수를 입력하세요: ")
num = int(num)

if ((num %4 == 0) and (num %100 != 0)) or (num %400 == 0):
    print(num, "윤년입니다.")
else:
    print(num, "윤년이 아닙니다.")
