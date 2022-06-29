L=[9, 29, 19, 0, 99, 5]

a=input("추가할 데이터 입력:")

if a.isnumeric():
    a=int(a)
    if L.count(a)==0:
        L[len(L):len(L)]=[a]
    else:
        print("이미 존재하는 데이터!!")

else:
    print("0이상의 양의 정수, 숫자 데이터만 허용!!")

print(L)

'''
L=[9, 29, 19, 0, 99, 5]
a=input("추가할 데이터 입력 : ")

if not a.isnumeric():
    print("0이상의 양의 정수, 숫자 데이터만 허용!!")

else:
    if int(a) in L:
        print("이미 존재하는 데이터!!")

    else:
        L.append(int(a))

print(L)
'''
