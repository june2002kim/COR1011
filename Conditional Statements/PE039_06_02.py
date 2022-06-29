num1, op, num2=input("수식 입력:").split()  # 수식 입력 받아 분리하기
num1, num2=float(num1), float(num2)    # 피연산자를 실수 데이터형으로 변환하기

if  op == "+" :
    result=num1+num2    # + 연산하여 결과 저장하기
    print("%.2f %s %.2f = %.2f "%(num1, op, num2, result))
    
elif  op == "*" :
    result=num1*num2    # * 연산하여 결과 저장하기
    print("%.2f %s %.2f = %.2f "%(num1, op, num2, result))
    
elif  op == "/" :
    # student coding part 
    if (num2==0):   # 두번째 피연산자가 0인지 체크하는 조건문
        print("0으로 나누기를 수행할 수 없습니다")
    else:
        result=num1/num2    # / 연산하여 결과 저장하기
        print("%.2f %s %.2f = %.2f "%(num1, op, num2, result))
        
elif  op == "-" :
    result=num1-num2    # - 연산하여 결과 저장하기
    print("%.2f %s %.2f = %.2f "%(num1, op, num2, result))
    
else:
    print("{} 는 지원하지 않는 연산자입니다".format(op))     # 지원하지 않는 연산자라고 출력하기
