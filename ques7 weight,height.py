def func(weight,height):
    bmi=weight/height
    if bmi <= 18.5 :
        return "Underweight"
    if bmi <= 25.0 :
        return "Normal"
    if bmi <= 30.0 :
        return "Overweight"
    if bmi > 30 :
        return "Obese"
weight=int(input("enter the weight"))
height=int(input("enter the height"))
func(weight,height)