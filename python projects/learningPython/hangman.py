import random, time, json

with open("hangman.json", "r") as hang:
        possibleWords = json.load(hang)

word = random.choice(possibleWords)
guessedLetters = set()
guessCount = 9

while True:
    if guessCount > 0:
        guess = input("Guess a letter: ").lower()
    else:
        print('You lose!')
        time.sleep(1)
        break

    if len(guess) != 1:
        print("Please guess a single letter.")
        continue
    
    guessedLetters.add(guess)

    if guess in word:
        print(guess, "is in the word!")
    else:
        print(guess, "is not in the word!")
        guessCount -= 1

    display = ""
    for letter in word:
        if letter in guessedLetters:
            display += letter
        else:
            display += "_"

    print(display)
    print()

    if "_" not in display:
        print("You win!")
        break

    time.sleep(1)