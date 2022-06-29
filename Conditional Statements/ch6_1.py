n=input("Enter a numaber:")
if n.isnumeric():
    n=int(n)
    if n%2:
        s="odd"
    else:
        s="even"
    print("{} is {}".format(n,s))
else:
    print("Not numeric Data!")
name=input("Enter name : ")
if len(name)!=0:
    print("{} is your name".format(name))
else:
    print("No data!")
