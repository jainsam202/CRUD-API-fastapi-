import random
import math

lower = int(input("Enter lower bound - "))
upper = int(input("Enter upper bound - "))

x = random.randint(lower, upper)
print("\nYou have only",round(math.log(upper - lower + 1, 2)),"chances to get the integer")

count=0
while count<math.log(upper - lower + 1,2):
  count+=1
  guess = int(input("Guess the number - "))
 
  if x == guess:
    print("Congrats you did it in ",count," try")
    break
  elif x > guess:
    print("You guess too small")
  elif x < guess:
    print("Yoy guess too high")

if count >=math.log(upper-lower + 1, 2):
  print("The number id %d" % x)
else:
  print("\n Better luck next time!")