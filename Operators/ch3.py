import math

a = 5
if((a%2)==1):
    print("a는 홀수")
else:
    print("a는 짝수")

a=10; b=4; x=10.0; y=4.0
r1=a+b
r2=a+x
r3=a/b

print(r1, type(r1))
print(r2, type(r2))
print(r3, type(r3))

print((0.1+0.1+0.1)==0.3)
print(round(0.1+0.1+0.1, 10)==round(0.3,10))

num=81
if((num**0.5==math.pow(num,0.5)) and (math.pow(num,0.5)==math.sqrt(num))):
    print("GOOD!!")
