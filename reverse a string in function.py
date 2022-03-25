# a='1234abcd'
def func(num):
    i=1
    while i<len(num):
        a=(num[::-1])
        i+=1
    print(a)
num="abc123"
func(num)

