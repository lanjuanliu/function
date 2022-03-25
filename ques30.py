def func(num): 
    i=1
    while i<=10:
        a=i*num
        print(num,"*",i,"=",a)
        i+=1
num=int(input("enter the number"))
func(num)