def charCount(n):
    D={}
    
    for i in n:
        D[i]=n.count(i)

    return D


n=input("문자열 입력 : ")
n=n.lower()
n=n.replace(' ', '')

D=charCount(n)

if len(D)==0:
    print("No input data!!! OR Only space char.")

else:
    for j in D.keys():
        print("%c : %d" %(j, D[j]))
    
