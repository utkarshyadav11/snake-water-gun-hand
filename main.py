import random


def MyGame(comp, me):
   
    if comp == me:
        return None
      
    elif comp == 's':
        if me=='w':
            return False
        elif me=='g':
            return True
        elif me =="h":
            return False
    
    
    elif comp == 'w':
        if me=='g':
            return False
        elif me=='s':
            return True
        elif me =="h":
            return True
    
    
    elif comp == 'g':
        if me=='s':
            return False
        elif me=='w':
            return True
        elif me =="h":
            return False
        
    elif comp == "h":
       if me == "g":
           return True
       elif me =="w":
           return False
       elif me == "s":
           return True
    

print("Comp Turn: Snake(s) Water(w) hand(h) Gun(g)?")
randNo = random.randint(1, 4) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = '''w'''
elif randNo == 3:
    comp = 'g'
elif randNo == 4:
    comp ="h"

me = input("Your Turn: Snake(s) Water(w) hand(h) Gun(g)?")
a = MyGame(comp,me)

print(f"Computer chose {comp}")
print(f"You chose {me}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")