import time
import random


def nextGame():
    replay = 1
    while replay == 1:
        next_game = input("Play again? (yes or y/no or n): ")
        if next_game == "no" or next_game == "n":
            replay = 0
            exit()
        if next_game == "yes" or next_game == "y":
            action()


def initialPrint():
    print("Long ago, there was a pirate king who had a lot of gold and wealth")
    time.sleep(2)
    print("After living a fulfilled life, the king died")
    time.sleep(2)
    print('His last words were ')
    time.sleep(2)
    print('"I have kept all my gold somewhere in the ocean"')
    time.sleep(2)
    print('"I have left clues around"')
    time.sleep(2)
    print('"Whoever finds it will be the new pirate king"')
    time.sleep(2)
    print("New pirate groups started forming in search of the gold")
    time.sleep(2)
    print("Will you like to search for the gold too?")


def secondPrint():
    print("You have decided to join the game.")
    time.sleep(2)
    print(' Your first stop is to get money for a boat')
    time.sleep(2)
    print("You enter a casino, and decided to play a bet")
    time.sleep(2)
    print("Rule of the game:")
    time.sleep(2)
    print("Total dice x $1000")


def rollDice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    diceTotal = dice1+dice2
    print('Your first dice is ')
    time.sleep(2)
    print(dice1)
    time.sleep(2)
    print('Your second dice is ')
    time.sleep(2)
    print(dice2)
    time.sleep(2)
    print('Total is ... ')
    time.sleep(2)
    print(dice1+dice2)
    return diceTotal


def compareDays(totalDays):
    if totalDays < 9:
        print('Another player got the gold before you')
        time.sleep(2)
        print('Game Over!!!')
        time.sleep(2)
        return 1
    else:
        print('You got the gold before any other player')
        time.sleep(2)
        print('You win!!!')
        return 1


def questionChoice():
    questionNumber1 = random.randint(1, 100)
    questionNumber2 = random.randint(1, 100)
    print('Answer this question')
    time.sleep(2)
    print(str(questionNumber1) + ' + ' +
          str(questionNumber2) + ' x ' + str(questionNumber1))
    response = input('Answer?')
    correct = (questionNumber1 + (questionNumber2*questionNumber1))
    if int(response) == correct:

        print('Right Answer.')
        time.sleep(2)
        print('You have sent bandits to delay other players for 12 days')
        score = 12
    else:
        print('Wrong answer, correct answer is')
        time.sleep(2)
        print(correct)
        score = 0
        compareDays(score)


def mixedChoice():
    print('You met a genie, he asks you to roll.')
    time.sleep(2)
    print('The average will determine to some extent')
    print('how long the opponent\'s journey will take')
    time.sleep(2)
    halfDays = rollDice()/2
    print('Half is '+str(halfDays))

    questionNumber1 = random.randint(1, 100)
    questionNumber2 = random.randint(1, 100)
    print('You have been stopped by bandits.')
    time.sleep(2)
    print('They help you if you answer their question right')
    time.sleep(2)
    print('Or they delay you')
    time.sleep(2)
    print('Answer this question')
    time.sleep(2)
    print(str(questionNumber1) + ' + ' +
          str(questionNumber2) + ' x ' + str(questionNumber1))
    response = input('Answer?')
    correct = (questionNumber1 + (questionNumber2*questionNumber1))
    if int(response) == correct:

        print('Right Answer. You have delayed other players for 6 days')
        score = 6
    else:
        print('Wrong answer, correct answer is')
        time.sleep(2)
        print(correct)
        time.sleep(2)
        print('The bandits delay you for days')
        score = 0
    mixedtotalDays = halfDays+score
    compareDays(mixedtotalDays)


def randomChoice():
    print('While sailing, you met a genie')
    time.sleep(2)
    print('He forces you to roll')
    time.sleep(2)
    print('The output will be the number of days to your destination')
    totalDays = rollDice()
    time.sleep(2)
    print('You rolled '+str(totalDays))
    time.sleep(2)
    print('Your opponent spends '+str(totalDays)+' to reach their destination')
    return compareDays(totalDays)


def handleBoatOption(boatGotten):
    if boatGotten == 1:
        return randomChoice()
    elif boatGotten == 2:
        return mixedChoice()
    else:
        return questionChoice()


def boatStory(amount):
    print('Boat Options:')
    time.sleep(2)
    print('1: Basic Canoe - Random Chance')
    print('2: Standard Boat - Random Chance + question')
    print('3: Luxurious Fast Ship - Question')
    # time.sleep(2)
    if amount < 4:
        boatGotten = 1
        print('You have gotten Basic Canoe')
    elif amount < 8:
        boatGotten = 2
        print('You have gotten Standard Boat')
    else:
        boatGotten = 3
        print('You have gotten Luxurious Fast Ship')
    return handleBoatOption(boatGotten)


def continueMission1():
    newState = 0
    while newState == 0:
        print("Throw the dice?")
        dieChoice = input("y/n?")
        if dieChoice == 'no' or dieChoice == 'n':
            newState = 1
            print("You didn't get enough to buy a boat. Someone else won")
            time.sleep(2)
            print("GAME OVER!!!")
            exit()
        if dieChoice == 'yes' or dieChoice == 'y':
            newState = 1
            amount = rollDice()
            print('You get $')
            # time.sleep(2)
            print(amount*1000)
            return boatStory(amount)
        else:
            print('Incorrect selection')
            dieChoice = input("y/n?")


def action():
    initialPrint()
    choice = input("y/n? ")
    state = 0
    while state == 0:
        if choice == 'no' or choice == 'n':
            state = 1
            print("You've decided not to join the adventure")
            print("GAME OVER!!!")
            exit()
        if choice == 'yes' or choice == 'y':
            state = 1
            secondPrint()
            return continueMission1()
        else:
            print('Incorrect selection')
            choice = input("y/n? ")
