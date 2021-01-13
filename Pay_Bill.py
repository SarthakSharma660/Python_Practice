import random

# write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

names_string = input("Give me everybody's names, separated by a comma. ")
# split function seperates string and arrange them in list 
names = names_string.split(", ")
name_length=len(names)
random_num= random.randint(0,name_length-1)
final_name=print(names[random_num])
print(f"{final_name} is the person who will pay the bill.")