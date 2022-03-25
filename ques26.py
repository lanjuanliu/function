def func(num):
    i=0
    while i<num:
        if i%3==0:
            print(i,"fizz")
        if i%5==0:
            print(i,"buzz")
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        i+=1
num=int(input("enter the number"))
func(num)