import random

randno = random.randint(1, 100)
print(randno)
userguess = None
Guesses = 0

while(userguess != randno):
    Guesses += 1  
    try:
        userguess = int(input("Enter The Number: "))
        if(userguess == randno):
          print("Conrats ! You Guessed It Right")
        else:
           if(userguess > randno):
             print("Sorry! Enter A Smaller Number: ")
           else:
            print("Sorry! Enter A Larger Number: ")  
    except:
      print("Invalid Input Found! Try Again")

print("****************************************************************")

print(f"You Guessed The Number In {Guesses} Guesses! ")    

with open("highscore1.txt", "r") as f:
    score = int(f.read())

if(Guesses < score):
    print("*****************************************************")
    print("Congratulations! You Broke The HighScore")
    with open("highscore1.txt", "w") as f:
     f.write(str(Guesses))

