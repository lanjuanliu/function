def func(*num):
    i=0
    while i<len(num):
        if num[i]%2==0:
            print("even")
        else:
            print("odd")
        i+=1
func(1,2,3,4,5,6,7,8,9,90)
