print("Script Test")    #문자열 출력
print((5-3.5)*9)    #print() 함수 내의 수식 실행한 결과 출력
(5-3.5)*9   #수식 실행만 하고 결과는 출력되지 않음
a=10
b=20
print("a = ")
print(a)
print("b = ", b)    #변수 값 출력
print((a+b) - b/a)  #변수 값 참조해서 수식 실행
print()
num1, num2, s = 10, 34.1, "ans : "
print(type(num1), type(num2), type(s))
num1, num2 = num2, num1
print("num1 = ", num1, "num2 = ", num2)
num1 = int(num1)
num2 = float(num2)
print("num1 = ", num1, "num2 = ", num2)
print(s+str(num1)+str(num2))
