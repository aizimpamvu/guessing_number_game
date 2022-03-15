from random import randint
from art import logo

#Number Guessing Game Objectives:
EASY_LEVEL=10
HARD_LEVEL=5
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
def check_answer(guess,answer,turns):
  if guess>answer:
    print("Too High!!")
    return turns-1
  elif guess<answer:
    print("Too low")
    return turns-1
  else:
    print(f"You have got it! the answer wa {answer}")

# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
    
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def set_difficulty():
  level=input("Choose a difficulty. Type 'easy' or 'hard':").lower()
  if level=="hard":
    return HARD_LEVEL
  elif level=="easy":
    return EASY_LEVEL
  else:
    print("Wrong choice select the correct Choice")
    return set_difficulty()

# Playing game function
def game():
  #Choosing a random number between 1 and 100.
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer=randint(1,100)
  print(f"The number I am thinking is {answer} ")
  turns=set_difficulty()
  guess=0
  while guess!=answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    # Let the user gues a number
    guess=int(input("Enter a number:"))
    turns=check_answer(guess, answer, turns)
    if turns==0:
      print("You've run out of guesses, you lose.")
      return
    elif guess!=answer:
      print("Guess again!")
game()