def func(a,b):
    if len(a)>len(b):
        print(a)
    elif len(b)>len(a):
        print(b)
def name(c,d):
    if len(c)==len(d):
        print(c)
        print(d)
    if len(c)<len(d):
        print(d)
    if len(d)<len(c):
        print(c)
func("hello","welcome")
name("sonu","monu")