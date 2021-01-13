# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# take current age as an input from the user
age=input("Enter your current age: " )
#finding out left over age and type converting str 'age' to int
left_age=90-int(age)
#Calculating days, weeks and months left
days= left_age*365
weeks= left_age*52
months=left_age*12
# printing the data
print(f"You have {days} days, {weeks} weeks, and {months} months left.")