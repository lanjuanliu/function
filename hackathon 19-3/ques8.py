# x=int(input("enter the no:"))
# y=int(input("enter the no:"))
def num(x,y):
    if x<y:
        print("bike is faster")
    elif x>y:
        print("car is faster")
    elif x==y:
        print("both are same")
x=int(input("enter the no:"))
y=int(input("enter the no:"))
num(x,y)