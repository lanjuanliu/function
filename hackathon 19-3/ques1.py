def func(x,n):
    if x[n-1]%10==0:
        print("yes")
    else:
        print("no")
n=int(input("enter the number"))
x=[85,25,65,21,84]
func(x,n)