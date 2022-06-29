A=list(int(a) for a in input("Enter list A numbers : ").split())
B=list(int(b) for b in input("Enter list B numbers : ").split())

a=[]
b=[]
result=[]

for i in A:
    if i not in a:
        a.append(i)
for j in B:
    if j not in b:
        b.append(j)

for i in a:
    if i not in b:
        result.append(i)
for j in b:
    if j not in a:
        result.append(j)

print(sorted(result))
