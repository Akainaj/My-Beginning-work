import string
import random

s1 = string.ascii_uppercase
s2 = string.ascii_lowercase
s3 = string.punctuation
s4 = string.digits

while True:
   plen = input("Enter The Number Of Password Letters: \n")

   try:
      plen = int(plen)
      break
   except ValueError :
      print("Invalid Input! Please Try Again....")
      continue   

s = [] 
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

random.shuffle(s)

print("Your Password With Security Is: ")

print("".join(s[0:plen]))

