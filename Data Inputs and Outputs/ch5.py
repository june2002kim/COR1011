n1, n2, n3 = input("Enter Names: ").split()
s1, s2, s3 = input("Enter Scores: ").split()
s1=float(s1)
s2=float(s2)
s3=float(s3)
sums=s1+s2+s3
avg=sums/3
print("{} : {:5.2f}".format(n1, s1))
print("{} : {:5.2f}".format(n2, s2))
print("{} : {:5.2f}".format(n3, s3))
print("총합 : %d" %sums, end=" & ")
print("평균 : %.2f" %avg)
print()
myN=input("Enter your name: ")
myS=int(input("Enter your score: "))
print("%s score is %d" %(myN, myS))