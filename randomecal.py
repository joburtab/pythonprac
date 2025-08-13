import random
import time

opratores=["+","-","*" ,"/"]
min_operand=1
max_oprerand=12
Total_Problem=10
score=0

def generate_solution():
    left=random.randint(min_operand,max_oprerand)
    right=random.randint(min_operand,max_oprerand)
    opration=random.choice(opratores)
    
    expreesion=str(left) + " " + opration +"  "+str(right)
    answer=eval(expreesion)
    return expreesion, answer

wrong=0
input("prsse any thing to start ")
print("----------------------------------------")
start_time=time.time()

for i in range (Total_Problem):
    expreesion,answer=generate_solution()
    gusse=input("The problem no # " + str(i+1) + ": " + expreesion  + "=")
    if gusse != str(answer):
        print("you answer is not correct please try again ")
    else :
        score+=1
        print("you got it let go to other ")
        
        
end_time=time.time() 
total_time=(end_time-start_time,2 )      
print("you have got ",score,"and in :",total_time,"Time from this rnadom question ")       
print("----------------------------------------")


