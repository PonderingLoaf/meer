num = int(input('Input a whole number: '))

def numCanBe2(num):
    if num % 2 == 0:
        return True
    else:
        return False

if numCanBe2(num):
    print("even")
else: print("odd")