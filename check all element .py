
# def func(num):
#     i=0
#     while i<len(num)-1:
#         if num[i]==num[i+1]:
#             return  True
#         i+=1
#     return  False
# num=[1,2,3,1]
# print(func(num)) 


# def func(num):
#     i=0
#     while i<len(num)-1:
#         if num[i]==num[i+1]:
#             return  True
#         i+=1
#     return  False
# num=[1,2,1,3,1]
# print(func(num)) 


def all_qyo(num):
    # if len(num)==1 or len(num)==0:
    #     return True
        i=0
        j=1
        while i<len(num) and j<len(num):
            if num[i]==num[j]:
                return True
            else:
                return  False
print(all_qyo([1,1,1,1,2,1,1]))