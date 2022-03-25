def func(num):
    a=num/4
    if a.is_integer:
        print("good")
    else:
        print("not good")
num=int(input("enter the num"))
func(num)