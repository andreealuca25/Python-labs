"""Write a script to simulate loto 6/49 draw (numbers extraction). The output should be a list of six numbers between
1 and 49 representing the winning combination. """
import random
import time

print("The winning combination is: ")
for number in range(0,6):
    time.sleep(1)
    print(random.randint(1,49))