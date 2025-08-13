import random 

def  roll():
    min_val=1
    max_value=6
    roll=random.randint(min_val,max_value)
    
    return roll
while True:
    players=int(input("Enter the number of players 2-5 : "))
    if players.is_integer():
        players=int(players)
        if  2 <= players <=5:
             break
        else:
            print("must be bettwen the give number ")
    else:
        print("invalid iput")
        
max_score= 60
players_score =[ 0 for _ in range(players)]

while max(players_score) < max_score:
     for player_idx in range (players):
         print("\n player number ",player_idx +1,"turnin has just started !")
         print("your total score is :",players_score[player_idx],"\n")
         current_score=0
         
         while True:
            should_roll = input("World you like to  stop rolling (y)?")
            if should_roll.lower() == "y":
                break        
            vlaue= roll()
            if vlaue == 1:
               print("you rolled a 1! turn Done!")
               current_score=0
               break
            else:
                current_score += vlaue
                print("you rolled a:",vlaue)
            print("Your score is:",current_score)
         players_score[player_idx] += current_score     
         print("your totla score is :",players_score[player_idx])
     
max_score=max(players_score)
winning_idx=players_score.index(max_score)
print("player number ",winning_idx + 1,"is the winner with a score of:",max_score)
