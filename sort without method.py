def nummbers(num):
    b=len(num)
    for i in range(b):
        for j in range(i+1,b):
            if num[i]>num[j]:
                num[i],num[j]=num[j],num[i]
    print(num)
nummbers([1,3,8,6,4,6,0,90,23,5])



# def num(a):
#     # a=[1,2,3,4,23,5,8,6,78]
#     i=0
#     while i<len(a):
#         j=0
#         while j<len(a)-1:
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#             j+=1
#         i+=1
#         print(num)
# a=[1,2,3,4,23,5,8,6,78]
# num(a)