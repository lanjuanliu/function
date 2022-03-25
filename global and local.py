# num=[1,2,3,4,5,6]
def num():
    num=[1,2,3,4,5,6]
    i=0
    j=[]
    while i<len(num):
        c=num[i].split()
        d=list(c)
        i+=1
        j.append(d)
    print(j)
num()