def func(num):
    count=0
    i=0
    while i<len(num):
        if num[i]<="z":
            count+=1
        i+=1
    return count
num="Lanjuanliu Panmei"
print(func(num))