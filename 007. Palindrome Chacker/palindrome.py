
def checker():

    text = input('Enter you word: ')

    if text == text[::-1]:
        print('This is a plindrome word!')
    else:
        print('Not a palindrome!')
        

while True:
    checker()
    again = input('Do you want to check another word? ')
    if again not in ['y', 'yes']:
        break

print('Bye!')
