def fun(num):
    i=0
    while i<len(num):
        num.reverse()
        i+=1
    print(num)
num = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
fun(num)
