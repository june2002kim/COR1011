score=int(input("점수 입력 : "))
if score>=90:
    grade="A"
    if score>=95:
        a=10
    else:
        a=9

elif score>=80:
    grade="B"
    if score>=85:
        a=8
    else:
        a=7

elif score>=70:
    grade="C"
    if score>=75:
        a=6
    else:
        a=5

elif score>=60:
    grade="D"
    if score>=65:
        a=4
    else:
        a=3

else:
    grade="F"
    a=0

print(grade, score+a)
