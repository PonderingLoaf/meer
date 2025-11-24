import random as rand
import time

rock = ['rock', '1']
paper = ['paper', '2']
scissors = ['scissors', '3']

wins = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

def main():
    while True:
        compChoice = ''
        numChoice = rand.randint(1,3)
        if numChoice == 1:
            compChoice = 'rock'
        elif numChoice == 2:
            compChoice = 'paper'
        elif numChoice == 3:
            compChoice = 'scissors'

        playerChoice = str(input('Rock, Paper, Scissors: ')).lower()
        print('AI chose', compChoice)
        print('')

        if compChoice == playerChoice:
            print('It was a tie!')
            again = input('Play again? (y/n) ')
            if again in ['y', 'yes']:
                continue
            else:
                exit()
        elif wins[playerChoice] == compChoice:
            print('You win!')
            again = input('Play again? (y/n) ')
            if again in ['y', 'yes']:
                continue
            else:
                exit()
        else:
            print('You lose!')
            again = input('Play again? (y/n) ')
            if again in ['y', 'yes']:
                continue
            else:
                exit()
        break

def exit():
    input('Press any key to close.')

main()