from art_High_Low import logo,vs
from game_data import data
import random
import os
score=0
game_over=True
a_dic={
    'name': "sarthak",
    'follower_count': 0,
    'description': 'xyxy ',
    'country': 'India '
    }
b_dic={
    'name': "sarthak",
    'follower_count': 0,
    'description': 'xyxy ',
    'country': 'India '
    }    

def randomvalue():
    index=random.randint(0,len(data)-1)
    dic={
        'name': "sarthak",
        'follower_count': 0,
        'description': 'xyxy ',
        'country': 'India '
        }
    dic=data[index]
    return dic
def winner(Input):
    global a_dic,b_dic
    global score
    if (a_dic['follower_count']>b_dic['follower_count'] and Input=="a") or(a_dic['follower_count']<b_dic['follower_count'] and Input=="b") :
        os.system("clear")
        score=score+1
        a_dic=b_dic
        print(f"You're right! Current score: {score}.")
        return score
    else:
        os.system("clear")
        print(f"Sorry, that's wrong. Final score: {score}")
        score=0
        return score
a_dic=randomvalue()
while game_over:
    print(logo)
    print(f"Compare A:{a_dic['name']},{a_dic['description']},from {a_dic['country']}.")
    print(vs)
    b_dic=randomvalue()
    print(f"Compare B:{b_dic['name']},{b_dic['description']},from {b_dic['country']}.")
    user_input=input("Who has more followers? Type 'A' or 'B': ").lower()
    score=winner(user_input)
    if score==0:
        game_over=False



