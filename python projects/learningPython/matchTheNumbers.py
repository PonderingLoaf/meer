import random as rand, time, math

num1, num2, num3 = (rand.randint(1, 100) for _ in range(3))
numsList = [num1, num2, num3]

bonus = rand.randint(1, 300)

while True:
    numsGuess = input('Guess 3 numbers: ')
    inputtedNumbers = [item.strip() for item in numsGuess.split(',')]

    if inputtedNumbers == numsList:
        print('You got it all correct!')
    elif inputtedNumbers[0] + inputtedNumbers[1] + inputtedNumbers[2] == bonus:
        print('YOU GOT THE BONUS!!!!')
    else:
        for i in inputtedNumbers:
            if inputtedNumbers[i] == numsList[i]:
                print('You got', i, 'correct!')
                continue