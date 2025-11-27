import math
from rich import print
from rich.progress import track
from rich.console import Console
from rich.table import Table
import time

console = Console()

table = Table(title='History')
table.add_column("Expression", style="cyan")
table.add_column("Result", style="magenta")

features = """[purple]PyCalc Ultra v1[/purple]
[bright_cyan]Features[/bright_cyan]
[grey74]- Performs basic operations (+, -, *, /, **, python math functions, e.t.c)
- Storage and access to history which can also be cleared.
- can perfom operations using the python math module e.g math.log10(100)
- Enter 'h' to check history • enter 'q' to quit • enter 'f' to check the calculator features.[/grey74]"""

print("""[blue]
┌─────────────────────────────────────┐
│          PyCalc Ultra v1            │
└─────────────────────────────────────┘
[/blue]
[grey74]Enter 'h' to check history • enter 'q' to quit • enter 'f' to check the calculator features.[/grey74]
""")
print("[bright_cyan]Start calculating[/bright_cyan]")


while True:   
    expression = input("> ").lower().strip()

    if expression == 'f':
        print(features)
        continue
    if expression == 'q':
        break
    if expression == 'h':
        console.print(table)
        continue
    else:
        try:
            result = eval(expression)
            print(f"[bright_green]= {result}[/bright_green]")
            table.add_row(expression, str(result))
            continue
        except (ZeroDivisionError, SyntaxError, NameError, TypeError):
            print('[yellow]Invalid Syntax.[/yellow]')
            continue
    
    
for step in track(range(5), description='[red]Shuting down calculator...[/red].'): 
    time.sleep(0.2)

print('[yellow]Calculator Ofline[/yellow]')
