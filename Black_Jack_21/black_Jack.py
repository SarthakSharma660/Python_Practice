import random
from art import logo
import os
import time
def Black_jack():
     start_game=input("Do you want to play a game of Blackjack? Type 'yes' or 'no'").lower()
     user_score=0
     dealer_score=0
     user_deck=list()
     dealer_deck=list()
     counter=1
     while start_game=="yes":
          print(logo)   
          while start_game=="yes":
               cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
               def score_calc(deck,score):
                    user_number=random.randint(0,len(cards)-1)
                    deck.append(cards[user_number])
                    score=sum(deck)
                    if 11 in deck and score>12:
                         deck.remove(11)
                         deck.append(1)
                         score=sum(deck)
                    return deck,score
               if counter==1:
                    for _ in range(0,2):
                         user_deck,user_score=score_calc(deck=user_deck,score=user_score)
                         dealer_deck,dealer_score=score_calc(deck=dealer_deck,score=dealer_score)
               else:
                    user_deck,user_score=score_calc(deck=user_deck,score=user_score)
                    dealer_deck,dealer_score=score_calc(deck=dealer_deck,score=dealer_score)
               print(f"dealer deck :{dealer_deck[0]}")
               print(f"user deck {user_deck} and score :{user_score}")
               counter=2
               if user_score<21 and dealer_score<21:
                    start_game=input("Do you want to play a game of Blackjack? Type 'yes' or 'no'").lower()
                    if start_game=="no":
                         if dealer_score<15:
                              dealer_deck,dealer_score=score_calc(deck=dealer_deck,score=dealer_score)
                              if dealer_score<user_score or dealer_score>21:
                                   print(f"user deck {user_deck} and score :{user_score}")
                                   print(f"dealer deck {dealer_deck} and score :{dealer_score}")                                   
                                   print("You win")
                                   start_game="no"
                                   time.sleep(5)
                                   os.system("clear")
                                   Black_jack()
                              else :
                                   print(f"user deck {user_deck} and score :{user_score}")
                                   print(f"dealer deck {dealer_deck} and score :{dealer_score}")
                                   print("you lose")
                                   start_game="no"
                                   time.sleep(5)
                                   os.system("clear")
                                   Black_jack()
                         else:
                              if dealer_score<user_score:
                                   print(f"user deck {user_deck} and score :{user_score}")
                                   print(f"dealer deck {dealer_deck} and score :{dealer_score}")
                                   print("You win")
                                   start_game="no"
                                   time.sleep(5)
                                   os.system("clear")
                                   Black_jack()
                              else :
                                   print(f"user deck {user_deck} and score :{user_score}")
                                   print(f"dealer deck {dealer_deck} and score :{dealer_score}")
                                   start_game="no"
                                   print("you lose")
                                   time.sleep(5)
                                   os.system("clear")
                                   Black_jack()
               elif (dealer_score>21 and user_score>21) or(dealer_score==user_score) :
                    print(f"user deck{user_deck}and score :{user_score}")
                    print(f"dealer deck{dealer_deck}and score :{dealer_score}")
                    print("Draw")
                    start_game="no"
                    time.sleep(5)
                    os.system("clear")
                    Black_jack()               
               elif user_score==21 :
                    print(f"user deck {user_deck} and score :{user_score}")
                    print(f"dealer deck {dealer_deck} and score :{dealer_score}")
                    print("You Win")
                    start_game="no"
                    time.sleep(5)
                    os.system("clear")
                    Black_jack()
               elif dealer_score<21 :
                    print(f"user deck {user_deck} and score :{user_score}")
                    print(f"dealer deck {dealer_deck} and score :{dealer_score}")
                    print("You Lose")
                    start_game="no"
                    time.sleep(5)
                    os.system("clear")
                    Black_jack()
               
               elif dealer_score>21 :
                    print(f"user deck {user_deck} and score :{user_score}")
                    print(f"dealer deck {dealer_deck} and score :{dealer_score}")
                    print("You win")
                    start_game="no"
                    time.sleep(5)
                    os.system("clear")
                    Black_jack()

               elif dealer_score==21 or user_score>21:
                    print(f"user deck{user_deck}and score :{user_score}")
                    print(f"dealer deck{dealer_deck}and score :{dealer_score}")
                    print("You lose")
                    start_game="no"
                    time.sleep(5)
                    os.system("clear")
                    Black_jack()

Black_jack()
     

     