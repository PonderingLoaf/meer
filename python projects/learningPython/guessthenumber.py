import random as rand, time

num = 0

def createNum(dif):
    if dif == 'easy':
        num = rand.randint(1, 100)
        game(num, 12)
    elif dif == 'medium':
        num = rand.randint(1, 1000)
        game(num, 9)
    elif dif == 'hard':
        num = rand.randint(1, 10000)
        game(num, 6)
    elif dif == 'wtf':
        num = rand.randint(1, 100000)
        game(num, 3)

def game(num, remainingGuesses):
    while True:
        player = int(input('Input a number: '))
        if num == player:
            print('You win! The number was', num)
            time.sleep(2)
            difSelector
        elif remainingGuesses == 0:
            print('Out of guesses! The number was', num)
            time.sleep(2)
            difSelector()
        elif num != player:
            remainingGuesses -= 1
            print('Not right', remainingGuesses, 'guesses left...')
            hint = str(input('Would you like a hint? ')).strip().lower()
            if hint in ['yes', 'y']:
                if player <= num:
                    print('You need to go higher!')
                    continue
                else:
                    print('You need to go lower!')
                    continue
            else:
                continue

def difSelector():
    dif = str(input('Choose a difficulty (easy, medium, hard, wtf) ')).lower().strip()
    createNum(dif)

difSelector()