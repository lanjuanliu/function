def check_num(a,b):
        if a%2==0 and b%2==0:
            print("even")
        else:
            print("odd")
check_num(4,6)
def check_numlist(c,d):
    i=0
    while i<len(c):
        a=c[i]+d[i]
        if a%2==0:
            print("both are even")
        elif a%2!=2:
            print("both are odd")
        i+=1
check_numlist([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])
