import random
from art import logo,vs
from game_data import data
print(logo)
def start(choose):
  account_name=choose["name"]
  account_description=choose["description"]
  account_country=choose["country"]
  return f"{account_name},{account_description},{account_country}"

score=0
game_is_over=False
second=random.choice(data)
while not game_is_over:

  first=second
  second=random.choice(data)
  if first==second:
    second=random.choice(data)

  print(f"compare A : {start(first)}")
  print (vs)
  print(f"Againt B : {start(second)}")

  guess=input("who has more followers . Type A or B :").upper()
  account_followers_A=first["follower_count"]
  account_followers_B=second["follower_count"]

  def checking(guess,account_followers_A,account_followers_B):
    if guess =="A" and account_followers_A>account_followers_B  :
      return True
    elif guess =="A" and account_followers_A<account_followers_B :
      return False
    elif guess =="B" and account_followers_B>account_followers_A :
      return True
    elif guess =="B" and account_followers_B<account_followers_A :
      return False
  is_correct=checking(guess,account_followers_A,account_followers_B)
  
  if is_correct:
    score+=1
    print(f"your right! : current score is {score}")
  else:
    game_is_over=True
    print(f"sorry , you are wrong : final score is {score}")