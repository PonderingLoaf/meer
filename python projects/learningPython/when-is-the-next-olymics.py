last = int(input('When was the last olymics? '))
nextlocation = ''

if last + 2 == 2026:
    nextlocation = 'Italy and it is a winter olymics.'
elif last + 2 == 2028:
    nextlocation = 'USA and it is a summer olymics.'
elif last + 2 == 2030:
    nextlocation = 'France and it is a winter olymics.'
elif last + 2 == 2032:
    nextlocation = 'Australia and it is a summer olymics.'
elif last + 2 == 2034:
    nextlocation = 'USA and it is a winter olymics.'
elif last + 2 >= 2035:
    nextlocation = 'an undecided location.'

print('The next olymics will be in', last + 2, 'it will be in', nextlocation)