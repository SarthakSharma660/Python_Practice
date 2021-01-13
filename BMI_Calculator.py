# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# taking input from the user
height=input("enter your height in m :\n")
weight=input("enter your weight in kg :\n")
# as our input is in string from now we would convert into float 
new_height= float(height)
new_weight= float(weight)
# BMI= WEIGHT/HEIGHT*HEIGHT so for squaring any number we would use ** operator
BMI=float(new_weight/(new_height**2))
print(BMI)
# This program is very basic program anyone with small amout of knowdege of operators in python cando this program
