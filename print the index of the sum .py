def func(a):
    # a=[1,2,3,4,5]
    i=0
    b=[]
    user=int(input("enter your number: "))
    while i<len(a):
        j=0
        c=[]
        while j<len(a):
            if a[i]+a[j]==user:
                c.append(i)
                c.append(j)
            j+=1
        b.append(c)
        i+=1
    print(b)
a=[1,2,3,4,5]
func(a)
        



