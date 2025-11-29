import secrets
import string
from rich import print
from rich.console import Console
from rich.progress import track
import time


print('[cyan]Welcome to Password generator\nReccomended length [bold]18-20[/bold]\nMax length [bold]94.[/bold][cyan]')

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

passw_bank = lowercase + uppercase + numbers + symbols


def password_generator():
    
    print('[bright_blue]Enter password length: [/bright_blue]', end='')
    passw_length = input('')

    if not passw_length.isdigit():
        print('[bright_red]Invalid length.[/bright_red]')
        return
    elif int(passw_length) > 94:
        print('[bright_red]Password length cannot be greater than 94.[/bright_red]')
        return
    elif int(passw_length) == 0:
        print('[bright_red]Password length cannot be 0[/bright_red]')
        return
    
    passw_length = int(passw_length)

    _passw = [secrets.choice(passw_bank) for _ in range(passw_length)]
    passw = ''.join(_passw)

    for step in track(range(10), description='[green]Generating...[/green].'): 
        time.sleep(0.1)
    print('[green]Password ready[/green]')

    print(f'[magenta]Your password: [/magenta][grey74]{passw}[/grey74]')

while True:

    password_generator()

    print('[bright_blue]Do you want to generate a password again?(y/n): [/bright_blue]', end='')
    again = input('').lower().strip()
    while again not in ['y', 'n', 'yes', 'no']:
        again = input('Please enter y or n: ')
        continue
    if again not in ['y', 'yes']:
        break
    
print('[blink blue]Bye! Keep using strong passwords![/blink blue]')
