def plus(num1, num2):
    return (num1+num2)

def minus(num1, num2):
    return (num1-num2)

def multiply(num1, num2):
    return (num1*num2)

def divide(num1, num2):
    return (num1/num2)

num1, op, num2=input("수식 입력(예: 20 * 40) : ").split()
num1, num2=float(num1), float(num2)

if op=='+':
    result=plus(num1, num2)
    print("%f %c %f = %f" %(num1, op, num2, result))

elif op=='-':
    result=minus(num1, num2)
    print("%f %c %f = %f" %(num1, op, num2, result))

elif op=='*':
    result=multiply(num1, num2)
    print("%f %c %f = %f" %(num1, op, num2, result))

elif op=='/':
    if num2==0:
        print("%f 로 나누기를 수행할 수 없습니다" %num2)

    else:
        result=divide(num1, num2)
        print("%f %c %f = %f" %(num1, op, num2, result))

else:
    print("%c 지원하지 않는 연산자입니다" %op)
