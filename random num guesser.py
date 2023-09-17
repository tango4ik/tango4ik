#modules
import os
import time
import random
#vars
tries = 2
rand = int(random.randrange(1,10))
num = int(input("1 to 10 number "))
#main code
for i in range(3):
    print("tries left are",tries)
    if rand == num:
        os.system('cls')
        print("correct!")
    if num != rand and tries != 0:
        tries = tries - 1
        num = int(input("1 to 10 number "))
    if tries == 0:
        os.system('cls')
        print("the correct number was",rand)
time.sleep(1)
