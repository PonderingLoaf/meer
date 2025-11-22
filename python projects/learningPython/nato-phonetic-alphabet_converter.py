dict = {
    'a': 'alpha',
    'b': 'bravo',
    'c': 'charlie',
    'd': 'delta',
    'e': 'echo',
    'f': 'foxtrot',
    'g': 'golf',
    'h': 'hotel',
    'i': 'india',
    'j': 'juliett',
    'k': 'kilo',
    'l': 'lima',
    'm': 'mike',
    'n': 'november',
    'o': 'oscar',
    'p': 'papa',
    'q': 'quebec',
    'r': 'romeo',
    's': 'sierra',
    't': 'tango',
    'u': 'uniform',
    'v': 'victor',
    'w': 'whiskey',
    'x': 'x-ray',
    'y': 'yankee',
    'z': 'zulu',
    ' ': ' ',
    '0': 'launch!',
    '1': 'onek',
    '2': 'twok',
    '3': 'threek',
    '4': 'fork',
    '5': '5 stars!',
    '6': 'six seven!',
    '7': 'six seven!',
    '8': 'yummy',
    '9': 'nein!'
}

idict = {
    'alpha': 'a',
    'bravo': 'b',
    'charlie': 'c',
    'delta': 'd',
    'echo': 'e',
    'foxtrot': 'f',
    'golf': 'g',
    'hotel': 'h',
    'india': 'i',
    'juliett': 'j',
    'kilo': 'k',
    'lima': 'l',
    'mike': 'm',
    'november': 'n',
    'oscar': 'o',
    'papa': 'p',
    'quebec': 'q',
    'romeo': 'r',
    'sierra': 's',
    'tango': 't',
    'uniform': 'u',
    'victor': 'v',
    'whiskey': 'w',
    'x-ray': 'x',
    'yankee': 'y',
    'zulu': 'z',
    ' ': ' ',
    'launch!': '0',
    'onek': '1',
    'twok': '2',
    'threek': '3',
    'fork': '4',
    '5 stars!': '5',
    'SIX seven!': '6',
    'six SEVEN!': '7',
    'yummy': '8',
    'nein!': '9'
}

## English to NATO
def eton():
    name = input('Please enter text: ')

    print(' ')

    for letter in name.lower(): # repeats once for every letter
        if letter == ' ':
            print(dict.get(' ')) # prints an empty line if a space is detected
        else:
            print(letter, 'as in', dict.get(letter)) # prints the letters with their nato phonetic alphabet versions

    print(' ')
    print('"'+ name + '"', 'has been converted to NATO phonetic alphabet.')

    print(' ')
    input("Press Enter to close...")


## NATO to English
def ntoe():
    name = input('Please enter NATO words: ')

    words = name.lower().split() # splits into lowercase words
    
    for word in words: # repeats once for every word
        print(word, 'becomes', idict.get(word)) # prints the NATO PA word + the english translation
    print(' ')
    print('"'+ name + '"', 'has been converted to English.')

    print(' ')
    input("Press Enter to close...")

# Start page

print('NATO phonetic alphabet converter')

program = (input('Convert to NATO(1) or English(2) '))
if program == 1 or 'NATO':
    eton()
elif program == 2 or 'English':
    ntoe()