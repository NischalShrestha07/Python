import random

choices=["rock","paper","scissors"]
computer=random.choice(choices)
player=None


while player not in choices:
    player=input("rock,paper,scisoors?:").lower()
    if player==computer:
        print("Computer:",computer)
        print("Player:",player)
        print("Tie!")
    elif player == "rock":
        if computer =="paper":
            print("Computer:",computer)    
            print("Player:",player)    
            print("You Lose!")
        if computer =="scissors":
            print("Computer:",computer) 
            print("Player:",player) 
            print("You Win!!")
            
    elif player == "paper":
        if computer =="rock":
            print("Computer:",computer)    
            print("Player:",player)    
            print("You win!!")
        if computer =="scissors":
            print("Computer:",computer) 
            print("Player:",player) 
            print("You Lose!!")
            
    elif player == "scissors":
        if computer =="rock":
            print("Computer:",computer)    
            print("Player:",player)    
            print("You Lose!")
        if computer =="paper":
            print("Computer:",computer) 
            print("Player:",player) 
            print("You Win!!")
    
