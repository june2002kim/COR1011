a, b, c=input("실수 세개 입력:").split()
a, b, c=float(a), float(b), float(c)

if c>b:
    if c>a:
        if a>b:
            a, b=b, a
    else:
        a, b=b, a
        b, c=c, b
else:
    if b>a:
        if c>a:
            b, c=c, b
        else:
            b, c=c, b
            b, a=a, b
    else:
        a, c=c, a
        
print("오름차순 정렬: %.1f %.1f %.1f" %(a, b, c))

'''
a, b, c=input("실수 세개 입력 : ").split()
a, b, c=float(a), float(b), float(c)

if c>b:
    max_=c
    if c>a:
        if a>b:
            min_=b
            num=a
        else:
            min_=a
            num=b
    else:
        max_=a
        min_=b
        num=c
elif b>c:
    max_=b
    if b>a:
        if a>c:
            min_=c
            num=a
        else:
            min_=a
            num=c
    else:
        max_=a
        num=b
        min_=c
    
print("오름차순 정렬 :", min_, num, max_)
'''
