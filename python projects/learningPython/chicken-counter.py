import random

chick = random.randint(1, 10)
text = ''
count = chick

while chick != 0:
    text = text + 'bagawk '
    chick -= 1

print(text)

howMany = int(input('How many chickens are there? '))

if int(howMany) == count:
    print('Correct! There was ' + str(count), 'chickens.')
elif int(howMany) != count:
    print('Sorry, that is not correct')

input('Press [Enter] to close')