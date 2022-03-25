def func(age):
    if age<=14:
        print("drink toddy")
    if age<=18 and age>14:
        print("drink coke")
    if age>18 and age<21:
        print("drink beer")
    if age>21:
        print("drink whiskey")
age=int(input("enter the age"))
func(age)