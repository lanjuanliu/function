
def add(num1,num2):
    print(num1+num2)
add(45,7)
def  add_num(a,b):
    i=0
    a1=0
    b1=0
    while i<len(a):
        a1=a1+a[i]
        b1=b1+b[i]
        i+=1
    print(a1)
    print(b1)
add_num([1,2,3],[3,6,7])