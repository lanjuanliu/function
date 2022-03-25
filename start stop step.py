def func(min,max,step):
    i=min
    a=[]
    while i<=max:
        a.append(i)
        i+=step
    return a
min=int(input("enter the number: "))
max=int(input("enter the number: "))
step=int(input("enter your number: "))
print(func(min,max,step))                                                    
