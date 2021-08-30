import random 

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == "s":
       if you == "w":
           return False
       elif you == "g":
           return True

    elif comp == "w":
       if you == "g":
           return False
       elif you == "s":
           return True
           
    elif comp == "g":
       if you == "s":
           return False
       elif you == "w":
           return True      

print("Computer Chosed Among Snake(s) Water(w) gun(g) ? ")
randno = random.randint(1, 3)
if randno == 1:
    comp = "s" 
elif randno == 2:
     comp = "w"  
elif randno == 3:
    comp = "g"


you = input("Your Turn: Snake(s) Water(w) gun(g) ? :  ")
a = gamewin(comp, you)
print(f"Computer Chosed: {comp}")
print(f"You Choose: {you}")


if (you != "w" and you != "s" and you != "g"):
    print("********************Invalid Input***************************")
elif(print("Input Checked Right............")):
    print("")
else:
    if a == None:
        print("The Game Is a Tie ")
    elif a == True:
        print("You Won The Game")      
    else:
        print("You Lost The Game")
            






    
      

