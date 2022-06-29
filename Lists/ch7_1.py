L=[]
print("L =", L)

L[len(L):len(L)]=['a', 'b']
print("L =", L)

L[len(L):len(L)]=['ab']
print("L =", L)

L[len(L):len(L)]=[['c','d']]
print("L =", L)

L[-1:-1]=[['cd']]
print("L =", L)

del L[2:4]
print("L =", L)

L[2:2]=['ab', 'cd']
print("L =", L)
