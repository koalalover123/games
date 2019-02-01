import random
import time

answer= random.randint(1,100)

time1=time.time()

choice= input("Guess a number 1-100")

while True:
    choice= int(input(''))
    if choice < answer:
        print ("TOO LOW")
    elif choice > answer:
        print ("TOO HIGH")
    elif choice == answer:
        break

print ("YOU GOT IT!!!")

time2= time.time()

totalTime= str(int(time2-time1))

print ("IT TOOK YOU " + totalTime + "  SECONDS. ")
       
