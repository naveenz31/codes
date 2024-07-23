a=[]
print("Enter 10 Numbers")
for i in range(5):
    b=int(input("enter a number "+str(i+1)+" :"))
    a.append(b)
print(a)
b=0
for i in a:
    b=b+i
print(b)
