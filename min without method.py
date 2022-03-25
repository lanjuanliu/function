def min_num(num):
    i=0
    m=num[i]
    while i<len(num):
        if num[i]<m:
            m=num[i]
        i+=1
    print(m)
num=[12,34,6,8,97,78]
min_num(num)
