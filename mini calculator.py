a=int(input("A :"))
b=int(input("B :"))
oper=input("add\sub\mul\div :")
if(oper=="add"):
    print(a+b)
elif(oper=="sub"):
    print(a-b)
elif(oper=="mul"):
    print(a*b)
elif(oper=="div"):
    print(a/b)
else:
    print("invalid operator selected")
