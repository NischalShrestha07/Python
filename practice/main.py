
import random


def get_choices():
   player_choice=input("enter a choice(rock,paper,scissors)")
   options=['rock','paper','scissors']
   # computer_choice="paper"
   computer_choice=random.choice(options)
   choices={"player":player_choice,"Computer":computer_choice}
   return choices


choices=get_choices()   
print(choices)

def checkWin(player,computer):
      #  print("You choose "+player+" Computer Choose: "+computer)
      print(f"You choose {player}, Computer Choose {computer}")

      if player==computer:
              return "Its a tie!"
      elif player=="rock":
         if computer == "scissors":
          return "Rock Smashes scissors! You Win"     
      else:       
         return "Paper Covers Rock! You Lose"     

      # elif player=="scissors":
      # if computer == "paper":
      #     return "Scissors cuts paper! You Win"     
      #  else:       
      #      return "Rock smashes scissors! You Lose"     
      # elif player=="scissors":
      # if computer == "paper":
      #     return "Scissors cuts paper! You Win"     
      # else:       
      #    return "Rock smashes scissors! You Lose"     


        
   


