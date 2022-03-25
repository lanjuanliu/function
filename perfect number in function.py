def number(num):
    sum=0
    i=1
    while i<num:
        if num%i==0:
            sum=sum+i
            if sum==num:
                print("perfect")
            else:
                print("not perfect")
        i+=1
number(6)


