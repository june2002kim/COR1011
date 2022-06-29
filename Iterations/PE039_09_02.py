from random import*

a=randint(10, 20)
L=[]
x=1
y=0
cnt=0

for i in range(a):
    L.append(randint(-10, 10))
print("랜덤 정수 리스트 :", L)

while x<11:
    cnt=0
    y=0
    while y<a:
        if x==L[y]:
            cnt+=1
        y+=1   
    print("숫자 %d는 %d번 입력되었습니다." %(x, cnt))
    x+=1
