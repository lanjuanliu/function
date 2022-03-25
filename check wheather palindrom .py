def func(num):
    i=0
    while i<len(num):
        a=(num[::1])
        if a==num:
            print("palindrom")
        else:
            print("not palindrom")
        i+=1
num=[1,2,3]
func(num)