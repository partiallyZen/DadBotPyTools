import random

x = int(input("How many dice do you wish to roll?"))
y = int(input("How many sides?"))
for i in range(x):
  print(random.randint(1,y))