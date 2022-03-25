def func(num):
# a=[1,2,3,4,5]
    c=[]
    sum=0
    i=0
    while i<len(num):
        sum=sum+num[i]
        c.append(sum)
        i+=1
    print(c)
num=[1,2,3,4,5]
func(num)
