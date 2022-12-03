import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


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
    print_pause(
        "Long ago, there was a pirate king who had a lot of gold and wealth")

    print_pause("After living a fulfilled life, the king died")

    print_pause('His last words were ')

    print_pause('"I have kept all my gold somewhere in the ocean"')

    print_pause('"I have left clues around"')

    print_pause('"Whoever finds it will be the new pirate king"')

    print_pause("New pirate groups started forming in search of the gold")

    print_pause("Will you like to search for the gold too?")


def secondPrint():
    print_pause("You have decided to join the game.")

    print_pause(' Your first stop is to get money for a boat')

    print_pause("You enter a casino, and decided to play a bet")

    print_pause("Rule of the game:")

    print_pause("Total dice x $1000")


def rollDice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    diceTotal = dice1+dice2
    print_pause('Your first dice is ')

    print_pause(dice1)

    print_pause('Your second dice is ')

    print_pause(dice2)

    print_pause('Total is ... ')

    print(dice1+dice2)
    return diceTotal


def compareDays(totalDays):
    if totalDays < 9:
        print_pause('Another player got the gold before you')

        print_pause('Game Over!!!')

        return 1
    else:
        print_pause('You got the gold before any other player')

        print('You win!!!')
        return 1


def questionChoice():
    questionNumber1 = random.randint(1, 100)
    questionNumber2 = random.randint(1, 100)
    print_pause('Answer this question')

    print(str(questionNumber1) + ' + ' +
          str(questionNumber2) + ' x ' + str(questionNumber1))
    response = input('Answer?')
    correct = (questionNumber1 + (questionNumber2*questionNumber1))
    if int(response) == correct:

        print_pause('Right Answer.')

        print_pause('You have sent bandits to delay other players for 12 days')
        print('YOU WIN!!!')
        score = 12
    else:
        print_pause('Wrong answer, correct answer is')

        print(correct)
        score = 0
        compareDays(score)


def mixedChoice():
    print_pause('You met a genie, he asks you to roll.')

    print_pause('The average will determine to some extent')
    print_pause('how long the opponent\'s journey will take')

    halfDays = rollDice()/2
    print_pause('Half is '+str(halfDays))

    questionNumber1 = random.randint(1, 100)
    questionNumber2 = random.randint(1, 100)
    print_pause('You have been stopped by bandits.')

    print_pause('They help you if you answer their question right')

    print_pause('Or they delay you')

    print_pause('Answer this question')

    print_pause(str(questionNumber1) + ' + ' +
                str(questionNumber2) + ' x ' + str(questionNumber1))
    response = input('Answer?')
    correct = (questionNumber1 + (questionNumber2*questionNumber1))
    if int(response) == correct:

        print_pause('Right Answer. You have delayed other players for 6 days')
        score = 6
    else:
        print_pause('Wrong answer, correct answer is')

        print_pause(correct)

        print_pause('The bandits delay you for days')
        score = 0
    mixedtotalDays = halfDays+score
    compareDays(mixedtotalDays)


def randomChoice():
    print_pause('While sailing, you met a genie')

    print_pause('He forces you to roll')

    print_pause('The output will be the number of days to your destination')
    totalDays = rollDice()

    print_pause('You rolled '+str(totalDays))

    print_pause('Your opponent spends '+str(totalDays) +
                ' to reach their destination')
    return compareDays(totalDays)


def handleBoatOption(boatGotten):
    if boatGotten == 1:
        return randomChoice()
    elif boatGotten == 2:
        return mixedChoice()
    else:
        return questionChoice()


def boatStory(amount):
    print_pause('Boat Options:')

    print('1: Basic Canoe - Random Chance')
    print('2: Standard Boat - Random Chance + question')
    print('3: Luxurious Fast Ship - Question')
    #
    if amount < 4:
        boatGotten = 1
        print_pause('You have gotten Basic Canoe')
    elif amount < 8:
        boatGotten = 2
        print_pause('You have gotten Standard Boat')
    else:
        boatGotten = 3
        print_pause('You have gotten Luxurious Fast Ship')
    return handleBoatOption(boatGotten)


def continueMission1():
    print("Throw the dice?")
    dieChoice = input("y/n?")
    while dieChoice not in ['yes', 'y', 'no', 'n']:
        dieChoice = input("y/n?")

    if dieChoice == 'no' or dieChoice == 'n':
        print_pause(
            "You didn't get enough to buy a boat. Someone else won")

        print("GAME OVER!!!")
        exit()
    elif dieChoice == 'yes' or dieChoice == 'y':
        amount = rollDice()
        print_pause('You get $')
        #
        print_pause(amount*1000)
        return boatStory(amount)


def action():
    initialPrint()
    choice = input("y/n? ")
    state = 0
    while state == 0:
        if choice == 'no' or choice == 'n':
            state = 1
            print_pause("You've decided not to join the adventure")
            print("GAME OVER!!!")
            exit()
        if choice == 'yes' or choice == 'y':
            state = 1
            secondPrint()
            return continueMission1()
        else:
            print('Incorrect selection')
            choice = input("y/n? ")
