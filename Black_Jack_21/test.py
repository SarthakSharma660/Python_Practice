import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_score=0
user_deck=list()
deck=list()
dealer_deck=list()
def score_calc(deck,score):
    user_number=random.randint(0,len(cards)-1)
    deck.append(cards[user_number])
    score=sum(deck)
    return deck,score

score_calc(deck=user_deck,score=user_score)
user_deck,user_score=score_calc(user_deck,user_score)
user_deck,user_score=score_calc(user_deck,user_score)
# print(score_calc(user_deck,user_score))
print(user_score)
print(user_deck)
