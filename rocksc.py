import random

user_win=0
computer_win=0
options= ["rock","paper","scissors"] 

while True:
    user_input=input("type Rock/paper/Scissor or Q to quit:").lower()
    if user_input =="q":
       break
    
    if user_input not in options:
        continue 
    
    random_No=random.randint(0,5)
    # thts is indexed placement to the list given above 
    computer_pick=options[random_No]
    print("Computer Picked ", computer_pick+".")
    if user_input == "rock" and computer_pick=="scissors":
        user_win+=1
        print("You won")
      
    elif user_input=="paper" and computer_pick=="rock":
        user_win+=1
        print("you won !")
    
    elif user_input=="scissors" and computer_pick=="paper":
        user_win+=1
        print("you win!")
   
    else:
     computer_win+=1
     print("computers win ")
    if user_input=="rock" and computer_pick=="rock":
        break
print("see you soon ") 
if computer_win > user_win:  
 print("computer wins",computer_win,"times")
else:
 print("you win ",user_win,"times") 
        
    