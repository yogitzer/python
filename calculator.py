
calc = int(input("1. 입력한 수식 계산 2.두 수 사이의 합계 : "))

if calc == 1:
   
    math = input("*** 수식을 입력하세요: ")
    answer = eval(math)
    print("%s 결과는 %5.1f입니다." %(math, answer))
    

if calc == 2:
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    sum = 0
    for i in range(num1, num2+1):
        sum = sum + i
    print("%d+...+%d는 %d입니다" %(num1, num2, sum))
1