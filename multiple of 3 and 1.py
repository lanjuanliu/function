# Define a function which takes one parameter(positive integer). This function returns the sum of all multiples of 3 and 5 (not neccessary common multiples) in the range 1 to the integer passed as the parameter
def func_name(num):
    i=0
    sum=0
    while i<=num:
        if i%3==0 :
            print(i)
        if i%5==0:
            print(i)   
        i+=1
func_name(10)