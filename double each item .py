def func(num):
    i=1
    x=[]
    while i<num:
        a=i*i
        x.append(a)
        i+=1
    print(x)
num=int(input("enter the number"))
func(num)