import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
RPS_list=[rock,paper,scissors]
choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if choose<3 :
  print(RPS_list[choose])

  num=random.randint(0,2)

  print(RPS_list[num])
  win_list=[["D","L","W"],["W","D","L"],["L","W","D"]]
  if win_list[choose][num]=="W" :
      print("You win")
  elif win_list[choose][num]=="L":
   print("You Lose")
  else:
    print("Draw")
else :
  print("You choose a invalid option")



