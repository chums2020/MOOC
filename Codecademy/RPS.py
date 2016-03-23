#Codecademy Python project
#Ask users to select either Rock, Paper, Scissors
#Compare the user's choice and the computer's choice
#Decide the winner

from time import sleep
from random import randint

options =["R", "P", "S"]
MESSAGE_LOST = "You lost!"
MESSAGE_WIN = "You win!"

def decide_winner(user_choice, computer_choice):
  print "User selectin %s" % user_choice
  print "Computer selecting..."
  sleep(1)
  print "%s" % computer_choice
  user_choice_index =options.index(user_choice)
  computer_choice_index =options.index(computer_choice)
  if user_choice == computer_choice:
    print "It's a tie."
  elif user_choice == "R" and computer_choice=="S":
    print MESSAGE_WIN
  elif user_choice == "P" and computer_choice=="R":
    print MESSAGE_WIN
  elif user_choice == "S" and computer_choice=="P":
    print MESSAGE_WIN
  elif user_choice_index >2:
    print "invalid option"
  else: 
    print MESSAGE_LOST
  return

def play_RPS():
  print "Rock, Paper, Scissors"
  user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors:")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0,len(options)-1)]
  decide_winner(user_choice, computer_choice)

play_RPS()

  
  
  
