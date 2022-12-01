import time

print("Long ago, there was a pirate king who had a lot of gold and wealth")
time.sleep(2)
print("After living a fulfilled life, the king died")
time.sleep(2)
print('His last words were "I have kept all my gold somewhere in the ocean and left clues around. Whoever finds it will be the new pirate king \"')
time.sleep(2)
print("New pirate groups started forming in search of the gold")
time.sleep(2)
print("Will you like to search for the gold too?")


choice = input("Y/N? ")
state = 0;
while state==0:
    choice = input("Y/N? ")
    if choice == "no" or choice == "n":
        state=1
        print("You've decided not to join the adventure")
        print("GAME OVER!!!")
    elif choice == "yes" or choice == "y":
        state=1
        print("You have decided to join the game. Your first stop is to get money for a boat")
        print("You enter a casino, and decided to play a bet")
        print("Rule of the game:")
        print("Total dice x $1000")
        newState = 0
        while newState == 0:
              print("Throw the dice?")
              dieChoice=input("Y/N?")
              if choice == "no" or choice == "n":   
                 newState=1
                 print("You could not get a money for a boat before a group found the gold")
                 print("GAME OVER!!!")          
              elif choice == "yes" or choice == "y":
                 newState=1    
                 print("You have rolled")
              else:
                 print("Incorrect input, try again")



print("Hello World")
