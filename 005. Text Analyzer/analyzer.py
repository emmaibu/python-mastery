import string
from rich import print
from rich.table import Table
from rich.console import Console
from rich.progress import track
import time

print("""[blue]
┌────────────────────────────────────────┐
│             Text Analyzer              │
└────────────────────────────────────────┘
[/blue]""")

console = Console()

all_letters = string.ascii_lowercase
space = string.whitespace
special_char = string.punctuation
all_vowels = ['a', 'e', 'i', 'o', 'u']
all_consonants = [char for char in all_letters if char not in all_vowels]

def analyser():

    table = Table(title='[bold bright_green]Text Stats[/bold bright_green]')
    table.add_column("Character", style="cyan")
    table.add_column("Count", style="magenta")
    table.add_column("Density", style='grey74')
    
    vowels = []
    consonants = []
    digits = []
    spaces = []
    special_chars = []
    
    print('[bright_cyan]Enter your text\n:[/bright_cyan]', end=' ')
    sentence = input('').lower()

    while len(sentence) == 0:
        print("[red]Please enter some text![/red]")
        return


    for i in sentence:
        if i in all_vowels:
            vowels.append(i)
        elif i in all_consonants:
            consonants.append(i)
        elif i.isdigit():
            digits.append(i)
        elif i in space:
            spaces.append(i)
        elif i in special_char:
            special_chars.append(i)

    
    for step in track(range(10), description='[green]Analyzing...[/green].'): 
        time.sleep(0.1)
    
    print('[green]Done!\nStats ready.[/green]')

    print(f'[bright_cyan]Total characters = {len(sentence)}[/bright_cyan]')

    vowel_density = (len(vowels) / len(sentence)) * 100
    consonant_density = (len(consonants) / len(sentence)) * 100
    digit_density = (len(digits) / len(sentence)) * 100
    space_density = (len(spaces) / len(sentence)) * 100
    special_char_density = (len(special_chars) / len(sentence)) * 100

    table.add_row('Vowels', str(len(vowels)), f'{vowel_density:.1f}%')
    table.add_row('Consonants', str(len(consonants)), f'{consonant_density:.1f}%')
    table.add_row('Digits', str(len(digits)), f'{digit_density:.1f}%')
    table.add_row('Spaces', str(len(spaces)), f'{space_density:.1f}%')
    table.add_row('Special Characters', str(len(special_chars)), f'{special_char_density:.1f}%')
    console.print(table)
    

while True:

    analyser()

    print('[yellow]Do you want to analyse another text?(y/n):[/yellow]', end=' ')
    again = input('')
    while again not in ['y', 'n', 'yes', 'no']:
        print('[bright_red]Please enter y or n: [/bright_red]', end=' ')
        again = input('')
        continue
    if again in ['y', 'yes']:
        continue
    else:
        break

print('[purple]Bye![/purple]')

