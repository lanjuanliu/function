from re import X


# def add(a,b):
#     d=a+b
#     return d
# def sub(c,e):
#     x=c-e
#     return X
# def symbol():
#     if =="+"


def add():
    d=user1+user2
    return d
def sub():
    c=user1-user2
    return c
def multiply():
    a=user1*user2
    return a
def symbol():
    if user3=="+":
        print(add())
    elif user3=="-":
        print(sub())
    elif user3=="*":
        print(multiply())
user1=int(input("enter the number"))
user2=int(input("enter the number"))
user3=input("enter the symbol")
symbol()
