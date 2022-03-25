# Q45. Draw a flowchart to Take 10 numbers as input and create a list of the numbers from the user and update each element of the list according to below rule
# If it is even, then multiply it by 100
# If it is odd, then multiply it by -1

def func():
    i=0
    while i<10:
        num=int(input("enter the number"))
        if num%2==0:
            a=num*100
            print(a)
        else:
            b=num*(-1)
            print(b)
        i+=1
func()