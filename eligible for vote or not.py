# Create a funciton named eligibleforvote which tell the user if he/she is eligible to vote or not.( Consider minimum age of voting to be 18. )
def vote(age):
    if age>=18:
        print("eligible")
    else:
        print("not eligible")
vote(age=int(input("enter the number")))
