def func_name(num):
    i=2
    count=0
    while i<=num:
        if num%i==0:
            count+=1
        i+=1
    if count==1:
        print("prim number")
    else:
        print("not prim number")
num=int(input("enter the numbre"))
func_name(num)


