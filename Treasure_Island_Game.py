print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

rl_input=input("You're at a cross road. Where do you want to go? Type left or right\n")
rl_input=rl_input.lower()

if rl_input=='left':
  lake_input=input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")

  if lake_input=='wait':

    colour_input=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")

    if colour_input=="red":
      print("It's a room full of fire. Game Over.")
    elif colour_input=="yellow":
      print("You found the treasure! You Win!")
    elif colour_input=="blue":
      print("You enter a room of beasts. Game Over.")
    else:
       print("You chose a door that doesn't exist. Game Over.")

  elif lake_input=="swim":
    print("You get attacked by an angry trout. Game Over.")
  else:
   print("You chose a door that doesn't exist. Game Over.")

elif rl_input=="right":
  print("You fell into a hole. Game Over.")
else:
  print("You chose a door that doesn't exist. Game Over.")