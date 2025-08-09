name=input("Enter your name")
print("Welcome", name)
options=["ortohodox","protestant","Muslim","pagan","hindu","joba","etist"]

answer=input("are religios or random person ? type religious or normal").lower()
if answer=="religious":
    answer=input("what religion ? write your religion").lower()
    if answer==options.index([0]):
        answer=input("you are chrstian then let me ask you somthing? okay  or no ").lower()
        if answer=="yes":
            q1=input("what is the name of your God").lower()
            if q1=="Egziabher ":
                print("Gobez kalehywet Ysemaln")
            else:
                print("you should learn halewote egziabher ")
                quit()
    
            
    if answer==options[2]:
        print("now you are pente okay what is sorry i dont have question ")
        quit()
        
    if answer==options[3]:
       print("now you are pente okay what is sorry i dont have question ")
       quit()
    if answer==options[4]:
        print("now you are pente okay what is sorry i dont have question ")
        quit()