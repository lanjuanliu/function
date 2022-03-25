def func(num):
    # a=[]
    i=0
    while i<len(num):
        num.sort()
        # a.append(num)
        i+=1
    print(num)
num = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
func(num)