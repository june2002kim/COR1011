L=list(int(x) for x in input("Enter int element of list L : ").split())
print("리스트 L =", L)

for i in range(len(L)):
    if L[i]%3==0:
        L[i]*=10
print("리스트 L =", L)

L=[]

for i in range(1, 100):
    if i%6==0:
        L.append(i)
print("리스트 L =", L)
for i in L:
    if i%4!=0 and i%7!=0:
        print(i, end=" ")

print()

for i in range(1, 10):
    for j in range(1, 10):
        print("%d*%d = %d" %(j, i, j*i), end=' ')
    print()
