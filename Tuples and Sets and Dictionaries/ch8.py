a=int(input("enter int num : "))

T1=(a,)
print("튜플 T1 =", T1)

T2=(3, 4, 5)
T=T1+T2
print("T =", T)

s1=set(T)
print("set s1 =", s1)

L=[4, 5, 6, 7]
s1.update(L)
print("set s1 =", s1)

s1del=s1.pop()
print("set s1 =", s1, "제거한 데이터 =", s1del)

D={}
print("D =", D)

D['5반']=[2, 'D104']
D['6반']=[3, 'D105']
D['13반']=[3, 'D104']
D['14반']=[4, 'D105']

print("D =", D)

print("사전 D의 items =", list(D.items()))

b=input("enter key : ")
print("%s 의 value 값은" %b, D.get(b, 'Not exist'), "입니다")

