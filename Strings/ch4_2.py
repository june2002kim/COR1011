Day = "2020/09/01"
L=Day.split("/")
print(L, type(L))
print(" ".join(L))
names = "David,Hyu,Lim"
n1, n2, n3 = names.split(",")
print(n1, n2, n3)
scores="28 91 30"
s1, s2, s3 = scores.split()
print(s1, s2, s3)
print(s1.isalpha())
print(n1.islower())
print(n2.isalnum())
print(s2.isspace())
print(s3.isnumeric())
new_n1=n1.upper()
print(new_n1, n1)

s="This is CT class #10"
s1 = s.replace("10", "13")
s2 = s.replace("#", "")
print(s1, s2, s)
