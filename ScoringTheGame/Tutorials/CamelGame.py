import random

def instructions():
    print 'Welcome to Camel!'
    print 'You have stolen a camel to make your way across the great Mobi desert.'
    print 'The natives want their camel back and are chasing you down! Survive your'
    print 'desert trek and out run the natives.'
    Camel()

def Camel():
    milesTraveled = 0
    thirst = 0
    camelTiredness = 0
    nativeDistance = 20
    drinksLeft = 3
    done = False
    oasisNumber = random.randint(0,19)

    while done == False:
        print 'A: Drink from your canteen.'
        print 'B: Ahead moderate speed.'
        print 'C: Ahead full speed.'
        print 'D: Stop for the night.'
        print 'E: Status check.'
        print 'Q: Quit.'
        print ' '
        choice = raw_input('Select an option: A, B, C, D, E, or Q:  ')
        choice = choice.upper()
        print ' '
        MaybeOasis = random.randint(0,19)
        if MaybeOasis == oasisNumber:
            print 'You have found an Oasis. Your water has been refilled'
            print ' '
            drinksLeft = 3
            thirst = 0
            camelTiredness = 0

        if choice == 'A':
            if drinksLeft > 0:
                drinksLeft = drinksLeft - 1
                thirst = 0
                print 'Drinks left in your canteen: ', drinksLeft
                print ' '
            else:
                print 'None left.. Try something else'
                print ' '
        elif choice == 'B':
            distanceB = random.randint(5,12)
            milesTraveled = milesTraveled + distanceB
            camelTiredness = camelTiredness + 1
            thirst = thirst + 1
            nativeDistance = nativeDistance - random.randint(7,14) + distanceB
            print 'you traveled ', distanceB, ' miles'
            print ' '
        elif choice == 'C':
            distanceC = random.randint(10,20)
            camelTiredness = camelTiredness + random.randint(1,3)
            milesTraveled = milesTraveled + distanceC
            thirst = thirst + 1
            nativeDistance = nativeDistance - random.randint(7,14) + distanceC
            print 'you traveled ', distanceC, ' miles'
            print ' '

        elif choice == 'D':
            camelTiredness = 0
            nativeDistance = nativeDistance - random.randint(7,14)
            print 'The camel is happy and energized'
            print ' '
        elif choice == 'E':
            print 'Miles traveled: ', milesTraveled
            print 'Drinks left in canteen: ', drinksLeft
            print 'The natives are ', nativeDistance, ' miles behind you.'
            print ' '
        elif choice == 'Q':
            done = True
        elif choice not in ['A','B','C','D','E','Q']:
            "Next time, please choose one of the options."
            print ' '

        if camelTiredness > 5 and camelTiredness <= 8:
            print 'Your camel is tired. If you do not rest him soon, he will die.'
            print ' '
        elif camelTiredness > 8:
            print 'You overworked your camel and he died.'
            print ' '
            print 'Game Over'
            done = True


        if thirst > 4 and thirst <=6 and done == False:
            print 'You are thirsty. If you do not drink from your canteen soon, you will die.'
            print ' '
        elif thirst > 6 and done == False:
            print 'You died of thirst.'
            print ' '
            print 'Game Over'
            done = True

        if nativeDistance <= 0 and done == False:
            print 'The natives caught you!'
            print ' '
            print 'Game Over'
            done = True
        elif nativeDistance < 10 and done == False:
            print 'the natives are getting close'
            print ' '
        if milesTraveled >= 200:
            print 'You Win!'
            done = True
        if done == True:
            playAgain()

def playAgain():
    print ' '
    userChoice = raw_input('Would you like to play again? ')
    userChoice = userChoice.upper()
    if userChoice == 'YES':
        Camel()
    elif userChoice == 'NO':
        print 'Bye'

instructions()
