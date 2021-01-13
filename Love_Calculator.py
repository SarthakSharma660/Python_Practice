# write a program that tests the compatibility between two people. 
# We're going to use the super scientific method recommended by BuzzFeed.
#https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name3=name1+name2
name3=name3.lower()

t= name3.count('t')
r= name3.count('r')
u=name3.count('u')
e=name3.count('e')

true=(t+r+u+e)*10

l=name3.count('l')
o=name3.count('o')
v=name3.count('v')

love=l+o+v+e

score= true+love

if score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")