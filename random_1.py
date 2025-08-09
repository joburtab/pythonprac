import random

toop_rage = int(input("Enter number "))
random_number =random.randint(0,toop_rage)
if toop_rage<=0:
        print('pl,ease type a number larger than 0 next time ')
        quit()
else:
       print('plaese inter digit okay')
       quit()
guesses=0
while True:
    guesses+=1
    user_G=input("make any Guess : ")
    if user_G ==random_number :
        print("you are correct ")
        break
    if user_G.isdigit():
        user_G= int(user_G)
    else:
        print("please type number")
        continue
top_range=int(random_number)
if top_range <=0:
    print('please type a number larger than 0 next time')

elif user_G > random_number:
     print("you were above the number ")
else:
    print('you were below the number ')
    

print("you got it in ",guesses,"to random guesses")



