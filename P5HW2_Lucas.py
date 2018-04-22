import random

def generateRandomNumber():
    randomNumber = random.randint(1, 100)
    return randomNumber

def askUserForNumber(message = 'Guess the number: '):
    userNumber = int(input(message))
    return userNumber

def checkUserNumber(userNumber, randomNumber):
    if userNumber > randomNumber:
        return 'Too high'
    elif userNumber < randomNumber:
        return 'Too low'
    else:
        return 'Congratulations!'

def main():
    userCongratulated = False
    letsStart = True

    while userCongratulated or letsStart:
        userNumberOfGuesses = 0
        randomNumber = generateRandomNumber()
        
        userNumber = askUserForNumber()
        userNumberOfGuesses += 1
        message = checkUserNumber(userNumber, randomNumber)

        while message != 'Congratulations!':
            print(message)
            userNumber = askUserForNumber('Try again: ')
            userNumberOfGuesses = userNumberOfGuesses + 1
            message = checkUserNumber(userNumber, randomNumber)

        print()
        print(message, 'It took you', userNumberOfGuesses,\
              'attempts to guess correctly\n' )
        userCongratulated = True

main()
