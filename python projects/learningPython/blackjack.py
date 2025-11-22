import random

cardTotal = 0
dealer = random.randint(1, 13)
cardTotal = random.randint(1, 13) + random.randint(1, 13)

while True:
    if cardTotal >= 21:
        print('Bust!')
    else:
        print(dealer)
        que = input('hit or stand? ')
        if que.lower() == 'stand':
            dealer += random.randint(1, 13)
            if dealer >= 21:
                print('You win!')
        elif que.lower() == 'hit':
            cardTotal += random.randint(1, 13)
            if cardTotal != 21:
                print(cardTotal)
                if cardTotal <= 21 and cardTotal >= dealer:
                    print('You win!')
                else:
                    if dealer <= 21:
                        dealer += random.randint(1, 13)
                    continue
    break
input('Press [Enter] to close.')