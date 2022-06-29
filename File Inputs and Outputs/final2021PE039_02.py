a, b=input("Enter two positive int nums : ").split()
a, b=int(a), int(b)

divisor1=set()
divisor2=set()
common_divisor=set()

for i in range(1, a+1):
    if a%i==0:
        divisor1.add(i)
for j in range(1, b+1):
    if b%j==0:
        divisor2.add(j)

print("first num divisor :", divisor1)
print("second num divisor :", divisor2)

for x in divisor1:
    if x in divisor2:
        common_divisor.add(x)

print("%d & %d common divisor : %s" %(a, b, common_divisor))
print("%d & %d greatest common divisor : %d" %(a, b, max(common_divisor)))
