# def outer_func():
#     def inner_func():
#         print("lan")
#     inner_func()
# outer_func()


# def outer_func(who):
#     def inner_func():
#         print("Hello", who)
#     inner_func()
# outer_func("World!")


def func(x=1,y=2):
    x=x+y
    y+=1
    print(x,y)
func(y=2,x=1)