import random

def play_game():
    print('Guess the number (1-10)!')
    number_to_guess = random.randint(1, 10)

    attempts = 0

    while True:
        guess = input('\nEnter your guess:')

        if not guess.isdigit() or not (1 <= int(guess) <=10):
            print('Please enter a number between 1 and 10!')
            continue

        guess = int(guess)
        attempts += 1

        if guess == number_to_guess:
            print(f'BOOM! You got it in {attempts} attempt(s)')
            break
        elif guess < number_to_guess:
            print('Too low!')
        else:
            print('Too high!')

print('Welcome to number guessing game!')

while True:
    play_game()
    again = input('Play again (y/n): ').strip().lower()
    while again not in ['y', 'n', 'yes', 'no']:
        again = input('Please type y or n')
    if again not in ['y', 'yes']:
        print('Thanks for playing! Bye!')
        break

