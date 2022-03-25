def func(speed):
    if speed<=70:
        print(70,"okay")
    if speed>70:
        i=70
        while i<=70:
            point=(speed-70)//5
            if point>12:
                print(point,speed,"license suspended")
            else:
                print(point,speed,"okay")
            i+=1
speed=int(input("enter the speed"))
func(speed)