# a= [1,2,3,3,3,3,4,5]
def func(num):
    i=0
    b=[]
    while i<len(num):
        if num[i] not in b:
            b.append(num[i])
        i+=1
    print(b)
num= [1,2,3,3,3,3,4,5]
func(num)


