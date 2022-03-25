# def func(name="jian"):
#     print("student name=",name)
# func()
# func("teresa")
# func("lan")
# func("ning")

def func(*name):
    print("student name",name)
func("ning","teresa","jian","grace","lan")
def func(num=20,wee=30):
    if wee>20:
       print("wee greater than 20")
func(num=30)



        