majorB={"computer":[9, "R"], "math":[2, "AS"], "elec":[11, "R"], "psy":[1, "X"]}

a=input("학과명을 입력 : ")

if a in majorB:
    print("%s과는 %s 건물 %d 층으로 배정합니다." %(a, majorB[a][1], majorB[a][0]+1))
    majorB[a][0]=majorB[a][0]+1

elif a=='':
    print("ERROR : No Data!!")

else:
    print("%s과 정보가 없습니다. GN 건물 1층에 배정합니다." %a)
    majorB[a]=[1, 'GN']

majorb=sorted(majorB.items())
print("\nsorting :", majorb)
