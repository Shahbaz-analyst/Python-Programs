# Rock-Paper-Scissor game

import random

def check(comp, user):
    if(comp == user):
        return 0
    
    elif(comp == 0 and user ==1):
        return 1
    
    elif(comp == 1 and user == 2):
        return 1
    
    elif(comp == 2 and comp == 0):
        return 1
    
    else :
        return -1
    
    
comp = random.randint(0, 2)
user = int(input("0 for Rock, 1 for Paper and 2 for Scissors: "))

score = check(comp , user)

print("You: ", user)
print("Comp: ", comp)

if(score == 0):
    print("Its a Draw")

elif(score == 1):
    print("You won")
    
else:
    print("You loose")