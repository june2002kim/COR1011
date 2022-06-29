def isOverlap(a, b):
    result=set()
    for i in a:
        if i in b:
            result.add(i)

    return list(result)

list1=list(int(x) for x in input("enter list1 elements : ").split())
list2=list(int(x) for x in input("enter list2 elements : ").split())

result=isOverlap(list1, list2)

if len(result)==0:
    print("No overlapping elements")

else:
    print(list(result), "overlapping elements")
