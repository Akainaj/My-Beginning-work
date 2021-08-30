import os

def findit(filename):
    with open(filename, "r") as f:
        content = f.read()

    if "harry" in content.lower():
        return True
    else:
        return False

dir_cont = os.listdir()
b = 0

for items in dir_cont:
    if items.endswith(".txt"):
        print(f"Detecting Harry In {items} \n")
        a = findit(items) 

        if a is True :
          print(f" -Harry Found In {items} !!!! \n")
          b += 1

        else:
          print(f" -Harry Not Found In {items} \n")

print("********** Harry Detector Summary ********** \n")  

print(f"  {b} Files Found With Harry Hidden In Items!")

    
