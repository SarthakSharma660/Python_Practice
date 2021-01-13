import os
more_members="yes"
while more_members=="yes":
  name=input("What is your name?\n")
  bid=int(input("What is your bid?: $"))
 
  auction_dic={}
 
  def auction(bider_name,bid):
    auction_dic[bider_name]=bid
 
  auction(bider_name=name,bid=bid)
 
  winner=0
  winner_name=""
 
  for key in auction_dic:
    if auction_dic[key]>winner:
      winner=auction_dic[key]
      winner_name=key

  more_members=input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
  os.system("clear")
  if more_members=="no":
    print(f"The winner is {winner_name} with a bid of ${winner}")
  