import random
def easy_game(value,turn):
  user_value=int(input("Guess a Number : "))
  if(value==user_value):
    print(f"The number was {value}")
    print("You Won")
    return
  elif (value>user_value):
    print("Guess Higher")
    turn-=1
  else:
    print("Guess Lower")
    turn-=1
  print(f"You have {turn} attempts remaining to guess the number")
  if(turn>0):
    easy_game(value,turn)

def hard_game(value,turn):
  user_value=int(input("Guess a Number : "))
  if(value==user_value):
    print(f"The number was {value}")
    print("You Won")
    return
  elif (value>user_value):
    print("Guess Higher")
    turn-=1
  else:
    print("Guess Lower")
    turn-=1
  print(f"You have {turn} attempts remaining to guess the number")
  if(turn>0):
    easy_game(value,turn)


def play():
  print("Welcome to Number Guessing Game!")
  print("I'm thinking of number between 1 and 100")
  difficulty=input("Choose a difficulty ? Type easy or hard : ")
  comp_value=random.randint(1,100)
  if(difficulty=="easy"):
    easy_game(comp_value,10)
  else:
    hard_game(comp_value,5)

choice=input("Do you want to play (y/n) : ");
while(choice=="y"):
  play()
  choice=input("Want to play again (y/n) : ");
print("GoodBye") 


  