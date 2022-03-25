# a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
def func(num):
    i=0
    a=[]
    while i<len(num):
        if num[i]%2==0:
            a.append(num[i])
            # print(a)
        i+=1
    print(a)
num=[1, 2, 3, 4, 5, 6, 7, 8, 9]
func(num)
