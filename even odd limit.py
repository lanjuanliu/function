# Define a function which takes one argument which is the limit upto which the function has to print the numbers and their label(even or odd) as shown below.
def funcname(num):
    i=0
    while i<=num:
        if i%2==0:
            print("even")
        else:
            print("odd")
        i+=1
funcname(4)